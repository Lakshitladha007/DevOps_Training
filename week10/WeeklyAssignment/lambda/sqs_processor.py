import boto3
import os
import zipfile
import json
import csv
import logging

# Setup logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3_client = boto3.client('s3')

# Parse an S3 URI into bucket and key
def parse_s3_uri(s3_uri):
    
    s3_uri = s3_uri.replace("s3://", "")
    bucket, key = s3_uri.split("/", 1)
    return bucket, key

# Download an object from S3 to local path
def download_file_from_s3(bucket, key, download_path):
    try:
        logger.info(f"Downloading s3://{bucket}/{key} to {download_path}")
        s3_client.download_file(bucket, key, download_path)
        logger.info("Download successful.")
    except Exception as e:
        logger.error(f"Failed to download file: {e}")
        raise

# Extract zip file to a directory.
def unzip_file(zip_path, extract_dir):
    try:
        logger.info(f"Extracting {zip_path} to {extract_dir}")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        logger.info("Extraction complete.")
    except Exception as e:
        logger.error(f"Failed to unzip file: {e}")
        raise

# Convert .txt or .json file content to CSV format
def convert_txt_json_to_csv(file_path, csv_path):
    try:
        logger.info(f"Converting {file_path} to CSV {csv_path}")
        if file_path.endswith('.txt'):
            with open(file_path, 'r') as txt_file, open(csv_path, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                for line in txt_file:
                    row = line.strip().split(",")
                    writer.writerow(row)
        
        elif file_path.endswith('.json'):
            with open(file_path, 'r') as json_file, open(csv_path, 'w', newline='') as csv_file:
                data = json.load(json_file)
                if not isinstance(data, list) or len(data) == 0:
                    logger.warning(f"JSON file {file_path} is empty or not a list. Skipping.")
                    return
                # Use keys from first dict as header
                header = data[0].keys()
                writer = csv.DictWriter(csv_file, fieldnames=header)
                writer.writeheader()
                for entry in data:
                    writer.writerow(entry)
        else:
            logger.warning(f"Unsupported file type for conversion: {file_path}")
            return
        logger.info(f"Conversion complete for {file_path}")
    except Exception as e:
        logger.error(f"Failed to convert {file_path} to CSV: {e}")
        raise

# Upload a local file to S3 bucket with specified key.
def upload_file_to_s3(bucket, key, file_path):

    try:
        logger.info(f"Uploading {file_path} to s3://{bucket}/{key}")
        s3_client.upload_file(file_path, bucket, key)
        logger.info("Upload successful.")
    except Exception as e:
        logger.error(f"Failed to upload file: {e}")
        raise

def lambda_handler(event, context):
    try:
        logger.info(f"Received event: {event}")

        # Extract S3 URI from SQS message body
        records = event.get("Records", [])
        if not records:
            logger.error("No records found in event.")
            return

        s3_uri = records[0]["body"]
        logger.info(f"SQS Message (S3 URI): {s3_uri}")

        # Parse bucket and key
        bucket, key = parse_s3_uri(s3_uri)

        # Prepare local paths
        file_name = os.path.basename(key) # extract file name form complete path
        zip_path = f"/tmp/{file_name}"
        extract_dir = "/tmp/extracted_files"
        os.makedirs(extract_dir, exist_ok=True)

        # Download ZIP file from S3
        download_file_from_s3(bucket, key, zip_path)

        # Extract ZIP file
        unzip_file(zip_path, extract_dir) # source=zip_path and destination=extract_dir

        # Process extracted files: convert .txt and .json to CSV and upload
        for root, _, files in os.walk(extract_dir):
            for file in files:
                if file.endswith(('.txt', '.json')):
                    file_path = os.path.join(root, file)
                    csv_file_name = os.path.splitext(file)[0] + ".csv"
                    csv_path = os.path.join("/tmp", csv_file_name)

                    convert_txt_json_to_csv(file_path, csv_path)

                    # Upload converted CSV to s3 output folder
                    s3_output_key = f"output/{csv_file_name}"
                    upload_file_to_s3(bucket, s3_output_key, csv_path)

        logger.info("Lambda processing completed successfully.")

    except Exception as e:
        logger.error(f"Error in lambda_handler: {e}")
        raise

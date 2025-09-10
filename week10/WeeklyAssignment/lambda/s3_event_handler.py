import json
import logging
import boto3
from botocore.exceptions import ClientError

# Setup logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS clients outside handler for re-use
s3 = boto3.client('s3')
sns = boto3.client('sns')
sqs = boto3.client('sqs')

QUEUE_URL = "https://sqs.ap-south-1.amazonaws.com/867344449786/my-message-queue"
SNS_TOPIC_ARN = 'arn:aws:sns:ap-south-1:867344449786:file-upload-notify'

# Extract S3 bucket and key from the Lambda event and return the S3 path string.
def extract_s3_path(event):
    try:
        record = event['Records'][0]
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        s3_path = f's3://{bucket}/{key}'
        logger.info(f"Extracted S3 path: {s3_path}")
        return s3_path
    except ClientError as e:
        logger.error(f"Failed to extract S3 path: {e}")
        raise

# Send a message to the specified SQS queue.
def send_message_to_sqs(message_body):
    try:
        response = sqs.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=message_body
        )
        logger.info(f"Message sent to SQS successfully: MessageId={response.get('MessageId')}")
        return response
    except ClientError as e:
        logger.error(f"Failed to send message to SQS: {e}")
        raise


# Publish a notification to the specified SNS topic.
def publish_sns_notification(subject, message):
    try:
        response = sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject=subject
        )
        logger.info(f"SNS notification published successfully: MessageId={response.get('MessageId')}")
        return response
    except ClientError as e:
        logger.error(f"Failed to publish SNS notification: {e}")
        raise

# Extracts S3 file path, sends it to SQS, and publishes SNS notification.
def lambda_handler(event, context):
    try:
        s3_path = extract_s3_path(event)

        send_message_to_sqs(s3_path)

        publish_sns_notification(
            subject='File Upload Notification',
            message=f'A new file has been uploaded: {s3_path}'
        )

        logger.info("Lambda execution completed successfully.")
        return {
            'statusCode': 200,
            'body': json.dumps('Message sent to SNS and SQS!')
        }

    except ClientError as e:
        logger.exception(f"Error processing Lambda event: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error: {e}")
        }

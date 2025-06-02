import logging
import argparse
import json
import os

def_filename="demo.log"
args=None

def initialize_parser():
    global args
    parser=argparse.ArgumentParser()
    parser.add_argument("--configfilename", help="config file from which data is to be read")
    parser.add_argument("--filename", help="the file where logs are tobe written")
    args= parser.parse_args()
    global def_filename
    if args.filename:
        def_filename=args.filename

def intialize_logger():
    logging.basicConfig(
      filename=def_filename,
      level=logging.INFO, 
      format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.info("Successfully initialized the logger")

def write_data():
    global args
    try: 
        if not args.configfilename:
            raise ValueError("Config file argument is missing!")
        
    except ValueError as e:
        logging.warning(f"Warning: {e}")
        return
    
    if not os.path.exists(args.configfilename):
        print("File does not exist")
        logging.warning("Warning: File does not exist.")
        return
    
    logging.info("Started writing the data")
    with open(args.configfilename, "r") as f:
        data=f.read()
    json_data=json.loads(data)
    logging.info(json_data)
    logging.info("Successfully wrote the data")

if __name__ == "__main__":
    initialize_parser()
    intialize_logger()
    write_data()




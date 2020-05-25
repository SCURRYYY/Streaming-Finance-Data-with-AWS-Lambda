import json
import boto3
import os
import subprocess
import sys
CHOICES = ["TECHNOLOGY", "ENERGY", "FINANCIAL"]
#subprocess.check_call([sys.executable, "-m", "pip", "install", "--target", "/tmp", 'yfinance'])
#sys.path.append('/tmp')
#import yfinance as yf
def lambda_handler(event, context):
    output_records = []
    for record in event["records"]:
        output_records.append({
            "recordId": record['recordId'],
            "result": "Ok",
            "data": record["data"] + "Cg==" # this is the key here
        })
        
    return { "records": output_records }

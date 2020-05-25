import boto3
import os
import subprocess
import sys
import json

subprocess.check_call([sys.executable, "-m", "pip", "install", "--target", "/tmp", 'yfinance'])
sys.path.append('/tmp')
import yfinance as yf

def lambda_handler(event, context):
    fh = boto3.client("firehose", "us-east-2")
    #define the time 
    start_date = '2020-05-14'
    end_date = '2020-05-15'
    #select the assets from yfinance 
    assets = ['FB', 'SHOP', 'BYND', 'NFLX', 'PINS', 'SQ', 'TTD', 'OKTA', 'SNAP', 'DDOG']
    for asset in assets:
    	#get the data 
        get_data = yf.download(asset, start = start_date, end = end_date, interval = '1m')
        for index, row in get_data.iterrows():
            output = {"high":row['High'],"low":row['Low'],
                      "ts":index.strftime('%m/%d/%Y %X'),"name":asset}        
            # Convert the data into JSON
            as_jsonstr = json.dumps(output)   
            # Pass the stream info where the data should be stored as a single batch
            fh.put_record(
                DeliveryStreamName="delivery-stream-test", 
                Record = {'Data': as_jsonstr.encode('utf-8')})
                     
    # Return the JSON file dump    
    return {
        'statusCode': 200,
        'body': json.dumps(f'Done! Recorded: {as_jsonstr}')
    }


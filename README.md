# Streaming-Finance-Data-with-AWS-Lambda

#### The project is aimed to use lambda function to generate near real time finance data records for downstream processing and interactive querying. 

#### This project consists of three infrastructure elements parts: 
#### 1. Data Transformer
####        - We will create a Kinesis Firehose Delivery Stream which have a lambda function that transforms the records and streams it into an S3 bucket. 
#### 2. Data Collector 
####        - We will write a lambda function to get stock price data and place it into the delivery (DataTransformer).
#### 3. Data Analyzer
####        - We will use AWS Athena to gain insight into our streamed data.














## DataCollector Lambda configuration page
<img width="1208" alt="Screen Shot 2020-05-24 at 17 05 03" src="https://user-images.githubusercontent.com/60529752/82765539-c831cd00-9de5-11ea-924b-f014e88d9310.png">








## Kinesis Data Firehose Delivery Stream Monitoring
<img width="1100" alt="Screen Shot 2020-05-24 at 17 31 08" src="https://user-images.githubusercontent.com/60529752/82765525-acc6c200-9de5-11ea-84e8-8f39ca1ffb3e.png">


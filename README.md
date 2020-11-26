# Cisco Umbrella with ElasticStack 7.x

This repository describes the necessary steps and configuration of Umbrella and ElasticStack to ingest Umbrella logs for long-term analysis (>30 days)

- elasticsearch: The mappings needed for the index created by Umbrella
- logstash: The plugin configurations to ingest data from the S3 bucket and convert the CSV files to documents

## Logstash environment variables
Variable name | Description
--------------|--------------
S3_ACCESS_KEY | The AWS S3 bucket access key
S3_SECRET_KEY | The AWS S3 bucket secret key
S3_REGION | The AWS region in which the S3 bucket is located
S3_BUCKET | The S3 bucket name, without the s3:// prefix
S3_PREFIX | The prefix or directory name of the log files inside the S3 bucket


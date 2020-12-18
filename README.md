# Serverless_Fraud_detection_pipeline

CSYE7245 - Serverless Transactions Fraud Detection & Notification
December  18, 2020
Team-2
•	Manish Singh
•	Phu Tran
•	Kaviya Sachi
•	Rajavi Mehta
Overview
Did you know that each year, tens of billions of dollars are lost to online fraud world-wide?
Companies with online businesses have to constantly be on guard for fraudulent activity such as fake accounts and payments made with stolen credit cards.  One way they try to identify fraudsters is by using fraud detection apps, some of which use Machine Learning (ML).
Transaction Fraud Detection is a fully managed service that makes it easy to identify potentially fraudulent online Transaction such as online payment fraud.
Enter our Transaction Fraud Detection app. It uses historical data, ML to identify potentially fraudulent online activity so you can catch more fraud faster. You can create a fraud detection model with just a few clicks and no prior ML experience because Fraud Detector handles all of the ML heavy lifting for you.

Architecture
 

Setup
The pipeline requires an Amazon Web Services account to deploy and run. Signup for an AWS Account here. The pipeline uses the folllowing AWS Services:
•	Streamlit app
•	Amazon cognito
•	Api Gateway
•	Amazon SNS
•	Amazon SQS
•	Amazon SES
•	Step Function
•	Lambda Function
•	Amazon Fraud Detector
•	Amazon S3
•	Amazon RDS
•	Amazon Quick Sight

Deploying Lambda Functions
The pipeline extensively uses AWS Lambda Functions for Serverless Computing. All directories on this repo marked with the prefix lambda- are Lambda functions that have to be deployed on AWS. All functions follow a common deployment process.
Deploy serverless Python code in AWS Lambda
Python Lambda is toolkit to easily package and deploy serverless code to AWS Lambda. Packaging is requried since AWS Lambda functions only ship with basic Python libraries and do not contain external libraries. Any external libraries to be used will be have to be packaged into a .zip and deployed to AWS Lambda. More information about Python Lambda can be found here
Setup your config.yaml
All lambda- directories contain a config.yaml file with the configuration information required to deploy the Lambda package to AWS. Configure the file with your access keys, secret access keys and function name before packaging and deploying the Python code. An example is as follows
region: us-east-1

function_name: Lambda_Function_1
handler: service.handler
description: Deployed lambda Function
runtime: python3.7
role: <Enter the role name created earlier>

# if access key and secret are left blank, boto will use the credentials
# defined in the [default] section of ~/.aws/credentials.
aws_access_key_id: <Enter your Access Keys>
aws_secret_access_key: <Enter your Secret Access Keys>

timeout: 15
memory_size: 512

environment_variables:
    ip_bucket: <enter_your_S3_Bucket>

# Build options
build:
  source_directories: lib
Create a Virtual Environment
pipenv shell --python 3.7
pip3 install python-lambda
All package dependencies are available in the respective lambda- directories on this repository
Install all Python dependencies
pip3 install -r requirements.txt
Initiate Lambda Deployement
lambda init
This will create the following files: event.json, __init__.py, service.py, and config.yaml Replace the created service.py and config.yaml files with the service.py and config.yaml files in the respective lambda- directory on this repository.
Package and Deploy Lmabda function
lambda deploy
This should create a new Lambda function on your AWS Lambda Console. Follow the same steps for all lambda directories on this repository to deploy packages to AWS Lambda.


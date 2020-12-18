import json
import boto3
import time
import uuid 
  

client = boto3.client('stepfunctions')

def lambda_handler(event, context):

    body = event["Records"][0]["body"]
    bodyFormatted = json.loads(body)
    message = json.loads(bodyFormatted['Message'])
    # extract contents

    
    transactionId = str(uuid.uuid1())[0:9]
    message['transactionId'] = transactionId
  
    input_json= json.dumps(message)
    
    print(input_json)
            
    response = client.start_execution(
          input= input_json,
          name =transactionId,
          stateMachineArn= "*********"
          )
          
    print(response)
    
    
    

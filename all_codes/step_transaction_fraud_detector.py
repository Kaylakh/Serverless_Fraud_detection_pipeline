import json
import boto3

from random import randint



frauDetector = boto3.client('frauddetector')

def lambda_handler(event, context):
    
    id_29 = event['id_29']
    id_31 = event['id_31']
    DeviceType = event['DeviceType']
    DeviceInfo = event['DeviceInfo']
    TransactionDT = event['TransactionDT']
    TransactionAmt = event['TransactionAmt']
    ProductCD = event['ProductCD']
    card1 = event['card1']
    card4 = event['card4']
    card6 = event['card6']
    addr1 = event['addr1']
    addr2 = event['addr2']
    email = event['email']


    result = frauDetector.get_event_prediction(
        detectorId='transaction_fraud_detector',
        eventId='123456',
        eventTimestamp='2020-12-16T13:26:33Z',
        eventTypeName='transactions_fraud_event',
        entities=[{'entityType': 'transaction', 'entityId': '1234'}],
        eventVariables={
            'transaction_amt': TransactionAmt,
            'card4': card4,
            'card6': card6,
            'device_info': DeviceInfo,
            'device_type': DeviceType,
            'id_29': id_29,
            'id_31': id_31,
            'p_emaildomain': email,
            'product_cd': ProductCD,

        })
    outcome = result["ruleResults"][0]["outcomes"][0]

    print(outcome)
    event['outcome'] = outcome
    return event
    

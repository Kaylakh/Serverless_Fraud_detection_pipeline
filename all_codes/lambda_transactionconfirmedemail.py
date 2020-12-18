import json
import boto3

ses = boto3.client('ses')
def mask_number_in_card(card):
    if len(card) == 10 :
        hash_card = card.replace(card[0:6], '#####')
        return hash_card
    else:
        raise exception
    
def lambda_handler(event, context):
    # extract message
    body = event["Records"][0]["body"]
    bodyFormatted = json.loads(body)
    message = json.loads(bodyFormatted['Message'])
    
    # extract contents
    id_29 = message['id_29']
    id_31 = message['id_31']
    DeviceType = message['DeviceType']
    DeviceInfo = message['DeviceInfo']
    TransactionDT = message['TransactionDT']
    TransactionAmt = message['TransactionAmt']
    ProductCD =message['ProductCD']
    card1 = mask_number_in_card(message['card1'])
    card4 = message['card4']
    card6 = message['card6']
    addr1 = message['addr1']
    addr2 = message['addr2']
    email = message['email']
    
    
    
    # 
    emailBody = f""" Your transaction is in process. Here is a sumary of your order:
         {id_29}- {id_31}- {DeviceInfo}- {DeviceType}- {TransactionAmt}- {TransactionDT}- {ProductCD}-{card1}- {card4}- {card6}- {addr1}- {addr2}- {email}     
    
    """
    
    ses.send_email(Source = 'tranphu2495@gmail.com', 
                   Destination = {'ToAddresses':[email]},
                   Message={
                       'Subject':{
                           'Data': 'Your Transaction has been submitted'
                       },
                       'Body': {
                           'Text':{
                               'Data': emailBody
                           }
                         
                       }
                   })
                   
   
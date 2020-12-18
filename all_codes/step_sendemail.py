import json
import boto3

#frauDetector = boto3.client('frauddetector')
ses = boto3.client('ses')


#masking card details
def mask_number_in_card(card):
    if len(card) == 10:
        hash_card = card.replace(card[0:6], '#')
        return hash_card
    else:
        raise exception


def lambda_handler(event, context):

    outcome = event['outcome']
    email = event['email']
    TransactionAmt = event['TransactionAmt']
    card1 = event['card1']

    print(outcome)

    emailBody = ''
    if outcome == 'low_risk':
        emailBody = f" Your transaction has been approved. Your transaction amount is {TransactionAmt}"
    else:
        emailBody = f" Your transaction has been declined "

    ses.send_email(Source="tranphu2495@gmail.com",
                   Destination={'ToAddresses': [email]},
                   Message={
                       'Subject': {
                           'Data': 'Transaction Status'
                       },
                       'Body': {
                           'Text': {
                               'Data': emailBody
                           }

                       }
                   })
    
    return "Success"
    
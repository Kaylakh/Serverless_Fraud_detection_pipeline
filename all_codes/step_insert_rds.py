import json
import boto3
import pymysql



#rds connection
rds_endpoint='db-transaction.cme2zmutnvvg.us-east-1.rds.amazonaws.com'
username= 'admin'
password= 'admin2020'
db_name='transaction'
conn=None
conn = pymysql.connect(host=rds_endpoint, user=username, password=password, db='transaction')



def lambda_handler(event, context):
    try:
        transactionId =  event['transactionId']
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
        outcome = event['outcome']


        if outcome == 'low_risk':
            isfraud = 0
        else:
            isfraud = 1

        with conn.cursor() as cur:
            # Create a new record
            print(">>>>Before Insert")
            cur.execute(" \
                    insert into `fraud`(`TransactionID`,`id_29`,`id_31`,`DeviceType`,`DeviceInfo`,`isfraud`,`TransactionDT`,`TransactionAmt`,`ProductCD`,\
                                   `card1`,`card4`,`card6`,`addr1`,`addr2`,`P_emaildomain`)       \
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", \
                        (transactionId, id_29, id_31, DeviceType, DeviceInfo,isfraud, TransactionDT, TransactionAmt, ProductCD,
                         card1, card4, card6, addr1, addr2, email))

        conn.commit()
        print(">>>>Insert success")
        with conn.cursor() as cur:
            # Read a single record
            print(">>>inside second cursor")
            cur.execute("SELECT *  FROM fraud where id = (select max(id) from fraud)")
            sqlresult = cur.fetchone()
            print(sqlresult)

        return {
            'body': sqlresult
        }
    finally:
        cur.close()

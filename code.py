import json
import boto3
import datetime
import time
from faker import Faker
import random
import string
from time import sleep
import os

fake = Faker() # library to generate synthetic transaction info
kinesis_client = boto3.client('kinesis', region_name='eu-west-2')

def lambda_handler(event, context):
    print(event)
    noe_j = event['queryStringParameters']
    number_of_events = int(noe_j['create'])
    print(number_of_events)
    myDataStream1 = str(os.environ['myDataStream']) # reference environmental variable

    def data_for_stream():
        kinesis_client.put_record(
        StreamName=myDataStream1,
        Data=json.dumps(write_record()),
        PartitionKey='my-partition'
    )


    def write_record():
        name = fake.name()
        IP = fake.ipv4_private()
        EventTime = str(datetime.datetime.now())
        AccountNumber = random.randint(10000000, 19999999)
        location = fake.country()
        randnum = random.randint(1, 150) # lower transaction amount
        transaction_id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    
        record = '''
                {
                    "AccountNum": "'''+str(AccountNumber)+'''",
                    "EventTime": "'''+(EventTime)+'''",
                    "Name": "'''+str(name)+'''",
                    "IP_Address": "'''+str(IP)+'''",
                    "TransactionID": "'''+str(transaction_id)+'''",
                    "Amount": "'''+str(randnum)+'''",
                    "Country": "'''+str(location)+'''"
                }
            '''
        dataJ = json.loads(record)
        print(dataJ)
        return dataJ
        
    print('Number of events created ' + str(number_of_events))
    counter = 0
    while number_of_events > counter:
        print(data_for_stream())
        counter = counter + 1
    return ("Event creation triggered successfully")
#!/usr/bin/env python3

#full package imports
import os
import sys
import pif
import time

#partial imports
from godaddypy import Client,Account

domain = os.environ['DGDP_DOMAIN']
a_record = os.environ['DGDP_ARECORD']
record_type = os.environ['DGDP_RECORDTYPE']
api_key = os.environ['DGDP_APIKEY']
api_secret = os.environ['DGDP_APISECRET']
sleep_time = float(os.environ['DGDP_SLEEPTIME'])

var = 1

while var == 1:

    print("Sleeping")
    time.sleep( sleep_time ) 
   
    userAccount = Account(api_key=api_key, api_secret=api_secret)
    userClient = Client(userAccount)
    publicIP = pif.get_public_ip('ident.me')
    
    try:
        records = userClient.get_records(domain, name=a_record, record_type=record_type)
        
        if (len(records) == 0):
            print("No record found. Creating new one.")

            if (userClient.add_record(domain, {'data':publicIP, 'name':'@', 'ttl':3600, 'type':record_type})):
                records = userClient.get_records(domain, name=a_record, record_type=record_type)
    
        for record in records:

            if publicIP != record["data"]:
                updateResult = userClient.update_record_ip(publicIP, domain, name=a_record, record_type=record_type)

                if updateResult != True:
                    print('Error updating DNS');

            else:
                print('No DNS update needed.')

    except:
        print(sys.exc_info()[1])
        sys.exit
   	

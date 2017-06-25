#!/usr/bin/env python3

#full package imports
from datetime import datetime
import os
import sys
import pif
import time

#partial imports
from godaddypy import Client,Account

domain = os.environ['DGDP_DOMAIN']
#a_record='@'
record_type = os.environ['DGDP_RECORDTYPE']
api_key = os.environ['DGDP_APIKEY']
api_secret = os.environ['DGDP_APISECRET']
subdomains = os.environ['DGDP_SUBDOMAINS'].split(',')
sleep_time = float(os.environ['DGDP_SLEEPTIME'])

var = 1

while var == 1:

    userAccount = Account(api_key=api_key, api_secret=api_secret)
    userClient = Client(userAccount)
    publicIP = pif.get_public_ip('ident.me')

    print('--------------------') 
    print(datetime.now())
    print(publicIP)

    # subdomains_tmp will contain the subdomains to be created
    # after the current registered subdomains are updated
    subdomains_tmp = list(subdomains)
    
    try:
        records = userClient.get_records(domain, record_type=record_type)
        for record in records:
            if record["name"] in subdomains:
                print(record["name"])
                subdomains_tmp.remove(record["name"])
                if publicIP == record["data"]:
                    updateResult = True
                else:
                    updateResult = userClient.update_record_ip(publicIP, domain, name=record["name"], record_type=record_type)
                    print('Registry updated.')

                if updateResult != True:
                     print('Error updating registry.');

        for subdomain in subdomains_tmp:

            print(subdomain)
            print('Creating subdomain');

            if userClient.add_record(domain, {'data':publicIP, 'name':subdomain, 'ttl':3600, 'type':record_type}):
               print('Subdomain created')
            else:
               print('Subdomain creation error')
 


    except:
        print(sys.exc_info()[1])

    time.sleep( sleep_time ) 

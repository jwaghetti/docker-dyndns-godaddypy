#!/usr/bin/env python3

#full package imports
from datetime import datetime
from email.mime.text import MIMEText
import os
import sys
import smtplib
import pif
import time

#partial imports
from godaddypy import Client,Account

def sendMail(ip, mailFrom, mailTo):
  try:
    msg = MIMEText('The IP address of asmodai host changed to: ' + ip)
    msg['Subject'] = 'asmodai IP update: ' + ip
    msg['From'] = mailFrom 
    msg['To'] = mailTo 
    smtp = smtplib.SMTP(smtpServer, smtpPort)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo
    smtp.login(smtpUser, smtpPassword)
    smtp.sendmail(mailFrom, [mailTo], msg.as_string())
    smtp.quit()
  except:
    print("Error sending update e-mail")

domain = os.environ['DGDP_DOMAIN']
#a_record='@'
record_type = os.environ['DGDP_RECORDTYPE']
api_key = os.environ['DGDP_APIKEY']
api_secret = os.environ['DGDP_APISECRET']
subdomains = os.environ['DGDP_SUBDOMAINS'].split(',')
sleep_time = float(os.environ['DGDP_SLEEPTIME'])

mailFrom = os.environ['DGDP_MAILFROM']
mailTo = os.environ['DGDP_MAILTO']
mailSubject = os.environ['DGDP_MAILSUBJECT']
sendmail = bool(os.environ['DGDP_SENDMAIL'])
smtpServer = os.environ['DGDP_SMTPSERVER']
smtpPort = os.environ['DGDP_SMTPPORT']
smtpUser = os.environ['DGDP_SMTPUSER']
smtpPassword = os.environ['DGDP_SMTPPASSWORD']

lastIP = '0.0.0.0'

var = 1

while var == 1:

  try:

    userAccount = Account(api_key=api_key, api_secret=api_secret)
    userClient = Client(userAccount)
    publicIP = pif.get_public_ip('ident.me')

    print('--------------------') 
    print(datetime.now())
    print(publicIP)

    if (publicIP != lastIP and sendmail == True):
      sendMail(publicIP, mailFrom, mailTo)


    # subdomains_tmp will contain the subdomains to be created
    # after the current registered subdomains are updated
    subdomains_tmp = list(subdomains)
    
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

  lastIP = publicIP

  time.sleep( sleep_time ) 

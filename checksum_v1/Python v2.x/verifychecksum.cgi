#!/usr/bin/python

import Checksum
#import requests
import base64
#import json
#import requests

print "Content-type: text/html\n"
MERCHANT_KEY = 'XXXXXXXXXXX';
#import cgi

response_params= {}  # Pass paytm response here
respons_dict = {}

for i in response_params.keys():
 respons_dict[i]=response_params[i].value
 if i=='CHECKSUMHASH':
    checksum = response_params[i].value

if 'GATEWAYNAME' in respons_dict:
	if respons_dict['GATEWAYNAME'] == 'WALLET':
		respons_dict['BANKNAME'] = 'null';

verify = Checksum.verify_checksum(respons_dict, MERCHANT_KEY, checksum)

print verify

#if checksum is validated Kindly verify the amount and status 
#if transaction is successful 
#kindly call Paytm Transaction Status API and verify the transaction amount and status.
#If everything is fine then mark that transaction as successful into your DB.
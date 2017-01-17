#!/usr/bin/python

import Checksum
import requests
import base64
import json
import requests

print "Content-type: text/html\n"
MERCHANT_KEY = 'kbzk1DSbJiV_O3p5';
import cgi

form = cgi.FieldStorage()
respons_dict = {}

respons_dict['MID'] = '';
respons_dict['ORDER_ID'] = '';
respons_dict['CUST_ID'] = '';
respons_dict['INDUSTRY_TYPE_ID'] = '';
respons_dict['CHANNEL_ID'] = '';
respons_dict['TXN_AMOUNT'] = '';
respons_dict['WEBSITE'] = '';

Orderid = "";
for i in form.keys():
 respons_dict[i]=form[i].value
 if i=='ORDER_ID':
    Orderid = form[i].value
 
#below code snippet is mandatory, so that no one can use your checksumgeneration url for other purpose .   
for i in respons_dict:    
    if("REFUND" in respons_dict[i]):
        respons_dict = {}
        exit()


checksum = Checksum.generate_checksum(respons_dict, MERCHANT_KEY)

paramarr = {};
paramarr['ORDER_ID'] = Orderid;
paramarr['CHECKSUMHASH'] = checksum;
paramarr['payt_STATUS'] = '1';


param_dict = json.dumps(paramarr, separators=(',', ':'))
print param_dict



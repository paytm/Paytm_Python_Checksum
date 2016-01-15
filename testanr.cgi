#!/usr/bin/python

import Checksum
import requests
import base64
import json
import cgi
import requests
print "Content-type: application/json\n"

form = cgi.FieldStorage()
respons_dict = {}
for i in form.keys():
 respons_dict[i]=form[i].value
 if i=='CHECKSUMHASH':
    checksum = form[i].value

#print respons_dict
MERCHANT_KEY = 'kbzk1DSbJiV_O3p5';

param_dict = {}
checkSum = Checksum.generate_checksum(respons_dict, MERCHANT_KEY)

param_dict['CHECKSUMHASH'] = checkSum
param_dict['ORDER_ID'] = respons_dict['ORDER_ID']
param_dict['payt_STATUS'] = '1'

print json.dumps(param_dict, separators=(',', ':'))

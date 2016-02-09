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
Orderid = "";
for i in form.keys():
 respons_dict[i]=form[i].value
 if i=='ORDER_ID':
    Orderid = form[i].value


checksum = Checksum.generate_checksum(respons_dict, MERCHANT_KEY)

paramarr = {};
paramarr['ORDER_ID'] = Orderid;
paramarr['CHECKSUMHASH'] = checksum;
paramarr['payt_STATUS'] = '1';


param_dict = json.dumps(paramarr, separators=(',', ':'))
print param_dict



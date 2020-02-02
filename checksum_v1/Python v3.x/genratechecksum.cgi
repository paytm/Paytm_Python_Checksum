#!/usr/bin/python3

import cgitb
cgitb.enable()

import Checksum
#import requests
import base64
#import json
#import requests

print("Content-type: text/html\n\n");
MERCHANT_KEY = 'XXXXXXXXXXXXXXXX';
#import cgi

#form = cgi.FieldStorage()
respons_dict = {}

respons_dict['MID'] = 'XXXXXXXXXXXXXXXXXXXX';   #Provided by Paytm
respons_dict['ORDER_ID'] = 'ORDER0000001'; #unique OrderId for every request
respons_dict['CUST_ID'] = 'CUST00001'; # unique customer identifier 
respons_dict['INDUSTRY_TYPE_ID'] = 'Retail'; #Provided by Paytm
respons_dict['CHANNEL_ID'] = 'WAP'; #Provided by Paytm
respons_dict['TXN_AMOUNT'] = '1.00'; #transaction amount
respons_dict['WEBSITE'] = 'XXXXXXXX'; #Provided by Paytm
respons_dict['EMAIL'] = 'abc@gmail.com'; #customer email id
respons_dict['MOBILE_NO'] = '7777777777'; #customer 10 digit mobile no.
respons_dict['CALLBACK_URL'] = 'https://domain/paytmchecksum/response';


checksum = Checksum.generate_checksum(respons_dict, MERCHANT_KEY)

#paramarr = {};

#paramarr = respons_dict;

respons_dict['CHECKSUMHASH'] = checksum;

print(respons_dict);

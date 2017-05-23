#!/usr/bin/python

import Checksum
#import requests
import base64
#import json
#import requests
print "Content-type: text/html\n"
MERCHANT_KEY = 'XXXXXXXXX';
#import cgi

#form = cgi.FieldStorage()
respons_dict = {}

respons_dict['MID'] = 'XXXXXXXXX';   #Provided by Paytm
respons_dict['ORDER_ID'] = 'ORDER0000001'; #unique OrderId for every request
respons_dict['CUST_ID'] = 'CUST00001'; # unique customer identifier 
respons_dict['INDUSTRY_TYPE_ID'] = 'XXXXXXXXX'; #Provided by Paytm
respons_dict['CHANNEL_ID'] = 'WAP'; #Provided by Paytm
respons_dict['TXN_AMOUNT'] = '1.00'; #transaction amount
respons_dict['WEBSITE'] = 'XXXXXXXXX'; #Provided by Paytm
respons_dict['EMAIL'] = 'abc@gmail.com'; #customer email id
respons_dict['MOBILE_NO'] = '9999999999'; #customer 10 digit mobile no.
respons_dict['CALLBACK_URL'] = 'https://pguat.paytm.com/paytmchecksum/paytmCallback.jsp';  #Provided by Paytm

checksum = Checksum.generate_checksum(respons_dict, MERCHANT_KEY)

#paramarr = {};

#paramarr = respons_dict;

respons_dict['CHECKSUMHASH'] = checksum;

print respons_dict;

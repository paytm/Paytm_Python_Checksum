#!/usr/bin/python3

import cgitb
cgitb.enable()

import Checksum
#import requests
import base64
#import json
# import requests

MERCHANT_KEY = 'XXXXXXXXXXXXXXXX';

print("Content-type: text/html\n\n");


import os

if os.environ['REQUEST_METHOD'] == 'POST':
	import cgi
	form = cgi.FieldStorage(keep_blank_values = 1)
	response = {}
	for key in form.keys():
		if key == 'CHECKSUMHASH':
			checksum = form[key].value
		else:
			response[key] = form[key].value
		
	print(response, "<br/><br/>")
	verify = Checksum.verify_checksum(response, MERCHANT_KEY, checksum)
	print("Checksum Result: ", verify)

# else:
# 	response = {}
# 	response["ORDERID"] = "ORDER_001"
# 	response["MID"] = "XXXXXXXXXXXXXXXXXXXX"
# 	response["TXNID"] = "20180427111212800110168746100011251"
# 	response["TXNAMOUNT"] = "1.00"
# 	response["PAYMENTMODE"] = "PPI"
# 	response["CURRENCY"] = "INR"
# 	response["TXNDATE"] = "2018-04-27 15:45:05.0"
# 	response["STATUS"] = "TXN_SUCCESS"
# 	response["RESPCODE"] = "01"
# 	response["RESPMSG"] = "Txn Success"
# 	response["GATEWAYNAME"] = "WALLET"
# 	response["BANKTXNID"] = ""
# 	response["BANKNAME"] = "WALLET"
# 	response["CHECKSUMHASH"] = "l0WJTnFq3sfRdMS4TBq67z2zUy1dmlN8U0WT9B3EiA5vym3nm2JTppd6MPE0iITD8yTqYSDJb4MBibx2FGqJ2ZPjjtfVzOugrAz4XLR2ypc="

# 	for key, val in response.items():
# 		if key == 'CHECKSUMHASH':
# 			checksum = val


	# print(response, "<br/><br/>")
	# verify = Checksum.verify_checksum(response, MERCHANT_KEY, checksum)
	# print("Checksum Result: ", verify)


# if checksum is validated Kindly verify the amount and status 
# if transaction is successful 
# kindly call Paytm Transaction Status API and verify the transaction amount and status.
# If everything is fine then mark that transaction as successful into your DB.
#!/usr/bin/python3

import cgitb
cgitb.enable()

import Checksum
#import requests
import base64
#import json
#import requests

print("Content-type: text/html\n\n");

PAYTM_MERCHANT_MID = 'XXXXXXXXXXXXXXXXXXXX'
PAYTM_MERCHANT_KEY = 'XXXXXXXXXXXXXXXX'
PAYTM_MERCHANT_WEBSITE = 'XXXXXXXXXX'
PAYTM_TXN_URL = "https://securegw-stage.paytm.in/theia/processTransaction"

import cgi
form = cgi.FieldStorage()


request = {}
request["MID"] = PAYTM_MERCHANT_MID
request["WEBSITE"] = PAYTM_MERCHANT_WEBSITE
request["ORDER_ID"] = form["ORDER_ID"].value
request["CUST_ID"] = form["CUST_ID"].value
request["INDUSTRY_TYPE_ID"] = form["INDUSTRY_TYPE_ID"].value
request["CHANNEL_ID"] = form["CHANNEL_ID"].value
request["TXN_AMOUNT"] = form["TXN_AMOUNT"].value
request["CALLBACK_URL"] = 'http://localhost/cgi-bin/python_checksum_utility/verifychecksum.cgi'

checksum = Checksum.generate_checksum(request, PAYTM_MERCHANT_KEY)

# print(checksum)

print('''
<head>
<title>Merchant Check Out Page</title>
</head>
<body>
	<center><h1>Please do not refresh this page...</h1></center>
		<form method="post" action="''', PAYTM_TXN_URL, '''" name="f1">
		<table border="1">
			<tbody>
			''')

for key, val in request.items():
	print("<input type='hidden' name='" + key +"' value='" + val +"' >")

print("<input type='hidden' name='CHECKSUMHASH' value='" + checksum +"' >")

print('''
			</tbody>
		</table>
		<script type="text/javascript">
			document.f1.submit();
		</script>
	</form>
</body>
</html>
''')

#!/usr/bin/python

import Checksum
import requests
import base64
import json
import requests

print "Content-type: text/html\n"
MERCHANT_KEY = 'i!jDTJ1vS@aFwaT5';
import cgi

form = cgi.FieldStorage()
respons_dict = {}


for i in form.keys():
 respons_dict[i]=form[i].value
 if i=='CHECKSUMHASH':
    checksum = form[i].value

verify = Checksum.verify_checksum(respons_dict, MERCHANT_KEY, checksum)

if verify:
     respons_dict['IS_CHECKSUM_VALID'] = 'Y'
else: 
     respons_dict['IS_CHECKSUM_VALID'] = 'N'



param_dict = json.dumps(respons_dict, separators=(',', ':'))


print '<head>'
print '<meta http-equiv="Content-Type" content="text/html;charset=ISO-8859-I">'
print '<title>Paytm</title>'
print '<script type="text/javascript">'
print 'function response(){'
#print 'return document.getElementById('response').value;'
print '}'
print '</script>'
print '</head>'
print 'Redirect back to the app<br>'
print '<form name="frm" method="post">'
print '<input type="hidden" id="response" name="responseField" value=\''+param_dict+'\'>'
print '</form>'





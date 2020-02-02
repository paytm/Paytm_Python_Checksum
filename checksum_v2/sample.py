# More Details: https://developer.paytm.com/docs/checksum/#python

import PaytmChecksum
import requests
import json

# Generate Checksum via Hash/Array
# initialize an Hash/Array
paytmParams = {}

paytmParams["MID"] = "YOUR_MID_HERE"
paytmParams["ORDERID"] = "YOUR_ORDER_ID_HERE"

# Generate checksum by parameters we have
# Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
paytmChecksum = PaytmChecksum.generateSignature(paytmParams, "YOUR_KEY_HERE")
verifyChecksum = PaytmChecksum.verifySignature(paytmParams, "YOUR_KEY_HERE",paytmChecksum)

print("generateSignature Returns:" + str(paytmChecksum))
print("verifySignature Returns:" + str(verifyChecksum))

# Generate Checksum via String
# initialize JSON String
body = "{\"mid\":\"YOUR_MID_HERE\",\"orderId\":\"YOUR_ORDER_ID_HERE\"}"

# Generate checksum by parameters we have
# Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
paytmChecksum = PaytmChecksum.generateSignature(body, "YOUR_KEY_HERE")
verifyChecksum = PaytmChecksum.verifySignature(body, "YOUR_KEY_HERE", paytmChecksum)

print("generateSignature Returns:" + str(paytmChecksum))
print("verifySignature Returns:" + str(verifyChecksum))
# More Details: https://developer.paytm.com/docs/checksum/#python

import requests
import json

from paytmchecksum import PaytmChecksum

# Generate Checksum via Hash/Array
# initialize an Hash/Array
paytmParams = {}

paytmParams["MID"] = "YOUR_MID_HERE"
paytmParams["ORDERID"] = "YOUR_ORDER_ID_HERE"

# Generate checksum by parameters we have
# Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
paytmChecksum = PaytmChecksum.generateSignature(paytmParams, "YOUR_MERCHANT_KEY")
verifyChecksum = PaytmChecksum.verifySignature(paytmParams, "YOUR_MERCHANT_KEY",paytmChecksum)

print("generateSignature Returns:" + str(paytmChecksum))
print("verifySignature Returns:" + str(verifyChecksum))

# Generate Checksum via String
# initialize JSON String
body = "{\"mid\":\"YOUR_MID_HERE\",\"orderId\":\"YOUR_ORDER_ID_HERE\"}"

# Generate checksum by parameters we have
# Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
paytmChecksum = PaytmChecksum.generateSignature(body, "YOUR_MERCHANT_KEY")
verifyChecksum = PaytmChecksum.verifySignature(body, "YOUR_MERCHANT_KEY", paytmChecksum)

print("generateSignature Returns:" + str(paytmChecksum))
print("verifySignature Returns:" + str(verifyChecksum))
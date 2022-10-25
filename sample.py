# More Details: https://developer.paytm.com/docs/checksum/#python

from paytmchecksum import PaytmCheckSum

# Generate Checksum via Hash/Array
# initialize an Hash/Array
paytmParams = {}

paytmParams["MID"] = "YOUR_MID_HERE"
paytmParams["ORDERID"] = "YOUR_ORDER_ID_HERE"

# Generate checksum by parameters we have
# Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
paytmChecksum = PaytmCheckSum.generateSignature(
    paytmParams, "YOUR_MERCHANTKEY")
verifyChecksum = PaytmCheckSum.verifySignature(
    paytmParams, "YOUR_MERCHANTKEY", paytmChecksum)

print("generateSignature Returns:" + str(paytmChecksum))
print("verifySignature Returns:" + str(verifyChecksum))

# Generate Checksum via String
# initialize JSON String
body = '{"mid": "YOUR_MID_HERE", "orderId": "YOUR_ORDER_ID_HERE"}'

# Generate checksum by parameters we have
# Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
paytmChecksum = PaytmCheckSum.generateSignature(body, "YOUR_MERCHANTKEY")
verifyChecksum = PaytmCheckSum.verifySignature(
    body, "YOUR_MERCHANTKEY", paytmChecksum)

print("generateSignature Returns:" + str(paytmChecksum))
print("verifySignature Returns:" + str(verifyChecksum))

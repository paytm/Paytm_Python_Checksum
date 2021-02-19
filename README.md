# Checksum Calculation.


```
from paytmchecksum.PaytmChecksum import PaytmChecksum
"""
        Args: data:
            "MID" : "YOUR_MID_HERE",
            "WEBSITE" : "YOUR_WEBSITE_HERE",
            "INDUSTRY_TYPE_ID" : "YOUR_INDUSTRY_TYPE_ID_HERE",
            "CHANNEL_ID" : "YOUR_CHANNEL_ID",
            "ORDER_ID" : "YOUR_ORDER_ID",
            "CUST_ID" : "CUSTOMER_ID",
            "TXN_AMOUNT" : "ORDER_TRANSACTION_AMOUNT",
            "CALLBACK_URL" : "YOUR_CALLBACK_URL",
            "MOBILE_NO" : "CUSTOMER_MOBILE_NUMBER",
            "EMAIL" : "CUSTOMER_EMAIL",   
        """
        required_params = [
            'website', 'industry_type_id', 'channel_id', 'order_id', 'cust_id', 
            'txn_amount', 'callback_url'
        ]
        checksum = PaytmChecksum()
        params_data['CHECKSUMHASH'] = checksum.generate_signature(params_data, self.key)
```
# Checksum Verificaton 

```
checksum = PaytmChecksum()
checksum_data = checksum.verify_signature(data, self.key, data['CHECKSUMHASH'])
```

# Checksum - Python Language
* More Details: **https://developer.paytm.com/docs/checksum/#python**

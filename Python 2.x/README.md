# Prerequisite
 1. Provide the value for MERCHANT_KEY in generatechecksum.cgi and verifychecksum.cgi files. (The value for MERCHANT_KEY will be provided after the onboarding process is completed)

# Installation Steps
 1. The generatechecksum.cgi file uses the Checksum.py file and provides the module to generate the checksum. Copy these files to the location on your server which will be used for the Checksum Generation URL.
 2. The verifychecksum.cgi file uses the Checksum.py file and provides the module to verify the checksum. Copy these files to the location on your server which will be used for the Checksum Verify URL.
 
# For Offline(Wallet Api) Checksum Utility below are the methods:
  1. generate_checksum_by_str : For generating the checksum
  2. verify_checksum_by_str : For verifing the checksum


import base64
import string
import random
import hashlib
import sys
from Crypto.Cipher import AES


class PaytmCheckSum:
    iv = '@@@@&&&&####$$$$'
    BLOCK_SIZE = 16

    @classmethod
    def generateSignature(cls, params, key):
        if not type(params) is dict and not type(params) is str:
            raise Exception("string or dict expected, " +
                            str(type(params)) + " given")
        if type(params) is dict:
            params = cls._getStringByParams(params)
        return cls._generateSignatureByString(params, key)

    @classmethod
    def verifySignature(cls, params, key, checksum):
        if not type(params) is dict and not type(params) is str:
            raise Exception("string or dict expected, " +
                            str(type(params)) + " given")
        if "CHECKSUMHASH" in params:
            del params["CHECKSUMHASH"]

        if type(params) is dict:
            params = cls._getStringByParams(params)
        return cls._verifySignatureByString(params, key, checksum)

    @classmethod
    def encrypt(cls, input, key):
        input = cls.__pad__(input)
        c = AES.new(key.encode("utf8"), AES.MODE_CBC, cls.iv.encode("utf8"))
        input = c.encrypt(input)
        input = base64.b64encode(input)
        return input.decode("UTF-8")

    @classmethod
    def decrypt(cls, encrypted, key):
        encrypted = base64.b64decode(encrypted)
        c = AES.new(key.encode("utf8"), AES.MODE_CBC, cls.iv.encode("utf8"))
        param = c.decrypt(encrypted)
        if type(param) == bytes:
            param = param.decode()
        return cls.__unpad__(param)

    @classmethod
    def _generateSignatureByString(cls, params, key):
        salt = cls._generateRandomString(4)
        return cls._calculateChecksum(params, key, salt)

    @classmethod
    def _getStringByParams(cls, params):
        params_string = []
        for key in sorted(params.keys()):
            value = params[key] if params[key] is not None and params[key].lower(
            ) != "null" else ""
            params_string.append(str(value))
        return '|'.join(params_string)

    @classmethod
    def _verifySignatureByString(cls, params, key, checksum):
        paytm_hash = cls.decrypt(checksum, key)
        salt = paytm_hash[-4:]
        return paytm_hash == cls._calculateHash(params, salt)

    @classmethod
    def _generateRandomString(cls, length):
        chars = ''.join(random.SystemRandom().choice(string.ascii_uppercase +
                        string.digits + string.ascii_lowercase) for _ in range(length))
        return chars

    @classmethod
    def _calculateChecksum(cls, params, key, salt):
        hashString = cls._calculateHash(params, salt)
        return cls.encrypt(hashString, key)

    @classmethod
    def _calculateHash(cls, params, salt):
        finalString = '%s|%s' % (params, salt)
        hasher = hashlib.sha256(finalString.encode())
        hashString = hasher.hexdigest() + salt
        return hashString

    @classmethod
    def __pad__(cls, s):
        if (sys.version_info > (3, 0)):
            return bytes(s + (cls.BLOCK_SIZE - len(s) %
                              cls.BLOCK_SIZE) * chr(cls.BLOCK_SIZE - len(s) % cls.BLOCK_SIZE), 'utf-8')
        else:
            return s + (BLOCK_SIZE - len(s) %
                        BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

    @classmethod
    def __unpad__(cls, s):
        return s[0:-ord(s[-1])]

# -*- coding: utf-8 -*-
"""
TigoMoney Client Web Service

Date: 05/06/2017
Author: Jorge Moreira.
Linkux IT

"""

import base64
from Crypto.Cipher import DES3
from suds.client import Client
from urlparse import parse_qsl


class TripleDes:
    def __init__(self, key):
        self.key = key

    def encrypt(self, message):
        des3 = DES3.new(self.key, DES3.MODE_ECB)

        # Padding zero
        padding = 8 - len(message) % 8
        message = message.ljust(len(message) + padding, '\0')

        return base64.b64encode(des3.encrypt(message))

    def decrypt(self, message):
        des3 = DES3.new(self.key, DES3.MODE_ECB)
        response = des3.decrypt(base64.b64decode(message))

        # Unpadding zero
        cleanedData = response.rstrip('\0')
        return cleanedData


class TigoMoneyApi:

    def __init__(self, soapUrl, identificationKey, encryptionKey):
        self.soapUrl = soapUrl
        self.identificationKey = identificationKey
        self.encryptionKey = encryptionKey
        self.soapClient = Client(soapUrl)

    def call(self, methodName, *args, **kwargs):
        if args:
            params = ''.join(args)
        elif kwargs:
            params = ';'.join('%s=%s' % (key, value) for key, value in kwargs.iteritems())
        else:
            raise ValueError('Illegal argument exception.')

        __call = getattr(self.soapClient.service, methodName)

        c3des = TripleDes(self.encryptionKey)
        encryptedParams = c3des.encrypt(params)

        response = __call(key=self.identificationKey, parametros=encryptedParams)

        qs = c3des.decrypt(response)

        return dict(parse_qsl(qs))

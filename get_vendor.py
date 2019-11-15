#!/usr/bin/env python3
from maclookup import ApiClient

def vendor(oui):
    client = ApiClient('Your API key') #from https://macaddress.io/
    vend = client.get_vendor(oui)
    vend = str(vend.decode('utf-8'))
    return vend

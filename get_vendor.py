#!/usr/bin/env python3

# Requires maclookup to be installed.
# to do that, run: sudo pip3 install maclookup
# After that sign up at https://macaddress.io/ to get your free API key.

from maclookup import ApiClient

def vendor(oui):
    client = ApiClient('Your API key') 
    vend = client.get_vendor(oui)
    vend = str(vend.decode('utf-8'))
    return vend

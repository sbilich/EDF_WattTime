import os, getpass, base64, json, urllib, login_util, query_util
from Tkinter import *
from urllib2 import Request, urlopen, URLError


def main():
    WATT_TOK = "WATT_TOK"
    login_util.login(WATT_TOK)

    auth_headers = {
        'Authorization': 'Bearer ' + os.environ['WATT_TOK'],
    }

    params = {
        'ba': 'CAISO_ZP26',
        'starttime': '2018-05-01T01:00:00Z',
        'endtime': '2018-05-01T01:10:00Z',
    }
    params_en = urllib.urlencode(params)

    request = Request('https://api2.watttime.org/v2/data/' + "?" + params_en, headers=auth_headers)

    response = urlopen(request)
    print response.read()

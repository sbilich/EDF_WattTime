import os, getpass, base64, json, urllib
from urllib2 import Request, urlopen, URLError

# prompt user for username and password
# store WattTime API token in environment variable
def login(tok, user, pwd):
    usr_pwd = user + ":" + pwd
    encrypted = base64.b64encode(usr_pwd.encode())

    headers = {
        'Authorization': 'Basic ' + encrypted
    }
    request = Request('https://api2.watttime.org/v2/login/?username=username&password=password', headers=headers)

    try:
        response = urlopen(request)
        code = response.getcode()

        if code == 200: # set api token
            data = response.read()
            JSON_object = json.loads(data.decode('utf-8'))
            os.environ[tok] = JSON_object['token']

        return response
    except URLError as e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code

    return None

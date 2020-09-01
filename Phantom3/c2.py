import requests

while(True):
    x = requests.Session()
    y = x.get('http://webchallenge.cybsec.in:8000')
    result = y.text
    ans = result[139:146].rstrip()
    print(ans)
    myobj = {'captcha': ans, 'key': 200}
    gg = x.post('http://webchallenge.cybsec.in:8000' , data = myobj,stream=True)
    print(gg.text)
    if('pCTF' in gg.text):
        break
    x.close()

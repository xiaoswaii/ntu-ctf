import requests
test = 1100
for i in range(1000):
    test = test + 1
    r=requests.get("http://13.53.91.128:50000/path/"+str(test),allow_redirects=False)
    print('level now:',test)
    print(r.status_code)
    print(r.text)
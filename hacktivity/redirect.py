import requests
session = requests.Session()
session.max_redirects = 200
r = session.get("http://jh2i.com:50011/site/flag.php")
for resp in r.history:
    print(resp.status_code, resp.url, resp.text)
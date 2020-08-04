from pwn import *
answer = [99126]
response = "begin"
while('flag{' not in response):
    r = remote('jh2i.com',50012)
    for i in range(len(answer)):
        r.recvuntil('> ')
        r.send(str(answer[i]))
    res = r.recv()
    print(res)
    r.send(str(1))
    response = str(r.recvall())
    print(response)
    ans = response[-11:-6]
    answer.append(ans)
    print(ans)
    print(answer)
    r.close()
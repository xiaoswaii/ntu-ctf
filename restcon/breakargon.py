from argon2 import PasswordHasher

ph = PasswordHasher()
hast = '$argon2id$v=19$m=64,t=16,p=8$Q3liZXJLbmlnaHQwMA$3ZodOqWeWZ0a41c3HQrLY4nawron7LNWajWIyztZkds'


fp = open('rockyou.txt', "r")

## 用 while 逐行讀取檔案內容，直至檔案結尾
while (True):
    line = fp.readline().strip()
    try:
        print(ph.verify(hast,line))
        print(word,"is the plaintext")
        break
    except:
        print("{} [-] FALSE".format(line))
       

from argon2 import PasswordHasher
import itertools
import os



ph = PasswordHasher()
hast = '$argon2id$v=19$m=16,t=5,p=1$Q3liZXJLbmlnaHQwMA$OsYit6bu17WDed6VMKq/Rw'
numbers = '0123456789'
y = ''
for c in itertools.product(numbers, repeat=5):
    pin = y+''.join(c)
    pin = '7'+ pin + '1'
    try:
        print(ph.verify(hast,pin))
        print(pin,"is the plaintext")
        break
    except:
        print("{} [-] FALSE".format(pin))
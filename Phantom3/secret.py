def kraitrot(input, d):
    Lf = input[0:d]
    Ls = input[d:]
    return Ls + Lf


def cobraverse(s):
    g = ''
    g += s[1::2]
    g += s[0::2]
    return g


def vipershift(s):
    g = ''
    for i in range(len(s)):
        a = hex(ord(s[i]) + 20)[2:]
        g += a

    return g


# s3rc3t = input("Enter the secret to get access to python's cave : ")
# print(vipershift(s3rc3t))
# if len(s3rc3t) < 28:
#     print('Add little more weight :::\n')
# else:
#     if vipershift(cobraverse(kraitrot(s3rc3t, 15))) == '867387738d7c8284688f454745737c4488894784884491575a807a738787':
#         print("\nWhy does Python live on land?\nBecause it's above C-level . XD!! \nCongrats for the flag anyways")
#     else:
#         print('Maybe a python bit you , better luck next time :((')

cipher = '867387738d7c8284688f454745737c4488894784884491575a807a738787'
def unshift(cipher):
    g = ''
    txt = ''
    for i in range(len(cipher)):
        if(i%2 == 0):
            g+=cipher[i]
        else:
            g+=cipher[i]
            x = int(g, 16)
            x = x - 20
            x = hex(x)
            txt += x[2:]
            g=''
    return ''.join([chr(int(''.join(c), 16)) for c in zip(txt[0::2],txt[1::2])])

def raverse(s):
    g = ''
    a = int(len(s)/2)
    for i in range(a):
        g += s[i+a]
        g += s[i]
    return g


print(len(unshift(cipher)))
print(raverse(unshift(cipher)))
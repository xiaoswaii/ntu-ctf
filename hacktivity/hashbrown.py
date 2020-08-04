import hashlib
import string
tocompare = '123dbc'
for i in string.printable:
    for j in string.printable:
        for k in string.printable:
            for z in string.printable:
                data = i+j+k+z
                sha1 = hashlib.md5(data.encode('utf-8')).hexdigest()
                print(i+j+k+z)
                if(sha1[:5] == tocompare):
                    print(sha1)
                    print(i)
                    break
    
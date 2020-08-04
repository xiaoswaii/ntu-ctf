import hashlib
import string
tocompare = 'b9cbede7a7bc4eee4c4a9cc6469fbaff2ff1f41d82d3fc7ed4bebbfecd569616'
for i in string.printable:
    for j in string.printable:
        for k in string.printable:
            for z in string.printable:
                data = i+j+k+z+ 'MYwiYNIZpNMwRDLE'
                sha1 = hashlib.sha256(data.encode('utf-8')).hexdigest()
                print(i+j+k+z+'MYwiYNIZpNMwRDLE')
                if(sha1 == tocompare):
                    print(sha1)
                    print(data)
                    print('sucess')
                    break
    
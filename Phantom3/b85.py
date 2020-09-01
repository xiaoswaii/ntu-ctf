import base64
f = open("is_it_base85", "r")
a = f.readline()
# print(a)
b1 = a.encode("UTF-8")
print(b1)
d = base64.b85decode(b1)
print(d)
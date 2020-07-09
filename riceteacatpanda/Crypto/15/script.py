encrpyt = "tovm{v4T3Ehq_f1oK_3J1e_i4O4}"
final = "rtcp{v4T3Ehq_f1oK_3J1e_i4O4}"
for i in range(4):
    print('before: ',ord(encrpyt[i]),end=" ")
    print('diffirent: ',ord(encrpyt[i])-ord(final[i]))
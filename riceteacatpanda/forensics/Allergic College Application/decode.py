import io
with io.open('Common_App_Essay.txt', 'rb') as f:
    text = f.read()
for each_unicode_character in text.decode('big5','ignore'):
    print (each_unicode_character)
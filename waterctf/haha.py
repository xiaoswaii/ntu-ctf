import pickle
import base64
b = {'money': 5000, 'history': [], 'anti_tamper_hmac': 'aa1ba4de55048cf20e0a7a63b7f8eb62'}
a = pickle.dumps(b)
print (a)
print (pickle.loads(a))
c = base64.b64encode(a)
print (c)
fuck = 'gAN9cQAoWAUAAABtb25leXEBTfQBWAcAAABoaXN0b3J5cQJdcQNYEAAAAGFudGlfdGFtcGVyX2htYWNxBFggAAAAYWExYmE0ZGU1NTA0OGNmMjBlMGE3YTYzYjdmOGViNjJxBXUu'
d = base64.b64decode(fuck)
print(d)
print(pickle.loads(d))
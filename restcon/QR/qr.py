import qrtools
qr = qrtools.QR()
for i in range(5000):
	qr.decode(i+".png")
	print(qr.data)

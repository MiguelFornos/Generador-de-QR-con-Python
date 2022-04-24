import qrcode

img=qrcode.make("Hola, mundo")

f= open("QR.png","wb")
img.save(f)
f.close()

import pyqrcode

qr_image = pyqrcode.MakeQRImage("http://code.google.com/p/pyqrcode/")
qr_image.show()

import pyqrcode
from pyqrcode import QRCode
s ="hai hello"
url = pyqrcode.create(s)
url.svg("test_qrcode.svg",scale = 8)

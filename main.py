import qrcode
import random

file_name = 'test.png'
try:
    r = random.random()  # create a random number
    qr_code = qrcode.make(r)  # generate QR Code
    qr_code.save(file_name)  # finally save the QR Code image
    print('done')
except:
    print('error')

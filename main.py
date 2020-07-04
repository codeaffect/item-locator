import qrcode
import random
import cv2

file_name = 'test.png'
try:
    r = random.random()  # create a random number
    print(f'random value:- {r}')
    qr_code = qrcode.make(r)  # generate QR Code
    qr_code.save(file_name)  # finally save the QR Code image
    print('qr code generated!')
except:
    print('error')

print('reading....')
try:
    img = cv2.imread(file_name)

    # initialize the cv2 QRCode detector
    qr_detection = cv2.QRCodeDetector()

    # detect and decode
    data, bbox, straight_qrcode = qr_detection.detectAndDecode(img)

    # if there is a QR code
    if bbox is not None:
        print(f"QRCode data:- {data}")

    # display the result
    # cv2.imshow("img", img)
except:
    print('error reading..')

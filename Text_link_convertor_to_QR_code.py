# install all the libaraies
# create a function that collects a text and converts ot to a code
# save the qr code as an image
# run the function 

'''import qrcode
import qrcode.constants

def genrate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black",back_color="white")
    img.save("qrcode.png")


genrate_qrcode("https://www.facebook.com/fer.thosi")'''


import qrcode
import qrcode.constants

def qrcode_generate(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size =10,
        border =4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color ="white")
    img.save("qrcode.png")

url = input("Enter your url: ")
qrcode_generate(url)
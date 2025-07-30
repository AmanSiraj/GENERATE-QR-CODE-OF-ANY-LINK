import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data('https://www.linkedin.com/in/aman-siraj-sayyad/')
qr.make(fit=True)

img = qr.make_image(fill_color='blue', back_color='white')
img.save('linkedin_web.png')

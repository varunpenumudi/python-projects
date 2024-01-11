import segno

# Qr properties
foreground_color = "#000000" # default is black color
background_color = "#ffffff" # default is white color
scaling_factor = 8           #To control size of QR
border = 1                   # border/whitespace around QR, must be an integer
title = "qrcode"             #Title for your qr code

# text for which qr code is generated
text = input("Enter the text to generate Qr: ")

# generate qr code
qrcode = segno.make_qr(text)


# create image for generated qr code
qrcode.save(
    f"{title}.png", 
    scale = scaling_factor , 
    border= border, 
    dark  = foreground_color,
    light = background_color,
)



import qrcode

# Data to be encoded
data = "https://www.example.com"

# Create QRcode instance
qr = qrcode.QRCode(
    version = 1, # Size of the Qrcode
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4,

)
# Add data to qrcode
qr.add_data(data)
qr.make(fit = True)

# Create an Image
img = qr.make_image(fill_color = "White", back_color = "Black")

# Save an Image
img.save("Qrcode.png")

print("QRcode Successfully Created")



























































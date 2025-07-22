pip install qrcode

import qrcode

# Step 1: Define the URL
url = input("enter your url")

# Step 2: Generate the QR code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

# Step 3: Display QR code in terminal (as ASCII)
print("QR Code in Terminal:\n")
qr.print_ascii(invert=True)  # invert=True for better visibility in light terminals

# Step 4: Save the QR code as an image
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_code.png")

print("\nQR code saved as 'qr_code.png'")

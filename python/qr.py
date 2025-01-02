import qrcode as qr
from PIL import Image

# Define the link and QR code name
link = ""
qr_name = ""

# Create the QRCode object
Qr = qr.QRCode(
    version=1, 
    error_correction=qr.ERROR_CORRECT_H, 
    box_size=10, 
    border=4
)
Qr.add_data(link)
Qr.make(fit=True)

# Generate QR code with custom colors
img = Qr.make_image(fill_color="blue", back_color="white")

# Save the QR code image
img.save(qr_name)

print(f"QR code saved as {qr_name}")

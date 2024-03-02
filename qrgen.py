import pandas as pd
import qrcode

x = pd.read_csv('/home/python/project/QrCodeGenerator/Book.csv', header = 0).values
x = pd.DataFrame(x)
l = []
for i in range(len(x[0])):
    data = (str(x[0][i]))
    l.append(data)
    try:
        name = data.split('/')[-2]
        print(name)

    except:
       name = data.split('/')[-1]
       print(name)

    
    # Create a QRCode object
    qr = qrcode.QRCode(
        version=1,  # Adjust version for size and data capacity
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Error correction level
    )

    # Add data and make the QR code
    qr.add_data(data)
    qr.make(fit=True)  # Auto-fit code to version

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(f"/home/python/project/QrCodeGenerator/images/{name}.png")
    print(data)

    
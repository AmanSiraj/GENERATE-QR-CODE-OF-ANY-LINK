# 🔳 QR Code Generator

This is a simple Python project that generates a customized QR code linking to a specific URL. It uses the `qrcode` and `Pillow` libraries to create colored QR codes and save them as image files.

---

## 📌 Features

- Generates a QR code for any given URL or text
- Custom fill and background color
- High error correction (up to 30%)
- Outputs a PNG image

---
<img width="490" height="490" alt="linkedin_web" src="https://github.com/user-attachments/assets/b7f2424c-8e31-435e-9be6-cc797e92f0a8" />

🚀 How to Run This Project Locally
Follow these steps to run the QR Code Generator on your machine:

1️⃣ Clone the Repository

git clone https://github.com/your-username/qr-code-generator.git
cd qr-code-generator
Replace your-username with your actual GitHub username.

2️⃣ Install Required Libraries
Make sure you have Python 3 installed.

Then, install the required packages using pip:

pip install qrcode[pil]
3️⃣ Run the Python Script
In the project folder, run the script:

python qr_generator.py
This will generate a QR code image and save it as linkedin_web.png in the same folder.

4️⃣ Customize (Optional)
Change the URL in the script:

python
qr.add_data('https://your-link.com')
Modify QR code colors:

python
img = qr.make_image(fill_color='your_color', back_color='your_color')
✅ Output
The script will create a file named:

linkedin_web.png
Scan it with your phone to open the link you encoded!

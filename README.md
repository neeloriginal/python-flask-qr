# python-flask-qr
Below is **plain copy-paste text** (no formatting tricks).
You can paste this directly into **README.md**.

---

Flask QR Code Generator

A simple and lightweight Flask web application that generates QR codes from user-provided text or URLs. The QR code is generated dynamically and displayed instantly on the web page.

---

Features

* Generate QR codes from text or URLs
* Fast and lightweight Flask backend
* QR code generated in memory (no file storage)
* Clean UI using Bootstrap
* Beginner-friendly project

---

Technologies Used

* Python
* Flask
* qrcode library
* Bootstrap 5
* HTML (Jinja2)

---

Project Structure

flask-qr/
│
├── app.py
├── templates/
│   └── index.html
├── .env/
└── README.md

---

Setup & Installation (Windows)

Step 1: Create Virtual Environment
python -m venv .env

Step 2: Activate Virtual Environment
..env\Scripts\Activate.ps1

Step 3: Install Dependencies
pip install flask
pip install qrcode
pip install pillow
---

Run the Application

python .\app.py

Open your browser and visit:
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

How It Works

1. User enters text in the form
2. Flask receives the input via POST request
3. QR code is generated using the qrcode library
4. QR image is converted to Base64
5. Image is rendered directly in the browser

---

Future Enhancements

* Download QR code as PNG
* Customize QR size and color
* Convert project into REST API
* Add Docker support

---

License
This project is open-source and available under the MIT License.

---

If you want a **shorter version** (only description + run steps) or a **GitHub one-line description**, tell me and I’ll rewrite it 👍

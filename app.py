from flask import Flask, render_template, request, send_file
import qrcode
import io
import base64

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    qr_image = None

    if request.method == 'POST':
        text = request.form['text']
         # Create QR image in memory
        img = qrcode.make(text)
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        # Convert to base64
        qr_image = base64.b64encode(buffer.getvalue()).decode()

    return render_template('index.html', qr_image=qr_image)

if __name__ == "__main__":
    app.run(debug=True)
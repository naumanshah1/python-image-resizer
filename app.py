from flask import Flask, request, render_template, send_file
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def resize():
    if request.method == 'POST':
        file = request.files['image']
        width = int(request.form['width'])
        height = int(request.form['height'])

        img = Image.open(file)
        resized = img.resize((width, height))

        img_io = BytesIO()
        resized.save(img_io, format='PNG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='resized.png')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

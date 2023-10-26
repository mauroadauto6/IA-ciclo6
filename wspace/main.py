import tempfile
import os
from flask import Flask, request, redirect, send_file, render_template
from skimage import io
import base64
import glob
import numpy as np

app = Flask(__name__)

@app.route("/")
def main():
    return(render_template('index.html'))


@app.route('/upload', methods=['POST'])
def upload():
    try:
        # check if the post request has the file part
        img_data = request.form.get('myImage').replace("data:image/png;base64,","")
        aleatorio = request.form.get('numero')
        print(aleatorio)
        print(aleatorio.split(' ')[0])
        with tempfile.NamedTemporaryFile(delete = False, mode = "w+b", suffix='.png', dir=os.path.join(shapes_dir, str(aleatorio.split(' ')[0]))) as fh:
            fh.write(base64.b64decode(img_data))
        #file = request.files['myImage']
        print("Image uploaded")
    except Exception as err:
        print("Error occurred")
        print(err)

    return redirect("/", code=302)


@app.route('/prepare', methods=['GET'])
def prepare_dataset():
    images = []
    s = ['triangulo', 'cuadrado', 'circulo', 'rombo']
    digits = []
    for digit in s:
        filelist = glob.glob('shapes/{}/*.png'.format(digit))
        images_read = io.concatenate_images(io.imread_collection(filelist))
        digits_read = np.array([digit] * images_read.shape[0])
        images.append(images_read)
        digits.append(digits_read)
    images = np.vstack(images)
    digits = np.concatenate(digits)
    np.save('X.npy', images)
    np.save('y.npy', digits)
    return "OK!"


@app.route('/X.npy', methods=['GET'])
def download_X():
    return send_file('X.npy')


@app.route('/y.npy', methods=['GET'])
def download_y():
    return send_file('y.npy')

if __name__ == "__main__":
    shapes = ['triangulo', 'cuadrado', 'circulo', 'rombo']
    for s in shapes:
        shapes_dir = 'shapes/'
        if not os.path.exists(shapes_dir):
            os.mkdir(shapes_dir)
        if not os.path.exists(os.path.join(shapes_dir, str(s))):
            os.mkdir(os.path.join(shapes_dir, str(s)))
    app.run()
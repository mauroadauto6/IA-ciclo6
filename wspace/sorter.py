import os
import tempfile
from flask import Flask, request, redirect, render_template, url_for
from skimage import io
import base64
from skimage.transform import resize
import numpy as np
import tensorflow as tf

model = tf.keras.models.load_model('D:/documents/UPC/Ciclo VI/Inteligencia Artificial/PC2/wspace/figurIA.h5')
app = Flask(__name__, template_folder="templates/")

@app.route("/")
def main():
    return render_template('drawing.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        img_data = request.form.get('myImage').replace("data:image/png;base64,","")
        with tempfile.NamedTemporaryFile(delete=False, mode="w+b", suffix='.png', dir=str('prediccion')) as fh:
            fh.write(base64.b64decode(img_data))
            tmp_file_path = fh.name
        imagen = io.imread(tmp_file_path)
        print(imagen.ndim, imagen.shape)
        size = (28, 28)
        image = imagen / 255.0
        im = resize(image, size)
        im = im.reshape(1, *im.shape)
        im = im[:,:,:,:3]
        print(im.ndim, im.shape)
        salida = model.predict(im)[0]
        os.remove(tmp_file_path)
        nums = salida*100
        numeros_formateados = [f'{numero:.2f}' for numero in nums]
        cadena_formateada = ', '.join(numeros_formateados)
        return redirect(url_for('show_predictions', nums=cadena_formateada, img_data=img_data))
    except:
        print("Error occurred")

    return redirect("/", code=302)

@app.route('/predicciones')
def show_predictions():
    nums = request.args.get('nums')
    img_data = request.args.get('img_data')
    componentes = nums.split(', ')
    nums = [float(componente) for componente in componentes]
    shapes = ['triangulo verde', 'triangulo azul', 'triangulo amarillo','triangulo rojo',
                'cuadrado verde', 'cuadrado azul', 'cuadrado amarillo', 'cuadrado rojo',
                'circulo verde', 'circulo azul', 'circulo amarillo', 'circulo rojo',
                'rombo verde', 'rombo azul', 'rombo amarillo', 'rombo rojo']
    if img_data is not None:
        return render_template('sorter.html', nums=nums, shapes=shapes, img_data=img_data)
    else:
        return redirect("/", code=302)


if __name__ == "__main__":
    app.run()
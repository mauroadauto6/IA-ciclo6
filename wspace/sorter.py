import os
import tempfile
from flask import Flask, request, redirect, render_template, url_for
from skimage import io
import base64
from skimage.transform import resize
import numpy as np
import tensorflow as tf
from gtts import gTTS

# carga del modelo entrenado con 0.89 de precisión
# https://colab.research.google.com/drive/1pgyV8zmYZh1LzwoJMDwQN4zNQCNLw9-A?usp=sharing
model = tf.keras.models.load_model('D:/documents/UPC/Ciclo VI/Inteligencia Artificial/PC2/wspace/figurIA.h5')
app = Flask(__name__, template_folder="templates/")

@app.route("/")
def main():
    return render_template('drawing.html')

@app.route('/clasificar', methods=['POST'])
def clasif():
    try:
        img_data = request.form.get('myImage').replace("data:image/png;base64,","")
        with tempfile.NamedTemporaryFile(delete=False, mode="w+b", suffix='.png', dir=str('clasificacion')) as fh:
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
        p_nums = [f'{n:.2f}' for n in nums]
        num_label = ', '.join(p_nums)
        return redirect(url_for('sort_shapes', nums=num_label, img_data=img_data))
    except:
        print("Error occurred")

    return redirect("/", code=302)

@app.route('/clasificaciones')
def sort_shapes():
    nums = request.args.get('nums')
    img_data = request.args.get('img_data')
    proporcion = nums.split(', ')
    nums = [float(p) for p in proporcion]
    print(nums)
    shapes = ['triangulo verde', 'triangulo azul', 'triangulo amarillo','triangulo rojo',
                'cuadrado verde', 'cuadrado azul', 'cuadrado amarillo', 'cuadrado rojo',
                'circulo verde', 'circulo azul', 'circulo amarillo', 'circulo rojo',
                'rombo verde', 'rombo azul', 'rombo amarillo', 'rombo rojo']
    
    max_num = nums.index(max(nums))
    max_shape = shapes[max_num] # obtenemos el label del indice del número más alto
    print(max_shape, type(max_shape))
    
    shape_sides, sh_only = calculateSides(max_shape)
    generateAudio(max_shape)
    
    if img_data is not None:
        return render_template('sorter.html', nums=nums, max_shape=max_shape, max_shape_nospace=max_shape.replace(' ', '_'), shape_sides=shape_sides, shape=sh_only, img_data=img_data)
    else:
        return redirect("/", code=302)

@app.route('/clasificaciones')
def calculateSides(max_shape):
    sides = {'triangulo': 3, 'cuadrado': 4, 'circulo': 0, 'rombo': 4}
    
    for sh, s in sides.items():
        if (sh == max_shape.split()[0]):
            shape_sides = s # almacenamos el numero de lados de la figura clasificada
            sh_only = sh # almacenamos la figura clasificada
            break
    return shape_sides, sh_only

@app.route('/clasificaciones')
def generateAudio(max_shape):
    tts = gTTS(text=max_shape, lang='es')
    audio_folder = os.path.join('wspace', 'static', 'audio')
    if not os.path.exists(audio_folder):
        os.makedirs(audio_folder)
    audio_file = os.path.join(audio_folder, max_shape.replace(' ', '_') + '.mp3')
    if not os.path.exists(audio_file):
        tts.save(audio_file)

if __name__ == "__main__":
    app.run()
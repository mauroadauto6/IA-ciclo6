from skimage import io
import os
from PIL import Image
import os
import tempfile
from flask import Flask, request, redirect, render_template, url_for
from skimage import io
import base64
from skimage.transform import resize
import numpy as np
import tensorflow as tf
from gtts import gTTS

shapes = ['triangulo verde', 'triangulo azul', 'triangulo amarillo','triangulo rojo',
                'cuadrado verde', 'cuadrado azul', 'cuadrado amarillo', 'cuadrado rojo',
                'circulo verde', 'circulo azul', 'circulo amarillo', 'circulo rojo',
                'rombo verde', 'rombo azul', 'rombo amarillo', 'rombo rojo']

"""suma = 0
total_size = 0

for s in shapes_color:
    shapes_dir = "shapes/"
    complete_path_to_shape = os.path.join(shapes_dir, str(s))
    for f in os.listdir(complete_path_to_shape):
        if f.endswith('.png'):
            imagen = io.imread(os.path.join(complete_path_to_shape, f))
            img = Image.open(os.path.join(complete_path_to_shape, f))
            size = os.path.getsize(os.path.join(complete_path_to_shape, f))
            print(os.path.join(complete_path_to_shape, f), imagen.shape, img.mode, size / 1000, "KB")
        suma += 1
        total_size += size / 1000000

print("{} - {:.2f}MB".format(suma, total_size))"""



"""shapes_color = ['triangulo verde', 'triangulo azul', 'triangulo amarillo','triangulo rojo',
                'cuadrado verde', 'cuadrado azul', 'cuadrado amarillo', 'cuadrado rojo',
                'circulo verde', 'circulo azul', 'circulo amarillo', 'circulo rojo',
                'rombo verde', 'rombo azul', 'rombo amarillo', 'rombo rojo']

shapes_color_dic = {'triangulo verde': 0, 'triangulo azul': 1, 'triangulo amarillo': 2,'triangulo rojo': 3,
                'cuadrado verde': 4, 'cuadrado azul': 5, 'cuadrado amarillo': 6, 'cuadrado rojo': 7,
                'circulo verde': 8, 'circulo azul': 9, 'circulo amarillo': 10, 'circulo rojo': 11,
                'rombo verde': 12, 'rombo azul': 13, 'rombo amarillo': 14, 'rombo rojo': 15}

shapes_color_dic_inv = {0: 'triangulo verde', 1: 'triangulo azul', 2: 'triangulo amarillo', 3: 'triangulo rojo',
                4: 'cuadrado verde', 5: 'cuadrado azul', 6: 'cuadrado amarillo', 7: 'cuadrado rojo',
                8: 'circulo verde', 9: 'circulo azul', 10: 'circulo amarillo', 11: 'circulo rojo',
                12: 'rombo verde', 13: 'rombo azul', 14: 'rombo amarillo', 15: 'rombo rojo'}"""
"""nums = [2, 1, 1, 1,
       1, 1, 1, 1,
       1, 1, 1, 1,
       1, 1, 1, 1]
sh =[]
for i in range(len(shapes)):
    sh.append(shapes[i].split()[0])

max_num = nums.index(max(nums))
max_shape = shapes[max_num] 

print(sh)
print(max_shape)

sides = {'triangulo': 3, 'cuadrado':4, 'circulo': 0, 'rombo': 4}
    
for sh, s in sides.items():
    if (sh == max_shape.split()[0]):
        shape_sides = s
        break
        
print(shape_sides)"""
"""max_shape = 'triangulo rojo'
tts = gTTS(text=max_shape, lang='es')
audio_folder = os.path.join('wspace', 'static', 'audio')
if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)
audio_file = os.path.join(audio_folder, max_shape.replace(' ', '_') + '.mp3')
tts.save(audio_file)
print(audio_file.split('\\')[3])"""
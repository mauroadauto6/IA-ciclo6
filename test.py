from skimage import io
import os
from PIL import Image

shapes_color = ['triangulo verde', 'triangulo azul', 'triangulo amarillo','triangulo rojo',
                'cuadrado verde', 'cuadrado azul', 'cuadrado amarillo', 'cuadrado rojo',
                'circulo verde', 'circulo azul', 'circulo amarillo', 'circulo rojo',
                'rombo verde', 'rombo azul', 'rombo amarillo', 'rombo rojo']

suma = 0

for s in shapes_color:
    shapes_dir = "shapes/"
    complete_path_to_shape = os.path.join(shapes_dir, str(s))
    for f in os.listdir(complete_path_to_shape):
        if f.endswith('.png'):
            imagen = io.imread(os.path.join(complete_path_to_shape, f))
            img = Image.open(os.path.join(complete_path_to_shape, f))
            #print(os.path.join(complete_path_to_shape, f), imagen.shape, img.mode)
        suma += 1

print(suma)



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


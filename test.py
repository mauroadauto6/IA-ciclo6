from skimage import io
import os
from PIL import Image

shapes = ['triangulo', 'cuadrado', 'circulo', 'rombo']

suma = 0

for s in shapes:
    shapes_dir = "shapes/"
    complete_path_to_shape = os.path.join(shapes_dir, str(s))
    for f in os.listdir(complete_path_to_shape):
        if f.endswith('.png'):
            imagen = io.imread(os.path.join(complete_path_to_shape, f))
            img = Image.open(os.path.join(complete_path_to_shape, f))
            print(os.path.join(complete_path_to_shape, f), imagen.shape, img.mode)
        suma += 1

print(suma)
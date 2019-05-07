"""
Nome: JPGtoASCII.py
Autor: Felipe Kenzo Shiraishi - Grupo aMuDi
Data: 07/05/2019
"""

from PIL import Image

REDUX = 4

foto_path = "kenzo.jpg"

im = Image.open(foto_path)

width, height = im.size

pixels = im.load()

f = open("ASCII_PHOTO.txt", "w")

ASCII_map = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def average_matrix(pixels):
    matrix = []
    for i in range(height):
        matrix.append([])
        for j in range(width):
            matrix[i].append((pixels[j, i][0] + pixels[j, i][1] + pixels[j, i][2])/3)
    return matrix

def map_to_ASCII(value):
    MAX_VALUE = 256
    pix = value/MAX_VALUE
    chars = len(ASCII_map)
    intervalo = 1/chars
    traduzido = int(pix/intervalo)
    return ASCII_map[traduzido]

def convert_JPG_to_ASCII(pixels):
    map_ASCII = average_matrix(pixels)
    map_ASCII = shrink_map(map_ASCII, REDUX)
    for i in range(len(map_ASCII)):
        for j in range(len(map_ASCII[i])):
            f.write(map_to_ASCII(map_ASCII[i][j]))
            f.write(map_to_ASCII(map_ASCII[i][j]))
            #f.write(map_to_ASCII(map_ASCII[i][j]))
        f.write('\n')

def shrink_map(pixels, redux):
    map_shrink = []
    for i in range(int(height/redux)):
        map_shrink.append([])
        for j in range(int(width/redux)):
            value = 0
            for k in range(redux):
                for l in range (redux):
                    value += pixels[(i * redux) + k][(j * redux) + l]
            value /= redux**2
            map_shrink[i].append(value)
    return map_shrink

convert_JPG_to_ASCII(pixels)

f.close()
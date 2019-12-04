opc = 0
import numpy as np
import matplotlib.pyplot as plt
import cv2
import base64
from PIL import Image
from io import BytesIO
import argparse
import sys

def letter2ASCII(msg):
     for i in msg:
        yield ord(i)

def encoder(imagen , mensaje, pattern, img=False):

    imagen = cv2.imread(imagen, 1)
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

    if img ==False:
        mensaje = open("{}".format(mensaje), "r")
        mensaje = mensaje.read()

    generador = letter2ASCII(mensaje)
    pattern = pattern
    cont = 0
    length = len(mensaje)
    space = (imagen.shape[0] * imagen.shape[1] * 3) - pattern
    
    if space < length*pattern:
        print('Text too large')
        return 0
            
    for chn in range(4):
        for row in range(imagen.shape[0]):
            for col in range(imagen.shape[1]):
                cont += 1 
                if cont == pattern :
                    cont = 0 
                    try:
                        imagen[row][col][chn] = next(generador)
                    except StopIteration:
                        imagen[row][col][chn] = 0
                        name = input('    Name to save new image: ')
                        cv2.imwrite('{}'.format(name),cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
                        print('\n')
                        print('------- Image Encoded :) --------')
                        print('\n')
                        print('\n')
                        return imagen 
            
def decoder(imagen, pattern, img=False):
    imagen = cv2.imread(imagen, 1)
    imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

    pattern = pattern
    message = ''
    cont = 0
    
    for chn in range(4): 
        for row in range(imagen.shape[0]):
            for col in range(imagen.shape[1]):
                cont += 1
                if cont == pattern:
                    cont = 0 
                    letra = imagen[row][col][chn]
                    if letra != 0: 
                        message = message + chr(letra)
                    else:
                        if img == False:
                            print('\n')
                            print('Msg: ', message)
                            print('\n')
                            print('\n')
                            return message
                        else:
                            return message


if __name__ == '__main__':

    while opc != 5:

        print('\n ------- Menu -------')
        print('1.) Text -> Image')
        print('2.) Image -> Text')
        print('3.) Image into Image')
        print('4.) Image from Image')
        print('5.) Exit')
        print('\n')
        opc = int( input("  Option: ") )

        if opc == 1:
            path = input("\n    Path for image: ")
            msg = input("    .txt file: ")
            patt = int(input("    Pattern: "))
            encoder(path, msg, patt)
        elif opc == 2: 
            path = input("\n    Path for image: ")
            patt = int(input("    Pattern: "))
            decoder(path, patt)

        elif opc == 3:

            path = input("\n    Path for base image: ")
            path2 = input("    Path for image to hide: ")
            patt = int(input("    Pattern: "))
            msg = None

            with open("{}".format(path2), "rb") as img_file:
                msg = base64.b64encode(img_file.read())

            msg = msg.decode('utf-8')

            encoder(path, msg, patt, True)

        elif opc == 4:

            path = input("\n    Path for image: ")
            patt = int(input("    Pattern: "))
            data = decoder(path, patt, True)

            im = Image.open(BytesIO(base64.b64decode(data)))
            im.save('imageFromDecoder.png', 'PNG')

            print('\n')
            print('------- Image Decoded :) --------')
            print('\n')
            print('\n')


        elif opc == 5:
            print('\n Bye :(')
            sys.exit()



#Esercizio2
#Esercizio1
import numpy as np
import sys
import ctypes
import matplotlib.pyplot as plt

#Importo modulo
sys.path.append("/Users/mariarita/Metodi_computazionali/gitHub/MCF/Esercitazione_11")
import mycamera

#buffer=ctypes.create_string_buffer(1536 * 1024 * 2)
buffer=mycamera.read_camera()

#mv=memoryview(buffer[1])
#print(mv)
#Devo creare array da passare per visualizzare l'immagine
#print(len(buffer))

#Prova di decodifica 
c=int.from_bytes(buffer[3], byteorder="little")


#Creo array di array ciascuno contenento informazioni per un pixel
width  = 1536
height = 1024

image=[[0] * width for i in range(height)] #lista che riproduce una matrice del tipo [height][width]
for i in range (height):
    for j in range(0, 2*width, 2):
        pixel= buffer[(i*2*width)+j] + buffer[(i*2*width)+j+1] 
        pixel_decodificated=int.from_bytes(pixel, byteorder="little", signed="False") 
        image[i][j//2]=pixel_decodificated

plt.subplots(figsize=(16,9))
plt.imshow(image, origin="lower", norm='log', cmap='gray')
plt.axis('off')
plt.show()




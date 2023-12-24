#esercizio 2.2
import numpy as np
import sys
import ctypes
import matplotlib.pyplot as plt


# Carico la libreria libserie (libserie.so) che è presente nella cartella di lavoro  ('.')
_libcamera = np.ctypeslib.load_library('libmycamera.so', '.')
_libcamera.read_camera.argtypes =[ctypes.c_char_p]
_libcamera.read_camera.restype  = ctypes.c_int

class myCamera:

    def read_camera(self):
        buffer = ctypes.create_string_buffer(1536 * 1024 * 2 )
        s=_libcamera.read_camera(buffer)
        return buffer
    
    def decode(self, buffer, width, height):
        image=[[0] * width for i in range(height)] #lista che riproduce una matrice del tipo [height][width]
        for i in range (height):
            for j in range(0, 2*width, 2):
                pixel= buffer[(i*2*width)+j] + buffer[(i*2*width)+j+1] 
                pixel_decodificated=int.from_bytes(pixel, byteorder="little", signed="False") 
                image[i][j//2]=pixel_decodificated
        return image
    
    def visualize(self, image):
        plt.subplots(figsize=(16,9))
        plt.imshow(image, origin="lower", norm='log', cmap='gray')
        plt.axis('off')
        plt.show()

camera=myCamera()
buffer=camera.read_camera()
image=camera.decode(buffer, 1536, 1024)
camera.visualize(image)

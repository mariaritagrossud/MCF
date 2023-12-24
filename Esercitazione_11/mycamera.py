#Modulo per implemnetare libreria in C
#Modulo che implementa la libreria serie.so
import ctypes
import numpy 

# Carico la libreria libserie (libserie.so) che è presente nella cartella di lavoro  ('.')
_libcamera = numpy.ctypeslib.load_library('libmycamera.so', '.')

# definizoine tipi di input (argtypes) e di output (restypes) per la funzione read_camera di libmycamera
_libcamera.read_camera.argtypes =[ctypes.c_char_p]
_libcamera.read_camera.restype  = ctypes.c_int

# utilizzo di _libserie.serie_fib
# il parametro n va necessariamente convertito in int
def read_camera(): 
   
    buffer = ctypes.create_string_buffer(1536 * 1024 * 2 )
    s=_libcamera.read_camera(buffer)
    return buffer
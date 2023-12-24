#Modulo che implementa la libreria serie.so
import ctypes
import numpy 


# Carico la libreria libserie (libserie.so) che è presente nella cartella di lavoro  ('.')
_libserie = numpy.ctypeslib.load_library('libserie.so', '.')

# definizoine tipi di input (argtypes) e di output (restypes) per la funzione serie_fib di libserie
_libserie.fibonacci.argtypes = [ctypes.c_int]
_libserie.fibonacci.restype  = ctypes.c_double

# utilizzo di _libserie.serie_fib
# il parametro n va necessariamente convertito in int
def fibonacci(n):
    return _libserie.fibonacci(int(n))
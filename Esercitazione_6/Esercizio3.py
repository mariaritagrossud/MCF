#Esercizio3
import pandas as pd
import matplotlib.pyplot as plt
import math as mt
import numpy as np
from  scipy import integrate

file= pd.read_csv('oscilloscope.csv')
ch1=np.asarray(file["signal1"])
ch2=np.asarray(file["signal2"])
t=np.asarray(file["time"])


#Grafico segnali
plt.plot(t, ch1, label="Canale 1" , color="royalblue")
plt.plot(t, ch2, label="Canale 2" , color="red")
plt.title("Segnali dei due canali oscilloscopio")
plt.legend()
plt.xlabel("Tempo (s)")
plt.ylabel("Tensione (V)")
plt.show()


def my_derivative_vh(xx, yy, nh):
    dd = yy[nh:] - yy[:-nh]
    hh = xx[nh:] - xx[:-nh]
    print(yy[nh:])
    print(yy[:-nh])
    
    for ih in range(int(nh/2)):
        dd = np.append(yy[nh-ih-1]-yy[0], dd)
        dd = np.append(dd, yy[-1:]-yy[len(xx)-(nh-ih)])
    
        hh = np.append(xx[nh-ih-1]-xx[0], hh)
        hh = np.append(hh, xx[-1:]-xx[len(xx)-(nh-ih)])
    return dd/hh

#Canale1
der1=my_derivative_vh(t,ch1,40)
plt.plot(t, ch1, label="Segnale canale 1" , color="royalblue")
plt.plot(t, der1, label="Derivata canale 1 - n=40 " , color="red")
plt.title("Segnali e derivata canale 1")
plt.legend()
plt.xlabel("Tempo (s)")
plt.ylabel("Tensione (V)")
plt.show()

#Canale 2
der2=my_derivative_vh(t,ch2,40)
plt.plot(t, ch2, label="Segnale canale 2" , color="royalblue")
plt.plot(t, der2, label="Derivata canale 2 - n=40 " , color="red")
plt.title("Segnali e derivata canale 2")
plt.legend()
plt.xlabel("Tempo (s)")
plt.ylabel("Tensione (V)")
plt.show()


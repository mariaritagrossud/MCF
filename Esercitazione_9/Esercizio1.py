#Esercizio1


import soundfile as sf
import math as mt
import numpy as np
import matplotlib.pyplot as plt
import soundcard as sc
from scipy import constants, fft
import pandas as pd
from scipy.optimize import curve_fit

#Carico file
dati1 = pd.read_csv('data_sample1.csv', sep=",")
dati2 = pd.read_csv('data_sample2.csv', sep=",")
dati3 = pd.read_csv('data_sample3.csv', sep=",")
time1=np.asarray(dati1['time'])
time2=np.asarray(dati2['time'])
time3=np.asarray(dati3['time'])
noise1=np.asarray(dati1['meas'])
noise2=np.asarray(dati2['meas'])
noise3=np.asarray(dati3['meas'])

#Grafico rumori
fig = plt.figure(figsize=(8,7))
gs = fig.add_gridspec(2,2)
axs = gs.subplots()
fig.suptitle('Ricostruzione segnale filtrando frequenze')
axs[0,0].plot(time1, noise1, color="red")
axs[0,0].set(xlabel="Tempo (s)",ylabel="Ampiezza (u.a)", title="Rumore 1")
axs[0,1].plot(time2, noise2, color="blue")
axs[0,1].set(xlabel="Tempo (s)", title="Rumore 2")
axs[1,1].plot(time3, noise3, color="purple")
axs[1,1].set(xlabel="Tempo (s)", title="Rumore 3")
fig.tight_layout()
plt.show()

#Trasformata di Fourier segnali in ingresso
trasformata1=fft.rfft(noise1)
T_01=time1[1]-time1[0] #periodo campionamento
N1=len(trasformata1)
freq1=0.5*fft.rfftfreq(N1,d=T_01) 
print(len(freq1),len(trasformata1))
potenza1=trasformata1.real**2+trasformata1.imag**2


trasformata2=fft.rfft(noise2)
T_02=time2[1]-time2[0] #periodo campionamento
N2=len(trasformata2)
freq2=0.5*fft.rfftfreq(N2,d=T_02) 
potenza2=trasformata2.real**2+trasformata2.imag**2



trasformata3=fft.rfft(noise3)
T_03=time3[1]-time3[0] #periodo campionamento
N3=len(trasformata3)
freq3=0.5*fft.rfftfreq(N3,d=T_03) 
potenza3=trasformata3.real**2+trasformata3.imag**2



#Grafico potenze
#
fig = plt.figure()
gs = fig.add_gridspec(1,3)
axs = gs.subplots()
fig.suptitle('Ricostruzione segnale filtrando frequenze')
axs[0].plot(freq1[:len(trasformata1)//2], potenza1[:len(trasformata1)//2], color="red")
axs[0].set(xlabel="Frequenza (Hz)",ylabel="Potenza (u.a)", title="Rumore 1")
axs[1].plot(freq2[:len(trasformata2)//2], potenza2[:len(trasformata2)//2], color="blue")
axs[1].set(xlabel="Frequenza (Hz)",ylabel="Potenza (u.a)", title="Rumore 2")
axs[2].plot(freq3[:len(trasformata3)//2], potenza3[:len(trasformata3)//2], color="purple")
axs[2].set(xlabel="Frequenza (Hz)",ylabel="Potenza (u.a)", title="Rumore 3")
fig.tight_layout()
plt.show()

#Faccio fit
def func_test(xx, b, c):
     return c/((xx)**b)

#Fit 1
xx=freq1[:(len(trasformata1)//2)]
xx1=xx[1:]
yy=potenza1[:(len(trasformata1)//2)]
yy1=yy[1:]
par1, pcov1 = curve_fit(func_test, xdata=xx1, ydata=yy1, p0=[0.5, 4000])
y_func1=func_test(xx1,par1[0], par1[1])
print(par1)
print(pcov1)
plt.plot(xx1, yy1, color="blue", label="dati")
plt.plot(xx1, y_func1, color="red", label="fit")
plt.title("Rumore 1")
plt.ylabel("Potenza (u.a.) - log scale")
plt.xlabel("Frequenza (Hz) - log scale ")
plt.xscale("log")
plt.yscale("log")
plt.show()


#Fit2
xx=freq2[:(len(trasformata2)//2)]

xx2=xx[1:]
yy=potenza2[:(len(trasformata2)//2)]
yy2=yy[1:]
par2, pcov2 = curve_fit(func_test, xdata=xx2, ydata=yy2, p0=[1.1, 100])
y_func2=func_test(xx2,par2[0], par2[1])
print(par2)
print(pcov2)
plt.plot(xx2, yy2, color="blue", label="dati")
plt.plot(xx2, y_func2, color="red", label="fit")
plt.title("Rumore 2")
plt.ylabel("Potenza (u.a.) - log scale")
plt.xlabel("Frequenza (Hz) - log scale ")
plt.xscale("log")
plt.yscale("log")
plt.show()

#Fit3
xx=freq3[:(len(trasformata3)//2)]
xx3=xx[5:]
yy=potenza3[:(len(trasformata3)//2)]
yy3=yy[5:]
par3, pcov3 = curve_fit(func_test, xdata=xx3, ydata=yy3, p0=[2.2, 10000])
y_func3=func_test(xx3,par3[0], par3[1])
print(par3)
print(pcov3)
plt.plot(xx3, yy3, color="blue", label="dati")
plt.plot(xx3, y_func3, color="red", label="fit")
plt.title("Rumore 3")
plt.ylabel("Potenza (u.a.) - log scale")
plt.xlabel("Frequenza (Hz) - log scale ")
plt.xscale("log")
plt.yscale("log")
plt.show()

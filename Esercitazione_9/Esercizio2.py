#Esercizio2
import soundfile as sf
import math as mt
import numpy as np
import matplotlib.pyplot as plt
import soundcard as sc
from scipy import constants, fft
import pandas as pd
from scipy.optimize import curve_fit

#Importo i file
dati1 = pd.read_csv('4FGL_J2202.7+4216_weekly_9_15_2023_mcf.csv', sep=",")
dati2 = pd.read_csv("4FGL_J0721.9+7120_weekly_9_15_2023_mcf.csv", sep=",")
dati3 = pd.read_csv("4FGL_J0428.6-3756_weekly_9_15_2023_mcf.csv", sep=",")
dati4 = pd.read_csv("4FGL_J1256.1-0547_weekly_9_15_2023_mcf.csv", sep=",")
dati5 = pd.read_csv("4FGL_J2253.9+1609_weekly_9_15_2023_mcf.csv", sep=",")
dati6 = pd.read_csv("4FGL_J2232.6+1143_weekly_9_15_2023_mcf.csv", sep=",")

#Grafico con tutte le sorgenti
time1=dati1["Julian Date"].values
flux1=dati1["Photon Flux [0.1-100 GeV](photons cm-2 s-1)"].values
time2=dati2["Julian Date"].values
flux2=dati2["Photon Flux [0.1-100 GeV](photons cm-2 s-1)"].values
time3=dati3["Julian Date"].values
flux3=dati3["Photon Flux [0.1-100 GeV](photons cm-2 s-1)"].values
time4=dati4["Julian Date"].values
flux4=dati4["Photon Flux [0.1-100 GeV](photons cm-2 s-1)"].values
time5=dati5["Julian Date"].values
flux5=dati5["Photon Flux [0.1-100 GeV](photons cm-2 s-1)"].values
time6=dati6["Julian Date"].values
flux6=dati6["Photon Flux [0.1-100 GeV](photons cm-2 s-1)"].values

plt.scatter(time1, flux1, label="Bl Lac", s=2)
plt.scatter(time2, flux2, label=" S5 0716+71",s=2)
plt.scatter(time3, flux3, label=" PKS 0426-380",s=2)
plt.scatter(time4, flux4, label="3C 279",s=2)
plt.scatter(time5, flux5, label="3C 454.3",s=2)
plt.scatter(time6, flux6, label="CTA 102",s=2)
plt.title("Curve di luce")
plt.xlabel("Tempo (giorno giuliano)")
plt.ylabel("Flusso (photons cm-2 s-1)")
plt.yscale("log")
plt.legend()
plt.show()

#6 Pannelli con varie sorgenti
fig = plt.figure()
gs = fig.add_gridspec(2,3)
axs = gs.subplots()
fig.suptitle('Curve luce per diverse frequenze')
axs[0,0].scatter(time1, flux1, color="red",s=2)
axs[0,0].set(ylabel="Flusso (photons cm-2 s-1)", title="Sorgente: Bl Lac",yscale="log")
axs[0,1].scatter(time2, flux2, color="red",s=2)
axs[0,1].set(title="Sorgente: S5 0716+71",yscale="log")
axs[0,2].scatter(time3, flux3, color="red",s=2)
axs[0,2].set(title="Sorgente: PKS 0426-380",yscale="log")
axs[1,0].scatter(time4, flux4, color="blue",s=2)
axs[1,0].set(ylabel="Flusso (photons cm-2 s-1)", xlabel="Tempo (giorno giuliano)", title="Sorgente: 3C 279",yscale="log")
axs[1,1].scatter(time5, flux5, color="blue",s=2)
axs[1,1].set( xlabel="Tempo (giorno giuliano)", title="Sorgente: 3C 454.3",yscale="log")
axs[1,2].scatter(time6, flux6, color="blue",s=2)
axs[1,2].set(xlabel="Tempo (giorno giuliano)", title="Sorgente: CTA 102",yscale="log")
plt.show()

#Calcolo trasformata di Fourier
#Sorgente 1
trasformata1=fft.rfft(flux1)
T_01=time1[1]-time1[0] #periodo campionamento
N1=len(trasformata1)
freq1=0.5*fft.rfftfreq(N1,d=T_01) 
potenza1=trasformata1.real**2+trasformata1.imag**2

#Sorgente 2
trasformata2=fft.rfft(flux2)
T_02=time2[1]-time2[0] #periodo campionamento
N2=len(trasformata2)
freq2=0.5*fft.rfftfreq(N2,d=T_02) 
potenza2=trasformata2.real**2+trasformata2.imag**2

#Sorgente 3
trasformata3=fft.rfft(flux3)
T_03=time3[1]-time3[0] #periodo campionamento
N3=len(trasformata3)
freq3=0.5*fft.rfftfreq(N3,d=T_03) 
potenza3=trasformata3.real**2+trasformata3.imag**2

#Sorgente 4
trasformata4=fft.rfft(flux4)
T_04=time4[1]-time4[0] #periodo campionamento
N4=len(trasformata4)
freq4=0.5*fft.rfftfreq(N4,d=T_04) 
potenza4=trasformata4.real**2+trasformata4.imag**2

#Sorgente 5
trasformata5=fft.rfft(flux5)
T_05=time5[1]-time5[0] #periodo campionamento
N5=len(trasformata5)
freq5=0.5*fft.rfftfreq(N5,d=T_05) 
potenza5=trasformata5.real**2+trasformata5.imag**2

#Sorgente 6
trasformata6=fft.rfft(flux6)
T_06=time6[1]-time6[0] #periodo campionamento
N6=len(trasformata6)
freq6=0.5*fft.rfftfreq(N6,d=T_06) 
potenza6=trasformata6.real**2+trasformata6.imag**2


#Spettro potenza sorgenti

plt.scatter(freq1[:len(trasformata1)//2], potenza1[:len(trasformata1)//2], color="red", label="Bl Lac",s=2)
plt.scatter(freq2[:len(trasformata2)//2], potenza2[:len(trasformata2)//2], color="red", label="S5 0716+71",s=2)
plt.scatter(freq3[:len(trasformata3)//2], potenza3[:len(trasformata3)//2], color="red", label="PKS 0426-380",s=2)
plt.scatter(freq4[:len(trasformata4)//2], potenza4[:len(trasformata4)//2], color="blue", label="3C 279",s=2)
plt.scatter(freq5[:len(trasformata5)//2], potenza5[:len(trasformata5)//2], color="blue", label="3C 454.3",s=2)
plt.scatter(freq6[:len(trasformata6)//2], potenza6[:len(trasformata6)//2], color="blue", label="CTA 102",s=2)
plt.legend()
plt.yscale("log")
plt.ylabel("Potenza (u.a)")
plt.xlabel("Frequenza (Hz)")
plt.title("Spettri varie sorgenti")
plt.show()

#Normalizzazione al primo coefficiente
potenza_1=potenza1[:len(trasformata1)//2]
potenza_2=potenza2[:len(trasformata2)//2]
potenza_3=potenza3[:len(trasformata3)//2]
potenza_4=potenza4[:len(trasformata4)//2]
potenza_5=potenza5[:len(trasformata5)//2]
potenza_6=potenza6[:len(trasformata6)//2]

potenza_1n=potenza_1/potenza_1[0]
potenza_2n=potenza_2/potenza_2[0]
potenza_3n=potenza_3/potenza_3[0]
potenza_4n=potenza_4/potenza_4[0]
potenza_5n=potenza_5/potenza_5[0]
potenza_6n=potenza_6/potenza_6[0]

plt.scatter(freq1[:len(trasformata1)//2], potenza_1n, color="red", label="Bl Lac",s=2)
plt.scatter(freq2[:len(trasformata2)//2], potenza_2n, color="red", label="S5 0716+71",s=2)
plt.scatter(freq3[:len(trasformata3)//2], potenza_3n, color="red", label="PKS 0426-380",s=2)
plt.scatter(freq4[:len(trasformata4)//2],potenza_4n, color="blue", label="3C 279",s=2)
plt.scatter(freq5[:len(trasformata5)//2], potenza_5n, color="blue", label="3C 454.3",s=2)
plt.scatter(freq6[:len(trasformata6)//2], potenza_6n, color="blue", label="CTA 102",s=2)
plt.legend()
plt.ylabel("Potenza (u.a)")
plt.xlabel("Frequenza (Hz)")
plt.yscale("log")
plt.title("Spettri varie sorgenti nomralizzando al primo coefficiente")
plt.show()




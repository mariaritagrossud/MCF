#Esercizio3
import soundfile as sf
import math as mt
import numpy as np
import matplotlib.pyplot as plt
import soundcard as sc
from scipy import constants, fft
import pandas as pd
from scipy.optimize import curve_fit

dati = pd.read_csv('copernicus_PG_selected.csv', sep=",")
#time=dati["date"].values
inq1=dati["mean_co_ug/m3"].values
inq2=dati["mean_nh3_ug/m3"].values
inq3=dati["mean_no2_ug/m3"].values
inq4=dati["mean_o3_ug/m3"].values
inq5=dati["mean_pm10_ug/m3"].values
inq6=dati["mean_pm2p5_ug/m3"].values
inq7=dati["mean_so2_ug/m3"].values
#Ogni campionamento è n un giorno successivo
time=np.arange(0,len(inq1),1) #espresso in giorni

plt.plot(time, inq1)
plt.plot(time, inq2)
plt.plot(time, inq3)
plt.plot(time, inq4)
plt.plot(time, inq5)
plt.plot(time, inq6)
plt.plot(time, inq7)
plt.title("Concentrazioni inquinanti")
plt.ylabel("Concentrazione")
plt.xlabel("Tempo (giorni) ")
plt.show()

#Grafico CO
plt.plot(time, inq1)
plt.title("Concentrazione CO")
plt.ylabel("Concentrazione")
plt.xlabel("Tempo (giorni) ")
plt.show()

#Trasformata segnale
trasformata1=fft.fft(inq1)
T_01=time[1]-time[0] #periodo campionamento
N1=len(trasformata1)
freq1=0.5*fft.rfftfreq(N1,d=T_01) 
potenza1=trasformata1.real**2+trasformata1.imag**2


#Grafico potenza in funzione frequenza
plt.plot(freq1[:len(trasformata1)//2], potenza1[:len(trasformata1)//2], color="red")
plt.title("Potenza in funzione frequenza")
plt.xlabel("Frequenza (Hz)")
plt.ylabel("Potenza (u.a.)")
plt.show()

#Cerco frequenza massima (a parte 0)
max=0
indice_max=0
for i in range (len(freq1[:len(trasformata1)//2])):
    if (freq1[i]!=0 and potenza1[i] > max ):
        max=potenza1[i]
        indice_max=i

plt.plot(freq1[:len(trasformata1)//2], potenza1[:len(trasformata1)//2], color="red")
plt.axvline(freq1[indice_max],   color='mediumseagreen', ls="dashed", linewidth=1)
plt.title("Potenza in funzione frequenza")
plt.xlabel("Frequenza (Hz)")
plt.ylabel("Potenza (u.a.)")
plt.show()

#Ricsotruisco il segnale con solo quella frequenza e lo 0
metà_freq=freq1[:len(trasformata1)//2]
mask=metà_freq==freq1[indice_max]
coefficienti=trasformata1[:len(trasformata1)//2]*mask
coefficienti[0]=trasformata1[0]
segnale_ricostruito=fft.irfft(coefficienti)

#Confronto segnali
plt.plot(time[:len(trasformata1)//2], inq1[:len(trasformata1)//2], color="blue")
plt.plot(time[:len(trasformata1)//2], segnale_ricostruito[:len(trasformata1)//2], color="red")
plt.title("Concentrazione CO")
plt.ylabel("Concentrazione")
plt.xlabel("Tempo (giorni) ")
plt.show()

# -------------------------------------------------------------------------------------------------

#Grafico NH3
plt.plot(time, inq2)
plt.title("Concentrazione NH3")
plt.ylabel("Concentrazione")
plt.xlabel("Tempo (giorni) ")
plt.show()

#Trasformata segnale
trasformata2=fft.fft(inq2)
freq2=0.5*fft.rfftfreq(N1,d=T_01) 
potenza2=trasformata2.real**2+trasformata2.imag**2

#Grafico potenza in funzione frequenza
plt.plot(freq2[:len(trasformata2)//2], potenza2[:len(trasformata2)//2], color="red")
plt.title("Potenza in funzione frequenza")
plt.xlabel("Frequenza (Hz)")
plt.ylabel("Potenza (u.a.)")
plt.show()

#Cerco frequenza massima  a parte 0)
max2=0
indice_max2=0
for i in range (len(freq2[:len(trasformata2)//2])):
    if (freq2[i]!=0 and potenza2[i] > max2 ):
        max2=potenza2[i]
        indice_max2=i

plt.plot(freq2[:len(trasformata2)//2], potenza2[:len(trasformata2)//2], color="red")
plt.axvline(freq2[indice_max2],   color='mediumseagreen', ls="dashed", linewidth=1)
plt.title("Un picco")
plt.xlabel("Frequenza (Hz)")
plt.ylabel("Potenza (u.a.)")
plt.show()



#Ricsotruisco il segnale con solo quella frequenza
metà_freq2=freq2[:len(trasformata2)//2]
mask2=metà_freq2==freq2[indice_max2]
coefficienti2=trasformata2[:len(trasformata2)//2]*mask2
coefficienti2[0]=trasformata2[0]
segnale_ricostruito2=fft.irfft(coefficienti2)


#Confronto segnali
plt.plot(time, inq2, color="blue")
plt.plot(time[:len(time)-2], segnale_ricostruito2, color="red")
plt.title("Ricostruzione con solo un picco - NH3")
plt.ylabel("Concentrazione")
plt.xlabel("Tempo (giorni) ")
plt.show()


#considero anche massimo successivo
max2bis=0
indice_max2bis=0
for i in range (len(freq2[:len(trasformata2)//2])):
    if (freq2[i]!=0 and freq2[i]!=freq2[indice_max2] and potenza2[i] > max2bis ):
        max2bis=potenza2[i]
        indice_max2bis=i
coefficienti2[indice_max2bis]=trasformata2[indice_max2bis]

segnale_ricostruito2=fft.irfft(coefficienti2)
print(freq2[indice_max2])
print(freq2[indice_max2bis])

plt.plot(freq2[:len(trasformata2)//2], potenza2[:len(trasformata2)//2], color="red")
plt.axvline(freq2[indice_max2],   color='mediumseagreen', ls="dashed", linewidth=1)
plt.axvline(freq2[indice_max2bis],   color='mediumseagreen', ls="dashed", linewidth=1)
plt.title("Due picchi")
plt.xlabel("Frequenza (Hz)")
plt.ylabel("Potenza (u.a.)")
plt.show()

#Confronto segnali
plt.plot(time, inq2, color="blue")
plt.plot(time[:len(time)-2], segnale_ricostruito2, color="red")
plt.title("Ricostruzione con i due picchi principali - NH3")
plt.ylabel("Concentrazione")
plt.xlabel("Tempo (giorni) ")
plt.show()









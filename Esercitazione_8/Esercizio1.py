#Esercizio1.py: risolvere un cricuito RC

import math as mt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

#Parametri 
a=0
b=10
n=200
h = (b-a)/n
Vout_O=0
RC_1=1
RC_2=0.1
RC_3=0.5

#Funzioni
def V_in(time): #gli elementi dell'array devono essere interi
    v_in=1
    if int(time) %2 != 0:
     v_in = -1

    return v_in

def fode(Vout, t, K):
    return (1/(K))*(V_in(t)-Vout)


time = np.linspace(0, 10, n)
Vout_1 = np.empty((0,0))

#Risolvo equazione per RC=1
Vout_1 = integrate.odeint(fode, y0=Vout_O, t=time, args=(RC_1,))

#Risolvo equazione per RC=0.1
Vout_2 = integrate.odeint(fode, y0=Vout_O, t=time, args=(RC_2,))

#Risolvo equazione per RC=0.5
Vout_3 = integrate.odeint(fode, y0=Vout_O, t=time, args=(RC_3,))

V_in_1=np.empty(0)
#Creo array 
for item in time:
    V_in_1=np.append(V_in_1,V_in(item))

#Plot della parte reale e immaginaria dei coefficienti

fig = plt.figure()
gs = fig.add_gridspec(1,3, hspace=0)
axs = gs.subplots(sharex=True, sharey=True, figsize=(15, 15))
fig.suptitle("Segnale in ingresso e in uscita in funzione del tempo con diversi valori di RC")
axs[0].plot(time, V_in_1, color="mediumseagreen",label="$V_{out}$")
axs[0].plot(time, Vout_1, color="salmon",label="$V_{out}$")
axs[0].set(ylabel="Tensione (V)", xlabel="Tempo(s)", title="RC=1", figsize=(15, 15))
axs[1].plot(time, V_in_1, color="mediumseagreen",label="$V_{out}$")
axs[1].plot(time, Vout_2, color="salmon",label="$V_{out}$")
axs[1].set( xlabel="Tempo(s)", title="RC=0.1")
axs[2].plot(time, V_in_1, color="mediumseagreen",label="$V_{out}$")
axs[2].plot(time, Vout_3, color="salmon",label="$V_{out}$")
axs[2].set( xlabel="Tempo(s)", title="RC=0.5")
plt.show()

#Salvo i risutati in un file csv
dati=pd.DataFrame(columns=["Tempo (s) ", "Vin (V) ", " Vout (V) - RC=1 ","Vout (V) - RC=0.1 "," Vout (V) - RC=0.5 "])
dati["Tempo (s) "]=time
dati["Vin (V) "]=V_in_1
dati[" Vout (V) - RC=1 "]=Vout_1
dati["Vout (V) - RC=0.1 "]=Vout_2
dati[" Vout (V) - RC=0.5 "]=Vout_3
dati.to_csv("dati.csv")

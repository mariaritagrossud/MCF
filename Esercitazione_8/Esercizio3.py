#Esercizio3
import math as mt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import integrate

def fode(r,t,omega):
    dxdt=r[1]
    dydt=-omega**2*r[0]**3
    return (dxdt,dydt
    )

#Tempi
dt = 0.05 # s
time = np.arange(0, 20, dt)

#Omega
omega=1000

#Condizioni iniziali
x0_1 = 0.1
x0_2 = 0.01
v0   = 1
v1 = 20

c0_1 = (x0_1, v0)
c0_2 = (x0_2, v0)
c0_3 = (x0_1, v0)
c0_4= (x0_1, v1)

# Soluzioni
sol1  = integrate.odeint(fode, c0_1, time, args=(omega,)) 
sol2  = integrate.odeint(fode, c0_2, time, args=(omega,)) 
sol3  = integrate.odeint(fode, c0_3, time, args=(omega,)) 
sol4  = integrate.odeint(fode, c0_4, time, args=(omega,)) 

# Grafico soluzioni
plt.plot(time, sol1[:,0], color='mediumseagreen', label="x0=0.1cm")
plt.plot(time, sol2[:,0], color='magenta',label="x0=0.01cm")
plt.legend(loc="upper right")
plt.title("Confronto soluzioni con stessa velocità e posizioni iniziali diverse")
plt.xlabel('time (s)')
plt.ylabel('x    (m)')
plt.show()


# Grafico soluzioni
plt.plot(time, sol3[:,0], color='mediumseagreen', label="v0=1 m/s")
plt.plot(time, sol4[:,0], color='magenta',label="v0=20 m/s")
plt.legend(loc="upper right")
plt.title("Confronto soluzioni con stessa posizione iniziale e velocità diverse")
plt.xlabel('time (s)')
plt.ylabel('x    (m)')
plt.show()
#Esercizio2
import math as mt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import integrate

g=9.81

def fsimode(r,t,l):
    "Definisco due equazioni differenziali"
    dthetadt=r[1]
    domegadt=-(g/l)*np.sin(r[0])
    drdt = [dthetadt, domegadt]
    return drdt

#Primo caso
l1=0.5
theta_rad_0=45*mt.pi/180
r0 = [theta_rad_0,0] #Condizioni iniziali
time = np.linspace(0, 20, 1000)
sol_1 = integrate.odeint(fsimode, r0, time, args=(l1,))

fig = plt.figure()
gs = fig.add_gridspec(2,1, hspace=0)
axs = gs.subplots(sharex=True)
fig.suptitle("Soluzioni equazione differenziale")
axs[0].plot(time, sol_1[:,0], color="red")
axs[0].set(ylabel="Theta (rad)", xlabel="Tempo(s)")
axs[1].plot(time, sol_1[:,1], color="blue")
axs[1].set(ylabel="Omega (rad\s)", xlabel="Tempo(s)")
axs[1].set_ylim(-10,10)

fig.tight_layout()
plt.show()

#Secondo caso
l2=1
theta_rad_2=45*mt.pi/180
r0_2 = [theta_rad_2,0] #Condizioni iniziali
sol_2 = integrate.odeint(fsimode, r0_2, time, args=(l2,))

fig = plt.figure()
gs = fig.add_gridspec(2,1, hspace=0)
axs = gs.subplots(sharex=True)
fig.suptitle("Soluzioni equazione differenziale")
axs[0].plot(time, sol_2[:,0], color="red")
axs[0].set(ylabel="Theta (rad)", xlabel="Tempo(s)")
axs[1].plot(time, sol_2[:,1], color="blue")
axs[1].set(ylabel="Omega (rad\s)", xlabel="Tempo(s)")
axs[1].set_ylim(-10,10)

fig.tight_layout()
plt.show()

#Terzo caso
l3=0.5
theta_rad_3=30*mt.pi/180
r0_3 = [theta_rad_3,0] #Condizioni iniziali
sol_3 = integrate.odeint(fsimode, r0_3, time, args=(l3,))

fig = plt.figure()
gs = fig.add_gridspec(2,1, hspace=0)
axs = gs.subplots(sharex=True)
fig.suptitle("Soluzioni equazione differenziale")
axs[0].plot(time, sol_3[:,0], color="red")
axs[0].set(ylabel="Theta (rad)", xlabel="Tempo(s)")
axs[1].plot(time, sol_3[:,1], color="blue")
axs[1].set(ylabel="Omega (rad\s)", xlabel="Tempo(s)")
axs[1].set_ylim(-10,10)

fig.tight_layout()
plt.show()

#Confronto theta in funzione tempo le varie soluzioni
plt.plot(time,sol_1[:,0], color="blue", label="Primo caso")
plt.plot(time,sol_2[:,0], color="red", label="Secondo caso")
plt.plot(time,sol_3[:,0], color="green", label="Terzo caso")
plt.title("Confronto andamento theta in funzione tempo")
plt.legend()
plt.show()


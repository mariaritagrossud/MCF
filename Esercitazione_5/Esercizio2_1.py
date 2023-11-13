import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Scarico un modulo del rilevatore ( equivalente ad un file )
mod0= pd.read_csv('hit_times_M0.csv')

#Istrogramma
n0, bins0, p0 = plt.hist(mod0["hit_time"], bins=30, range=(100000,1000010000), color='red', alpha=0.7 )
plt.title("Istogramma dell'tempo di rivelazione urto")
plt.xlabel("Tempo rivelazione (ns)")
plt.show()

#Creo array delle differenze temporali
time=np.array(mod0["hit_time"])
print(time)
deltat_0=np.diff(time)
amask=deltat_0 > 0
deltat_0_log=np.log10(deltat_0[amask])
n1, bins1, p1 = plt.hist(deltat_0_log, bins=80, range=(0,20), color='red', alpha=0.7 )
plt.title("Istogramma intervallo temporale ∆t tra un urto e altro ")
plt.xlabel("log10(∆t)")
plt.show()

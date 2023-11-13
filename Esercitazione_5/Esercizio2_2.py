import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt

#Importo modulo
sys.path.append("/Users/mariarita/Metodi_computazionali/Esercitazione_5")
import reco

#Leggere il file e per ognuno inizializzare un hit
def array_hit(nome_file):
    array_hits=np.empty(0)
    modulo=pd.read_csv(nome_file)
    for i in range (1,len(modulo)):
        nuovo_hit = reco.Hit(modulo["mod_id"][i],modulo["det_id"][i],modulo["hit_time"][i])
        array_hits=np.append(array_hits,nuovo_hit)
    return array_hits

#Creo array eventi per i vari moduli
eventi0=array_hit('hit_times_M0.csv')
eventi1=array_hit('hit_times_M1.csv')
eventi2=array_hit('hit_times_M2.csv')
eventi3=array_hit('hit_times_M3.csv')

#Array con hit ordinati temporalemente
eventi_tot0=np.append(eventi0, eventi1)
eventi_tot1=np.append(eventi_tot0,eventi2)
eventi_tot2=np.append(eventi_tot1,eventi3)
eventi_tot=np.sort(eventi_tot2)

#Differenza temporale
differenze=np.diff(eventi_tot)

differenze_tempi=np.empty(0)
for i in range (len(differenze)):
    differenze_tempi=np.append(differenze_tempi,differenze[i])
amask= differenze_tempi> 0
log_differenze_tempi=np.log10(differenze_tempi[amask])
n1, bins1, p1 = plt.hist(log_differenze_tempi, bins=150, color='red', alpha=0.7 )
plt.title("Istogramma intervalli temporali ∆t tra un urto e altro")
plt.xlabel("log10(∆t)")
plt.yscale("log")
plt.show()

#Osservazione: il primo picco riguarda urti di un stesso evento, quelli del secondo urti di eventi diversi
#Esercizio1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as mt
from scipy.optimize import curve_fit

#Acquisisco file
dataset = pd.read_csv('Jpsimumu.csv')
E1=np.asarray(dataset["E1"])
E2=np.asarray(dataset["E2"])
px1=np.asarray(dataset["px1"])
py1=np.asarray(dataset["py1"])
pz1=np.asarray(dataset["pz1"])
px2=np.asarray(dataset["px2"])
py2=np.asarray(dataset["py2"])
pz2=np.asarray(dataset["pz2"])


#Definizione prima funzione di fit
def fg1(xx ,A, m, sigma, p1, p2):
    """""
    Primo coeff: A
    Secondo coeff: media
    Terzo coeff: sigma
    Quarto coeff: p1
    Qinto coeff: po
    """""
    return A*np.exp(-(xx-m)**2/(sigma**2))+ p1*xx+p2

def fg2(xx ,A1, A2, m, sigma1,sigma2, p1, p2):
    """""
    Primo coeff: A
    Secondo coeff: media
    Terzo coeff: sigma
    Quarto coeff: p1
    Qinto coeff: po
    """""
    return A1*np.exp(-(xx-m)**2/(sigma1**2))+A2*np.exp(-(xx-m)**2/(sigma2**2)) +p1*xx+p2


#Calcolo massa invariante
massa_invariante=np.empty(0)
for i in range (len(E1)):
    massa=mt.sqrt(pow(E1[i]+E2[i],2)- (pow(px1[i]+px2[i],2)+pow(py1[i]+py2[i],2)+pow(pz1[i]+pz2[i],2)))
    massa_invariante=np.append(massa_invariante,massa)

n1, bins1, p1 = plt.hist(massa_invariante, bins=150, color='red', alpha=0.7 )
plt.title("Istogramma massa invariante")
plt.xlabel("Massa invariante (GeV)")
plt.ylabel("Numero eventi per bin")
plt.show()

#Riduco intervallo (prendo valori solo tra 2.6 e 3.5)
massa_invariante_red=np.empty(0)
for i in range (len(massa_invariante)):
    if(massa_invariante[i]>2.6 and massa_invariante[i]<3.5):
        massa_invariante_red=np.append(massa_invariante_red,massa_invariante[i])

n2, bins2, p2 = plt.hist(massa_invariante_red, bins=150, color='red', alpha=0.7 )
plt.title("Istogramma massa invariante - intervallo ristretto")
plt.xlabel("Massa invariante (GeV)")
plt.ylabel("Numero eventi per bin")
plt.show()


#Fit
# Calcolo centro del bin come valore come: (bin_xmin + bin_xmax)/2
bincenters = (bins2[:-1] + bins2[1:])/2


# Maschera per rimuovere bin vuoti dal fit
mask = np.nonzero(n2)

# Fit.  Parametri ottimizzati (par). Matrice di covarinaza (pcov)
par, pcov = curve_fit(fg1, xdata=bincenters[mask], ydata=n2[mask], 
                      sigma=np.sqrt(n2[mask]), p0=[600,3.1, 0.2, 1, 1], absolute_sigma=True)

# Grafico risultato fit
y_fit=fg1(bincenters,par[0],par[1],par[2],par[3],par[4])


#Scarto tra un dati e fit
scarto=np.empty(0)
for i in range(len(n2)):
    scarto=np.append(scarto,y_fit[i]-n2[i])


# Grafico con due subplot
fig, ax = plt.subplots(2,1, figsize=(9,6), gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
# Rimuovo spazio verticale fra i subplot
fig.subplots_adjust(hspace=0)

# Grafico subplot 0 (dati e funzione di fit)
ax[0].set_title('Fit con funzione fg1 e scarti tra dati e fit', fontsize=16, color='darkred')
ax[0].hist(massa_invariante_red, bins=150, color='red', alpha=0.7, label="Dati " )
ax[0].plot(bincenters, y_fit, c='blue', label="Fit con $f_{g1}$")
ax[0].set_ylabel('Eventi Misurati', fontsize=14)
ax[0].tick_params(axis="y", labelsize=14) 
ax[0].legend(fontsize=14, frameon=False)

# Grafico subplot 1 (rapporto dati / funzione di fit)
ax[1].scatter(bincenters,scarto, marker=".",color="mediumseagreen", label="scarti")
ax[1].set_xlabel('Massa invariante [GeV]', fontsize =14)
ax[1].set_ylabel('Scarti',  fontsize =14)
ax[1].tick_params(axis="x",   labelsize=14) 
ax[1].tick_params(axis="y",   labelsize=14) 
ax[1].legend(fontsize=14, frameon=False)
ax[1].set_ylim(-31,31)       
plt.show()



#Chiqudro
chi2 =  np.sum( (scarto)**2 /n2 ) 
#Chi quadro ridotto
ndof = len(n2)-len(par)
chi2_rid=chi2/ndof

#Parametri e chiquadro
print(' --- Parametri  ---')
print('     A   = {:3.0f} +- {:1.0f}'.format(par[0], mt.sqrt(pcov[0,0])) ) 
print('     media= {:3.1f} +- {:1.1f}'.format(par[1], mt.sqrt(pcov[1,1])) )
print('     sigma= {:3.1f} +- {:1.1f}'.format(par[2], mt.sqrt(pcov[2,2])) )
print('     p1  = {:3.0f} +- {:1.0f}'.format(par[3], mt.sqrt(pcov[3,3])) ) 
print('     t2 = {:3.1f} +- {:1.1f}'.format(par[4], mt.sqrt(pcov[4,4])) )
print("Chi quadro:", chi2)
print("Chi quadro ridotto:", chi2_rid)

#Fit 2
# Fit.  Parametri ottimizzati (par). Matrice di covarinaza (pcov)
par2, pcov2 = curve_fit(fg2, xdata=bincenters[mask], ydata=n2[mask], 
                      sigma=np.sqrt(n2[mask]), p0=[600,400,3.1, 0.2,0.1, 1, 1], absolute_sigma=True)

# Grafico risultato fit
y_fit2=fg2(bincenters,par2[0],par2[1],par2[2],par2[3],par2[4],par2[5],par2[6])

#Scarto tra un dati e fit
scarto2=np.empty(0)
for i in range(len(n2)):
    scarto2=np.append(scarto2,y_fit2[i]-n2[i])


# Grafico con due subplot
fig, ax = plt.subplots(2,1, figsize=(9,6), gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
# Rimuovo spazio verticale fra i subplot
fig.subplots_adjust(hspace=0)

# Grafico subplot 0 (dati e funzione di fit)
ax[0].set_title('Fit con funzione fg2 e scarti tra dati e fit', fontsize=16, color='darkred')
ax[0].hist(massa_invariante_red, bins=150, color='red', alpha=0.7, label="Dati " )
ax[0].plot(bincenters, y_fit2, c='blue', label="Fit con $f_{g2}$")
ax[0].set_ylabel('Eventi Misurati', fontsize=14)
ax[0].tick_params(axis="y", labelsize=14) 
ax[0].legend(fontsize=14, frameon=False)

# Grafico subplot 1 (rapporto dati / funzione di fit)
ax[1].scatter(bincenters,scarto2, marker=".",color="mediumseagreen")
ax[1].set_xlabel('Massa invariante [GeV]', fontsize =14)
ax[1].set_ylabel('Scarti',  fontsize =14)
ax[1].tick_params(axis="x",   labelsize=14) 
ax[1].tick_params(axis="y",   labelsize=14) 
ax[1].set_ylim(-31,31)       
plt.show()




#Chiqudro
chi2_2 =  np.sum( (scarto2)**2 /n2 ) 
#Chi quadro ridotto
ndof_2 = len(n2)-len(par2)
chi2_rid_2=chi2_2/ndof_2

#Parametri e chiquadro
print(' --- Parametri  ---')
print('     A   = {:3.0f} +- {:1.0f}'.format(par2[0], mt.sqrt(pcov2[0,0])) ) 
print('     media= {:3.1f} +- {:1.1f}'.format(par2[1], mt.sqrt(pcov2[1,1])) )
print('     sigma= {:3.1f} +- {:1.1f}'.format(par2[2], mt.sqrt(pcov2[2,2])) )
print('     p1  = {:3.0f} +- {:1.0f}'.format(par2[3], mt.sqrt(pcov2[3,3])) ) 
print('     t2 = {:3.1f} +- {:1.1f}'.format(par2[4], mt.sqrt(pcov2[4,4])) )
print("Chi quadro:", chi2_2)
print("Chi quadro ridotto:", chi2_rid_2)


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
print('     p2 = {:3.1f} +- {:1.1f}'.format(par[4], mt.sqrt(pcov[4,4])) )
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
print('     A1  = {:3.0f} +- {:1.0f}'.format(par2[0], mt.sqrt(pcov2[0,0])) ) 
print('     A2= {:3.1f} +- {:1.1f}'.format(par2[1], mt.sqrt(pcov2[1,1])) )
print('     media= {:3.1f} +- {:1.1f}'.format(par2[2], mt.sqrt(pcov2[2,2])) )
print('     sigma1= {:3.0f} +- {:1.0f}'.format(par2[3], mt.sqrt(pcov2[3,3])) ) 
print('     sigma2= {:3.1f} +- {:1.1f}'.format(par2[4], mt.sqrt(pcov2[4,4])) )
print('     p1= {:3.1f} +- {:1.1f}'.format(par2[5], mt.sqrt(pcov2[5,5])) )
print('     p2= {:3.1f} +- {:1.1f}'.format(par2[6], mt.sqrt(pcov2[6,6])) )
print("Chi quadro:", chi2_2)
print("Chi quadro ridotto:", chi2_rid_2)


#Riduco intervallo (prendo valori solo tra 2.6 e 3.5)
massa_invariante_red2=np.empty(0)
for i in range (len(massa_invariante)):
    if(massa_invariante[i]>3.5 and massa_invariante[i]<4):
        massa_invariante_red2=np.append(massa_invariante_red2,massa_invariante[i])

numero_bins=35
n3, bins3, p3 = plt.hist(massa_invariante_red2, bins=numero_bins, color='red', alpha=0.7 )
plt.title("Istogramma massa invariante - intervallo ristretto 2")
plt.xlabel("Massa invariante (GeV)")
plt.ylabel("Numero eventi per bin")
plt.show()

#Fit
# Calcolo centro del bin come valore come: (bin_xmin + bin_xmax)/2
bincenters3 = (bins3[:-1] + bins3[1:])/2


# Maschera per rimuovere bin vuoti dal fit
mask3 = np.nonzero(n3)

# Fit.  Parametri ottimizzati (par). Matrice di covarinaza (pcov)
par3, pcov3 = curve_fit(fg1, xdata=bincenters3[mask3], ydata=n3[mask3], 
                      sigma=np.sqrt(n3[mask3]), p0=[1,3.7, 0.2, 0, 0], absolute_sigma=True)

# Grafico risultato fit
y_fit3=fg1(bincenters3,par3[0],par3[1],par3[2],par3[3],par3[4])


#Scarto tra un dati e fit
scarto3=np.empty(0)
for i in range(len(n3)):
    scarto3=np.append(scarto3,y_fit3[i]-n3[i])


# Grafico con due subplot
fig, ax = plt.subplots(2,1, figsize=(9,6), gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
# Rimuovo spazio verticale fra i subplot
fig.subplots_adjust(hspace=0)

# Grafico subplot 0 (dati e funzione di fit)
ax[0].set_title('Fit con funzione fg1 e scarti tra dati e fit', fontsize=16, color='darkred')
ax[0].hist(massa_invariante_red2, bins=numero_bins, color='red', alpha=0.7, label="Dati " )
ax[0].plot(bincenters3, y_fit3, c='blue', label="Fit con $f_{g1}$")
ax[0].set_ylabel('Eventi Misurati', fontsize=14)
ax[0].tick_params(axis="y", labelsize=14) 
ax[0].legend(fontsize=14, frameon=False)

# Grafico subplot 1 (rapporto dati / funzione di fit)
ax[1].scatter(bincenters3,scarto3, marker=".",color="mediumseagreen", label="scarti")
ax[1].set_xlabel('Massa invariante [GeV]', fontsize =14)
ax[1].set_ylabel('Scarti',  fontsize =14)
ax[1].tick_params(axis="x",   labelsize=14) 
ax[1].tick_params(axis="y",   labelsize=14) 
ax[1].legend(fontsize=14, frameon=False)
ax[1].set_ylim(-31,31)       
plt.show()



#Chiqudro
chi2_3 =  np.sum( (scarto3)**2 /n3 ) 
#Chi quadro ridotto
ndof_3 = len(n3)-len(par3)
chi2_rid_3=chi2_3/ndof_3

#Parametri e chiquadro
print(' --- Parametri  ---')
print('     A   = {:3.0f} +- {:1.0f}'.format(par3[0], mt.sqrt(pcov3[0,0])) ) 
print('     media= {:3.1f} +- {:1.1f}'.format(par3[1], mt.sqrt(pcov3[1,1])) )
print('     sigma= {:3.1f} +- {:1.1f}'.format(par3[2], mt.sqrt(pcov3[2,2])) )
print('     p1  = {:3.0f} +- {:1.0f}'.format(par3[3], mt.sqrt(pcov3[3,3])) ) 
print('     p2 = {:3.1f} +- {:1.1f}'.format(par3[4], mt.sqrt(pcov3[4,4])) )
print("Chi quadro:", chi2_3)
print("Chi quadro ridotto:", chi2_rid_3)

#Fit 2
# Fit.  Parametri ottimizzati (par). Matrice di covarinaza (pcov)
par4, pcov4 = curve_fit(fg2, xdata=bincenters3[mask3], ydata=n3[mask3], 
                      sigma=np.sqrt(n3[mask3]), p0=[50,2,3.7, 0.2,0.1, 1, 1], absolute_sigma=True)

# Grafico risultato fit
y_fit4=fg2(bincenters3,par4[0],par4[1],par4[2],par4[3],par4[4],par4[5],par4[6])

#Scarto tra un dati e fit
scarto4=np.empty(0)
for i in range(len(n3)):
    scarto4=np.append(scarto4,y_fit4[i]-n3[i])


# Grafico con due subplot
fig, ax = plt.subplots(2,1, figsize=(9,6), gridspec_kw={'height_ratios': [3, 1]}, sharex=True)
# Rimuovo spazio verticale fra i subplot
fig.subplots_adjust(hspace=0)

# Grafico subplot 0 (dati e funzione di fit)
ax[0].set_title('Fit con funzione fg2 e scarti tra dati e fit', fontsize=16, color='darkred')
ax[0].hist(massa_invariante_red2, bins=numero_bins, color='red', alpha=0.7, label="Dati " )
ax[0].plot(bincenters3, y_fit4, c='blue', label="Fit con $f_{g2}$")
ax[0].set_ylabel('Eventi Misurati', fontsize=14)
ax[0].tick_params(axis="y", labelsize=14) 
ax[0].legend(fontsize=14, frameon=False)

# Grafico subplot 1 (rapporto dati / funzione di fit)
ax[1].scatter(bincenters3,scarto4, marker=".",color="mediumseagreen")
ax[1].set_xlabel('Massa invariante [GeV]', fontsize =14)
ax[1].set_ylabel('Scarti',  fontsize =14)
ax[1].tick_params(axis="x",   labelsize=14) 
ax[1].tick_params(axis="y",   labelsize=14) 
ax[1].set_ylim(-31,31)       
plt.show()




#Chiqudro
chi2_4 =  np.sum( (scarto4)**2 /n3 ) 
#Chi quadro ridotto
ndof_4 = len(n3)-len(par4)
chi2_rid_4=chi2_4/ndof_4

#Parametri e chiquadro
print(' --- Parametri  ---')
print('     A1   = {:3.2f} +- {:1.2f}'.format(par4[0], mt.sqrt(pcov4[0,0])) ) 
print('     A2= {:3.2f} +- {:1.2f}'.format(par4[1], mt.sqrt(pcov4[1,1])) )
print('     media= {:3.2f} +- {:1.2f}'.format(par4[2], mt.sqrt(pcov4[2,2])) )
print('     sigma1  = {:3.2f} +- {:1.2f}'.format(par4[3], mt.sqrt(pcov4[3,3])) ) 
print('     sigma2 = {:3.2f} +- {:1.2f}'.format(par4[4], mt.sqrt(pcov4[4,4])) )
print('     p1= {:3.2f} +- {:1.2f}'.format(par4[5], mt.sqrt(pcov4[5,5])) )
print('     p2= {:3.2f} +- {:1.2f}'.format(par4[6], mt.sqrt(pcov4[6,6])) )
print("Chi quadro:", chi2_4)
print("Chi quadro ridotto:", chi2_rid_4)
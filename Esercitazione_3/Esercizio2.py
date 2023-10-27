import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Leggo il file e creo il DataFrame corrispondente
df_fromfile = pd.read_csv('4LAC_DR2_sel.csv')
#Mostro colonne
print(df_fromfile.columns)
#Mostro estratto
print(df_fromfile)

#Grafico dell'indice spettrale in funzione del flusso
plt.scatter(df_fromfile['Flux1000'],df_fromfile['PL_Index'],s=4) #Demarco i punti del grafico
plt.title("Indice spettrale in funzione del flusso")
plt.xlabel('Flux1000 [photons cm-2 s-1]')
plt.xscale("log")
plt.ylabel('PL Index')
plt.show()

#Grafico dell'indice spettrale in funzione del logaritmo in base 10 di nu_syn
#Creo array con una colonna della tabella
x1=np.log10(df_fromfile.loc[(df_fromfile['nu_syn']>0), "nu_syn"])
y1=df_fromfile.loc[(df_fromfile['nu_syn']>0),"PL_Index"] #Valori delle iìrghe in cui la frequenza non è nulla
plt.scatter(x1, y1, s=4) #Demarco i punti del grafico
plt.title("Indice spettrale in funzione frequenza")
plt.xlabel('log(nu_syn [Hz])')
plt.ylabel('PL Index')
plt.yscale("log")#Uso scala logaritmica per la y
plt.show()


#Grafico in cui distinguo due sorgenti: bll e fsrq
#Creo array in cui considero valori di bll
#mydf.loc[( mydf['Log'] > 10) & ( mydf['Log'] < 100), 'Range']1
x1_bll=np.log10(df_fromfile.loc[(df_fromfile['CLASS']=="bll") & (df_fromfile['nu_syn']>0), "nu_syn"])
y1_bll=df_fromfile.loc[(df_fromfile['CLASS']=="bll") & (df_fromfile['nu_syn']>0), 'PL_Index']

#Creo array in cui considero valori di fsrq
x1_fsrq=np.log10(df_fromfile.loc[(df_fromfile['CLASS']=="fsrq") & (df_fromfile['nu_syn']>0), "nu_syn"])
y1_fsrq=df_fromfile.loc[(df_fromfile['CLASS']=="fsrq") & (df_fromfile['nu_syn']>0), 'PL_Index']


#Grafico deelle due sorgenti
plt.scatter(x1_bll, y1_bll, s=8, color="red", alpha=0.4 , label="bll")
plt.scatter(x1_fsrq, y1_fsrq, s=8, color="blue", alpha=0.4 , label="fsrq") 
plt.title("Indice spettrale in funzione frequenza ")
plt.legend()
plt.xlabel('log(nu_syn [Hz])')
plt.ylabel('PL Index')
plt.yscale("log")#Uso scala logaritmica per la y
plt.show()

#Grafico delle due sorgenti con incertezza
inc_y1_bll=df_fromfile.loc[(df_fromfile['CLASS']=="bll") & (df_fromfile['nu_syn']>0), 'Unc_PL_Index']
inc_y1_fsrq=df_fromfile.loc[(df_fromfile['CLASS']=="fsrq") & (df_fromfile['nu_syn']>0), 'Unc_PL_Index']
plt.errorbar(x1_bll, y1_bll, yerr=inc_y1_bll, color="red", alpha=0.3 , label="bll", fmt=".")
plt.errorbar(x1_fsrq, y1_fsrq, yerr=inc_y1_fsrq, color="blue", alpha=0.3 , label="fsrq", fmt=".")
plt.title("Indice spettrale in funzione frequenza con errori ")
plt.legend()
plt.xlabel('log(nu_syn [Hz])')
plt.ylabel('PL Index')
plt.yscale("log")#Uso scala logaritmica per la y
plt.show()

#Istogramma dell'indice  spettrale
n1, bins1, p1 = plt.hist(df_fromfile.loc[(df_fromfile['CLASS']=="bll"), 'PL_Index'], bins=80, range=(1, 4), color='red', alpha=0.7, label="bll" )
n2, bins2, p2 = plt.hist(df_fromfile.loc[(df_fromfile['CLASS']=="fsrq"), 'PL_Index'], bins=80, range=(1, 4), color='blue', alpha=0.7, label="fsrq" )
plt.title("Istogramma dell'indice  spettrale")
plt.ylabel('Numero di sorgenti')
plt.legend()
plt.show()

#Istogramma della frequenza di picco
n1, bins1, p1 = plt.hist(x1_bll, bins=50, range=(11, 21), color='red', alpha=0.7, label="bll" )
n2, bins2, p2 = plt.hist(x1_fsrq, bins=50, range=(11, 21), color='blue', alpha=0.7, label="fsrq" )
plt.title("Istogramma della frequenza di picco")
plt.ylabel('Numero di sorgenti')
plt.legend()
plt.show()

#Compongo tra loro i grafici
fig = plt.figure()
gs = fig.add_gridspec(2, 2, hspace=0, wspace=0)
((ax1, ax2), (ax3, ax4)) = gs.subplots(sharex='col', sharey='row')
plt.suptitle("Decomposizione dell'indice spettrale e frequenze")
ax1.hist(x1_bll, bins=50, range=(11, 21), color='red', alpha=0.7, label="bll" )
ax3.scatter(x1_bll, y1_bll, s=10, color="red", alpha=0.4 , label="bll")
ax4.hist(df_fromfile.loc[(df_fromfile['CLASS']=="bll"), 'PL_Index'], bins=80, range=(1, 3.6), color='red', alpha=0.7, label="bll" ,orientation='horizontal')
ax2.plot()
ax1.hist(x1_fsrq, bins=50, range=(11, 21), color='blue', alpha=0.7, label="fsrq" )
ax3.scatter(x1_fsrq, y1_fsrq, s=10, color="blue", alpha=0.4 , label="fsrq")
ax4.hist(df_fromfile.loc[(df_fromfile['CLASS']=="fsrq"), 'PL_Index'], bins=80, range=(1, 3.6), color='blue', alpha=0.7, label="fsrq",orientation='horizontal' )
ax1.set(ylabel= "Numero di sorgenti")
ax3.set(xlabel= 'log(nu_syn [Hz])', ylabel="PL Index")
ax4.set(xlabel="Numero di sorgenti")

for ax in fig.get_axes():
    ax.label_outer()
plt.show()







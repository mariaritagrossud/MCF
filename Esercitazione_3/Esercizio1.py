import pandas as pd
import matplotlib.pyplot as plt

#Leggo il file e creo il DataFrame corrispondente
df_fromfile = pd.read_csv('4FGL_J2202.7+4216_weekly_9_11_2023.csv')
print(df_fromfile.columns)

#Grafico del flusso in funzione del giorno giuliano
plt.plot(df_fromfile['Julian Date'],df_fromfile['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'], ".") #Demarco i punti del grafico
plt.title("Graph")
plt.xlabel("Julian Date [days]")
plt.ylabel("Photon Flux [photons cm-2 s-1]")
plt.show()

#Grafico del flusso in funzione del giorno giuliano con errori
plt.errorbar(df_fromfile['Julian Date'],df_fromfile['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'],yerr=df_fromfile[ 'Photon Flux Error(photons cm-2 s-1)'],fmt=".")
plt.title("Graph with errors")
plt.xlabel("Julian Date [days]")
plt.ylabel("Photon Flux [photons cm-2 s-1]") 
plt.savefig("Fig1_Es1.png", dpi=300) #Salvo il file in formato in png
plt.show()

#Grafico del flusso in funzione del giorno giuliano con errori ed asse logaritmico
plt.errorbar(df_fromfile['Julian Date'],df_fromfile['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'],yerr=df_fromfile[ 'Photon Flux Error(photons cm-2 s-1)'],fmt=".")
plt.title("Graph with errors")
plt.xlabel("Julian Date [days]")
plt.ylabel("Photon Flux [photons cm-2 s-1]") 
plt.yscale("log")
plt.savefig("Fig2_Es1.png", dpi=300) #Salvo il file in formato in png
plt.show()
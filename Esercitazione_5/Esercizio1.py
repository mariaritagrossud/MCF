#Provo funzioni importandole prima
import sys
sys.path.append("/Users/mariarita/Metodi_computazionali/Esercitazione_5")
import somme
print("La somma dei primi 6 numeri naturali è {:}".format(somme.somma(6)[0]))
print("Il prodotto dei primi 4 numeri naturali è {:}".format(somme.somma(4)[1]))
print("La somma delle prime 6 radici è {:}".format(somme.somma_sqrt(6)))
print("La  sommatoria delle potenze con base fino 4 ed esponente 3 è {:}".format(somme.somma_potenze(4,3)))

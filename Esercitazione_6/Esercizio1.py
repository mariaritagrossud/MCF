#Primo esercizio
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from  scipy import integrate
import argparse

def parse_arguments():
    
    parser = argparse.ArgumentParser(description='Esempio utilizzo argarse.',
                                     usage      ='python3 argparse_example.py  --opzione')
    parser.add_argument('-g1', '--opzione1', action='store_true',  help='Grafico v')
    parser.add_argument('-g2', '--opzione2', action='store_true',  help='Grafico x')
    return  parser.parse_args()

#Apro file
file= pd.read_csv('vel_vs_time.csv')
v=file["v"]
t=file["t"]


def main():

    args = parse_arguments()


    if args.opzione1 ==True:
        print("Plotto il grafico delle v")
        #Plotto il grafico della velocità in funzione tempo
        plt.plot(t,v)
        plt.title("Velocità in funzione del tempo")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Velocità (m/s)")
        plt.show()
    
    if args.opzione2 == True:
        print("Plotto il grafico delle x")
        #Plotto il grafico della velocità in funzione tempo
        #Ricavo x
        x=np.empty(0)

        for i in range(0,len(v)):

             #Creo array da dargli
            vel=np.empty(0)
            for j in range (i+1):
                vel=np.append(vel,v[j])
        
    
            distanza=integrate.simpson(vel, dx=0.5) 
            x=np.append(x,distanza)

        plt.plot(t,x)
        plt.title("Spazio in funzione del tempo")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Spazio (m)")
        plt.show()





if __name__ == "__main__":

    main()

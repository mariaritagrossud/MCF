#Esercizio2
import pandas as pd
import matplotlib.pyplot as plt
import math as mt
import numpy as np
from  scipy import integrate
import argparse

def parse_arguments():
    
    parser = argparse.ArgumentParser(description='Esempio utilizzo argarse.',
                                     usage      ='python3 argparse_example.py  --opzione')
    parser.add_argument('-v1', '--opzione1', action='store_true',  help='Periodo per V1')
    parser.add_argument('-v2', '--opzione2', action='store_true',  help='Periodo per V2')
    parser.add_argument('-v3', '--opzione3', action='store_true',  help='Periodo per V3')
    parser.add_argument('-v4', '--opzione4', action='store_true',  help='Periodo per V4')
    parser.add_argument('-all', '--opzione5', action='store_true',  help='Tutti i periodi')
    return  parser.parse_args()

#Visualizzo sistema 
def V_1(k,x):
    return k*x**6

def V_2(k,x):
    return k*x**2

def V_3(k,x):
    return k*x**4

def V_4(k,x):
    return k*abs(x)**3/2

#Dati
xx=np.arange(0,5.05,0.1)
mass=0.5
c=1000



def main():

    args = parse_arguments()


    if args.opzione1 ==True:
        periodo1=np.empty(0)
        
        for i in range (2,len(xx)):
            x_0=xx[i]
            x=xx[0:i]

            #Calcolo array dei punti potenziale
            potenziali=np.empty(0)

            for j in range (0,i):
                f=mt.sqrt(8*mass)/mt.sqrt(V_1(c,x_0)-V_1(c,x[j]))
                potenziali=np.append(potenziali,f)
    
            integrale=integrate.simpson(potenziali,dx=0.1)
            periodo1=np.append(periodo1, integrale)
        
        plt.plot(x[:-1],periodo1)
        plt.title("Andamento del periodo al variare posizione iniziale - V1")
        plt.xlabel("x_0 (m)")
        plt.ylabel("Periodo (s)")
        plt.show()
      
    
    if args.opzione2 == True:
        periodo2=np.empty(0)
    
        for i in range (2,len(xx)):
            x_0=xx[i]
            x=xx[0:i]

            #Calcolo array dei punti potenziale
            potenziali=np.empty(0)

            for j in range (0,i):
                f=mt.sqrt(8*mass)/mt.sqrt(V_2(c,x_0)-V_2(c,x[j]))
                potenziali=np.append(potenziali,f)
    
            integrale=integrate.simpson(potenziali,dx=0.1)
            periodo2=np.append(periodo2, integrale)
        
        plt.plot(x[:-1],periodo2)
        plt.title("Andamento del periodo al variare posizione iniziale - V2")
        plt.xlabel("x_0 (m)")
        plt.ylabel("Periodo (s)")
        plt.show()

    
    if args.opzione3 == True:
        periodo3=np.empty(0)
        
        for i in range (2,len(xx)):
            x_0=xx[i]
            x=xx[0:i]

            #Calcolo array dei punti potenziale
            potenziali=np.empty(0)

            for j in range (0,i):
                f=mt.sqrt(8*mass)/mt.sqrt(V_3(c,x_0)-V_3(c,x[j]))
                potenziali=np.append(potenziali,f)
    
            integrale=integrate.simpson(potenziali,dx=0.1)
            periodo3=np.append(periodo3, integrale)
        
        plt.plot(x[:-1],periodo3)
        plt.title("Andamento del periodo al variare posizione iniziale - V3")
        plt.xlabel("x_0 (m)")
        plt.ylabel("Periodo (s)")
        plt.show()
    
    if args.opzione4 == True:
        periodo4=np.empty(0)
        
        for i in range (2,len(xx)):
            x_0=xx[i]
            x=xx[0:i]

            #Calcolo array dei punti potenziale
            potenziali=np.empty(0)

            for j in range (0,i):
                f=mt.sqrt(8*mass)/mt.sqrt(V_4(c,x_0)-V_4(c,x[j]))
                potenziali=np.append(potenziali,f)
    
            integrale=integrate.simpson(potenziali,dx=0.1)
            periodo4=np.append(periodo4, integrale)
        
        plt.plot(x[:-1],periodo4)
        plt.title("Andamento del periodo al variare posizione iniziale - V4")
        plt.xlabel("x_0 (m)")
        plt.ylabel("Periodo (s)")
        plt.show()
    
    if args.opzione5==True:

        #Potenziale 1
        periodo1=np.empty(0)
        
        for i in range (2,len(xx)):
            x_0=xx[i]
            x=xx[0:i]

            #Calcolo array dei punti potenziale
            potenziali=np.empty(0)

            for j in range (0,i):
                f=mt.sqrt(8*mass)/mt.sqrt(V_1(c,x_0)-V_1(c,x[j]))
                potenziali=np.append(potenziali,f)
    
            integrale=integrate.simpson(potenziali,dx=0.1)
            periodo1=np.append(periodo1, integrale)
        
    

        #Potenziale 2
        periodo2=np.empty(0)
    
        for i in range (2,len(xx)):
            x_0=xx[i]
            x=xx[0:i]

            #Calcolo array dei punti potenziale
            potenziali=np.empty(0)

            for j in range (0,i):
                f=mt.sqrt(8*mass)/mt.sqrt(V_2(c,x_0)-V_2(c,x[j]))
                potenziali=np.append(potenziali,f)
    
            integrale=integrate.simpson(potenziali,dx=0.1)
            periodo2=np.append(periodo2, integrale)
        
    

        #Potenziale 3
        periodo3=np.empty(0)
        
        for i in range (2,len(xx)):
            x_0=xx[i]
            x=xx[0:i]

            #Calcolo array dei punti potenziale
            potenziali=np.empty(0)

            for j in range (0,i):
                f=mt.sqrt(8*mass)/mt.sqrt(V_3(c,x_0)-V_3(c,x[j]))
                potenziali=np.append(potenziali,f)
    
            integrale=integrate.simpson(potenziali,dx=0.1)
            periodo3=np.append(periodo3, integrale)
        
       

        #Potenziale 4
        periodo4=np.empty(0)
        
        for i in range (2,len(xx)):
            x_0=xx[i]
            x=xx[0:i]

            #Calcolo array dei punti potenziale
            potenziali=np.empty(0)

            for j in range (0,i):
                f=mt.sqrt(8*mass)/mt.sqrt(V_4(c,x_0)-V_4(c,x[j]))
                potenziali=np.append(potenziali,f)
    
            integrale=integrate.simpson(potenziali,dx=0.1)
            periodo4=np.append(periodo4, integrale)
        
        plt.plot(x[:-1],periodo1, label="V1")
        plt.plot(x[:-1],periodo2, label="V2")
        plt.plot(x[:-1],periodo3, label="V3")
        plt.plot(x[:-1],periodo4, label="V4")
        plt.title("Andamento del periodo al variare posizione iniziale ")
        plt.legend()
        plt.xlabel("x_0 (m)")
        plt.ylabel("Periodo (s)")
        plt.show()




    





if __name__ == "__main__":

    main()






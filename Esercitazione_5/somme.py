#Programma in cui sono definite le funzioni di somma, estrazione radice e somma di potenze con esponente comune
import math as mt

def somma(n):
    sum=0
    pd=1
    for i in range (1,n+1) :
        sum=sum+i
        pd=pd*i
    return sum,pd

def somma_sqrt(n):
    sum=0
    for i in range (n+1) :
        sum=sum+mt.sqrt(i)
    return sum

def somma_potenze(n, alfa=1) :
    sum=0
    for i in range (n+1):
        sum=sum+(i**alfa)
    return sum

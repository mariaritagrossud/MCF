//Modulo serie in C
#include <stdio.h>
#include <math.h>

//Definizione funzione ( numeri interi a partire da 2)

int fibonacci(int n){
    double f_n_2=1;
    double f_n_1=1;
    double f_n=1;
    //Trovo dal coefficiente 3 in poi
    for( int i=3; i<=n; ++i){
        f_n_1=f_n;
        f_n = f_n_1+f_n_2;
        f_n_2=f_n_1;
    };
    double rapporto=(f_n/f_n_1);

    return rapporto; 
}

#Scrivete una funzione che sommi tutti gli elementi di una lista*.
#Poi, committate il file in cui l’avete scritta.

#definisco una lista
my_list = [1,2,3,4,5]

#scrivo una funzione che dati sommi i valori contenuti in una lista
def funzione_somma (lista):
    somma = 0
    
    #ciclo per fare la somma degli elemnti della lista
    for item in lista:
        somma = somma + item
    
    return somma

#output della somma (richiamo della variabile)
print ("La somma è: {}".format (funzione_somma (my_list)))
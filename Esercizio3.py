#Scrivete una funzione che sommi tutti i valori delle vendite degli shampoo del file “shampoo_sales.csv”. Poi, committate il file in cui l’avete scritto.

#apro il file
my_file = open ('shampoo_sales.csv', 'r')

#inizializzo le variabili
lista = []
somma = 0

#divido le linee in modo da poter fare la somma
for line in my_file:
    elements = line.split(',')
    
    #rendo i valori della stringa dei numeri
    if elements[0] != "Date":
        mia_lista = float(elements[1])
        lista.append(float(mia_lista))
        somma = somma + mia_lista

#stampo per controllo la lista
print ("La mia lista di dati è: {}\n".format(lista))

#scrivo la funzione di somma
def somma_funz (lista):
    somma_f = 0
    for item in lista:
        somma_f = somma_f + item
    return somma_f

#stampa tramite richiamo della variabile
print ("La somma è (richiamo variabile): {}".format (somma))

#stampa tramite richiamo della funzione
print ("La somma è (richiamo della funzione): {}".format (somma_funz(lista)))

#chiudo il file
my_file.close

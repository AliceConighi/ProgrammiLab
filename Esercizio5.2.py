# Estendete l’oggetto CSVFile chiamandolo NumericalCSVFile e facendo in
# modo che converta automaticamente a numero tutte le colonne tranne
# la prima (della data).
# Poi, aggiungete questi due campi al file “shampoo_sales.csv”:
# e gestite gli errori che verranno generati in modo che le linee vengano
# saltate
# senza bloccare il programma ma che venga stampato a schermo l’errore

class CSVFile():
  
    #inizializzo il nome del file csv
    def __init__ (self, name):
        
        #creo l'attributo "name" che deve contenere il nome
        self.name = name

    def __str__ (self):
        return 'CSVFile "{}"'.format(self.name)
    
    def NumericalCSVFile (self):
        #apro il file
        sales_original = open(self.name)
        
        #inizializzo le linee
        sales_data = []
        sales_value = []

        #stampo prima frase di tutto
        print('Il file "{}" contiene:'.format(self.name))
        
        for line in sales_original:
            
            #ciclo try
            try:
                #divido le linee
                sales_split = line.split (',')
                    
                #ciclo per formare le due liste 
                if sales_split[0] != "Date":
                    sales = sales_split[0]
                    sales_data.append(sales)
                    data = sales
                    sales = float(sales_split[1])
                    sales_value.append(float(sales))
                    value = sales
                    print('[{}] [{}]'.format(data,value))
            
            #gestione degli errori di valore
            except ValueError:
                print('Non posso convertire "{}" in un numero \nquindi verrà usato il valore di default di 0.0'.format(sales_split[1][:-1]))
                print('Ho trovato un errore di VALORE')
                sales_split[1] = 0.0
        
#TESTER
tentativo = CSVFile("shampoo_salesE.csv")
tentativo.NumericalCSVFile()
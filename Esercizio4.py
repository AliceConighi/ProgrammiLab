# Create un oggetto CSVFile che rappresenti un file CSV, e che:
# 1) venga inizializzato sul nome del file csv, e
# 2) abbia un attributo “name” che ne contenga il nome
# 3) abbia un metodo “get_data()” che torni i dati dal file CSV come lista
# di liste, ad es: [ ['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ... ]
# Provatelo sul file “shampoo_sales.csv”.
# Poi, committate il file in cui l’avete scritto.


#creo un oggetto
class CSVFile():
  
    #inizializzo il nome del file csv
    def __init__ (self, name):
        
        #creo l'attributo "name" che deve contenere il nome
        self.name = name

    def __str__ (self):
        return 'CSVFile "{}"'.format(self.name)
    
    #creo il metodo “get_data()”
    def get_data(self):

        #apro il file e divido la stringa
        sales_original = open (self.name)
        
        #inizializzo la lista dei valori di sales
        sales_lista = []
        dates_lista = []

        #faccio il ciclo in cui taglio le stringhe
        for line in sales_original:
            sales = line.split (',')
        
            if sales != 'Date' and sales != 'Sales':
                sale = sales [1] [:-1]
                sales_lista.append(sale)
                data = sales [0]
                dates_lista.append(data)
            print("[{}] [{}]" .format(data, sale))

tentativo = CSVFile("shampoo_sales.csv")
tentativo.get_data()
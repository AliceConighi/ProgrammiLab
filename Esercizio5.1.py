# Modificate l’oggetto CSVFile della lezione precedente in modo che stampi a
# schermo un messaggio di errore se si cerca di aprire un file non esistente.
# Potete fare questo controllo:
# a) nella funzione get_data(), oppure
# b) nell’ __init__() (basta che leggiate la prima riga per vedere se il file   esiste)

class CSVFile():
  
    #inizializzo il nome del file csv
    def __init__ (self, name):
        
        #creo l'attributo "name" che deve contenere il nome
        self.name = name

    def __str__ (self):
        return 'CSVFile "{}"'.format(self.name)
    
    #creo il metodo “get_data()”
    def get_data(self):
        
        try:
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
        except:
            print('hai trovato un errore!!!')

tentativo = CSVFile("shampoo_sale.csv")
tentativo.get_data()
class Dictionary:
    def __init__(self,name, dict=None):
        self.name=name
        self.dict=dict if dict is not None else {} # IN QUESTO MODO POSSO INSERIRE
        # LISTE, DIZIONARI O ALTRO NEL COSTRUTTORE SENZA CHE DIA ERRORE

    def addWord(self, key, value=None):
        value=value if value is not None else []
        flag=True
        for chiave in self.dict:
            if chiave==key:
                self.dict[chiave].extend(value)
                flag=False
        if flag:
            self.dict[key]=value

    def translate(self, key):
        if key in self.dict:
            return self.dict[key]

    def translateWordWildCard(self,wildcard):
        posizione=wildcard.find("?") # CERCA LA POSIZIONE DI UN CARATTERE
        nuova=wildcard.split("?")[0]+wildcard.split("?")[1]
        trovate=[]
        for key in self.dict:
            if nuova==key[0:posizione]+key[posizione+1:]: # TOLGO LA LETTERA NELLA POSIZIONE DEL PUNTO INTERROGATIVO E CONTROLLO SE SIA UGUALE A QUELLA NUOVA
                trovate.extend(self.dict[key])
        return trovate

    def readDictionary(self, filename): # CREATO METODO PER LEGGERE IL DIZIONARIO
        try:
            with open(filename,"r",encoding="utf-8") as file:
                raws=file.readlines()
                for r in raws:
                    raw=r.strip().split(" ")
                    if len(raw)==2:
                        self.dict[raw[0]]=[raw[1]]
                    else:
                        traduzioni=[]
                        for t in range(1,len(raw)):
                            traduzioni.append(raw[t])
                        self.dict[raw[0]]=traduzioni

            file.close()
        except FileNotFoundError:
            print("Nome file ERRATO")
        except Exception as e:
            print("ERRORE durante la lettura del file")
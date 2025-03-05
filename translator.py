from dictionary import Dictionary

class Translator:

    def __init__(self):
        self.dizionario=Dictionary("dictionary.txt",{})

    def printMenu(self):
        print("-"*(len("Translator Alien-Italian")+4))
        print("Translator Alien-Italian")
        print("-" * (len("Translator Alien-Italian") + 4))
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il dizionario")
        print("5. Exit")
        print("-" * (len("Translator Alien-Italian") + 4))

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        if dict==self.dizionario.name:
            self.dizionario.readDictionary(dict) # LEGGO IL DIZIONARIO
            return self.dizionario.dict # RITORNO IL DIZIONARIO

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        parole=entry.strip().split(" ")

        if len(parole)==2:
            self.dizionario.addWord(parole[0],[parole[1]])
            with open(self.dizionario.name, "w", encoding="utf-8") as file:
                for key in self.dizionario.dict:
                    frase = f"{key} "
                    for i in range(0,len(self.dizionario.dict[key])):
                        if i==(len(self.dizionario.dict[key])-1):
                            frase += f"{self.dizionario.dict[key][i]}\n"
                        else:
                            frase+=f"{self.dizionario.dict[key][i]} "
                    file.write(frase)

            print(parole)
        elif len(parole)>2:
            traduzioni=[]
            for i in range(1,len(parole)):
                traduzioni.append(parole[i])
            self.dizionario.addWord(parole[0], traduzioni)

            with open(self.dizionario.name, "w", encoding="utf-8") as file: # SCRITTURA NEL FILE PER AGGIORNARE IL DIZIONARIO
                for key in self.dizionario.dict:
                    frase = f"{key} "
                    for i in range(0,len(self.dizionario.dict[key])):
                        if i==(len(self.dizionario.dict[key])-1):
                            frase += f"{self.dizionario.dict[key][i]}\n" # CONTROLLO PER L'ULTIMA PAROLA
                        else:
                            frase+=f"{self.dizionario.dict[key][i]} "
                    file.write(frase)

            print(parole)

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        if query in self.dizionario.dict:
            return self.dizionario.translate(query)

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        return self.dizionario.translateWordWildCard(query)

    def printDictionary(self,nome):
        if self.dizionario.name==nome:
            return self.dizionario.dict

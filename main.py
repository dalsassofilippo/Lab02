import translator as tr

t = tr.Translator()
t.loadDictionary("dictionary.txt")

while(True):

    t.printMenu()

    txtIn = input() # SCEGLIE L'OPZIONE

    if txtIn.isdigit():

        # Add input control here!

        if int(txtIn) == 1:
            print("Ok,quale parola devo aggiungere?")
            print()
            insert = input()
            parole=insert.strip().split(" ")
            if len(parole)<=1:
                print("ERRORE: non puoi associare nessuna traduzione alla parola aliena")
            else:
                flag=True
                for p in parole:
                    if not p.isalpha(): # CONTROLLO CHE CONTENGA SOLO LETTERE ALFABETICHE E NON ALFANUMERICHE
                        flag=False
                if flag:
                    t.handleAdd(insert)
                    print("Aggiunta!")
                else:
                    print("ERRORE: parole scritte con caratteri non validi")

        if int(txtIn) == 2:
            print("Ok,quale parola devo tradurre?")
            print()
            insert = input()
            flag = True
            if not insert.isalpha():  # CONTROLLO CHE CONTENGA SOLO LETTERE ALFABETICHE E NON ALFANUMERICHE
                flag = False
            if flag:
                print(t.handleTranslate(insert))
                print("Tradotta!")
            else:
                print("ERRORE: parole scritte con caratteri non validi")
        if int(txtIn) == 3:
            print("Ok,quale wildcard devo tradurre?")
            print()
            insert = input()
            flag = True
            if not insert.isalpha() and insert.count("?")!=1:  # CONTROLLO CHE CONTENGA SOLO LETTERE ALFABETICHE E NON ALFANUMERICHE
                flag = False
            if flag:
                print(t.handleWildCard(insert))
                print("Tradotta!")
            else:
                print("ERRORE: parole scritte con caratteri non validi")

        if int(txtIn) == 4:
            print(t.printDictionary("dictionary.txt"))
        if int(txtIn) == 5:
            print()
            print("Uscita eseguita con successo!")
            break
    else:
        print()
        print("RIPROVA: Inserisci un numero da 1 a 5")
        print()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 22:30:32 2022

@author: andrea
"""



scelta = 0
studenti = []

studenti.append({"nome":"Andrea", "cognome":"Ceci", "voti":[]})
studenti.append({"nome":"Giorgia", "cognome":"Sceni", "voti":[]})

while scelta != 5:

    print("1: Inserisci Studente")
    print("2: Aggiungi voto a Studente")
    print("3: Stampa Studente")
    print("4: Calcola Media voti Studente")
    print("5: Esci")
    print(" ")
    try:
        scelta = int(input("Digita la scelta: "))
    except:
        print("\n **** Inserisci una scelta corretta *** \n")

    print(" ")
    
    if scelta == 1:
        nome = input("Inserisci nome studente: ")
        cognome = input("Inserisci cognome studente: ")

        stud_app = {"nome":nome, "cognome":cognome, "voti":[]}

        studenti.append(stud_app)

    trovato = False
    
    if scelta == 2:
        nome = input("INSERIMENTO VOTO - Inserisci nome studente: ")
        cognome = input("INSERIMENTO VOTO - Inserisci cognome studente: ")
        voto = int(input("Inserici voto da inserire: "))
        
        i = 0

        while trovato != True and i < len(studenti):
            if studenti[i]["nome"] == nome and studenti[i]["cognome"] == cognome:
                trovato = True
                studenti[i]["voti"].append(voto)
            #print(i," ",len(studenti))
            i += 1
        
        if trovato is False:
            print("\n*** Studente non trovato *** \n")
        else:
            print("\n Voto inserito\n")

    if scelta == 3:
        for item in studenti:
            print(item)
        
        print(" ")

    if scelta == 4:
        nome = input("Inserisci il nome dello studente: ")
        cognome = input("Inserisci il cognome dello studente: ")

        i = 0

        while i < len(studenti) and trovato != True:

            if studenti[i]['nome'] == nome and studenti[i]['cognome'] == cognome:
                trovato = True
                
                if len(studenti[i]["voti"]) >0:
                    print("\nLa media è:", sum(studenti[i]["voti"]) / len(studenti[i]["voti"]))
                else:
                    print("\nNon sono presenti voti per lo studente selezionato")

            i += 1
            
        print(" ")

        if trovato is False:
            print("\n*** Studente non trovato *** \n")


#print(studenti)
#print(studenti[1]["nome"])
















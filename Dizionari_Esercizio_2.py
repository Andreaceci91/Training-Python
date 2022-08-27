#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 22:30:32 2022

@author: andrea
"""



studenti = {}
scelta = 0

while scelta != 5:
    
    print(" ")
    print("1: Inserisci Studente")
    print("2: Aggiungi voto a Studente")
    print("3: Stampa Studente")
    print("4: Calcola Media voti Studente")
    print("5: Esci")
    print(" ")
    try:
        scelta = int(input("Digita la scelta: "))
    except:
        scelta = 0
        print("\n **** Inserisci una scelta corretta *** \n")


    print(" ")
    
    if scelta == 1:
        nome = input("Inserisci nome studente: ")
        cognome = input("Inserisci cognome studente: ")

        studenti[nome+'-'+cognome] = []

    trovato = False
    
    if scelta == 2:
        nome = input("INSERIMENTO VOTO - Inserisci nome studente: ")
        cognome = input("INSERIMENTO VOTO - Inserisci cognome studente: ")

        # i = 0

        if nome+'-'+cognome in studenti:
            voto = int(input("Inserici voto da inserire: "))
            studenti[nome+'-'+cognome].append(voto)
        else:
            print("Studente non presente")


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
















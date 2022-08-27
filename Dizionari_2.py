#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 21:11:15 2022

@author: andrea
"""

# Dizionari Parte 2 
#Uso e prova dei dizionari


p1 = {}

p1['Nome'] = 'Andrea'
p1['Cognome'] = 'Ceci'
p1['Eta'] = 30

print(p1['Nome'], p1['Eta'])

lista = []

lista.append("Ciao")
lista.append("Bello")


stud = {}

stud['Andrea'] = [1,2,3,4]
stud['Giovanna'] = [5,6,7,8]
print(stud)

#print(prova['lista_1'])
somma = 0

for item in stud.keys():
    app = stud[item]
    for i in range(len(app)):
        somma = somma + app[i]

    print("Media voti", item,':', somma/len(app))
    somma = 0    
        
# Try to do a dictionary list
lista_dic = []
lista_dic = [{'nome':'Andrea', 'cognome':'Ceci','eta':30},
             {'nome':'Giovana','cognome':'Brava','eta':55}]

for item in lista_dic:
    print('Eta =', item['eta'])

# Second test to print a mean of value
stud2 = []
stud2 = [
            {'nome':'Andrea','cognome':'Ceci','voti':[1,1,1,6]},
            {'nome':'Giorgia','cognome':'Sceni','voti':[2,2,2,2]}
          ]

for item in stud2:
    print('Media voti = ', sum(item['voti'])/len(item['voti']))

        
        
print(sum(stud2[0]['voti']))
        
        
        
        
        
        
        
        
        
        
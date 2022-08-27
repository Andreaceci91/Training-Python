# Esercitazione sulle Matrici
'''
lista = [[1,2,3],[4,5,6],[7,8,9]]

print(lista[0][1])
'''

# Esercitazione Matrici riempimento in input

nrighe = int(input("Inserisci numero di righe: "))
ncolonne = int(input("Inserisci numero di colonne: "))

matrice = []
lista = []

for i in range(ncolonne):   
    for j in range(nrighe):
        n = int(input("Numero: "))
        lista.append(n)
    matrice.append(lista)
    lista = []

print(matrice[1])
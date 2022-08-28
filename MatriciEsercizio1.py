# Matrix Exercise

print("The follow program is based on a n*n Matrix\n")
n = int(input("Insert a number of rows\columns of Matrix: "))

nrows = n
ncol = n

mat = []
list_app = []

for i in range(n):
    for j in range(n):
        number = int(input("Number: "))
        list_app.append(number)
    mat.append(list_app)
    list_app = []

mat_sq = []
list_app = []

for i in range(nrows):
    for j in range(ncol):
        number = mat[i][j] * mat[i][j]
        list_app.append(number)
    
    mat_sq.append(list_app)
    list_app = []

print(" ")
print("The square matrix: ")
for item in mat_sq:
    print(item)

sum_tot = 0

for item in mat:
    sum_tot += sum(item)

print("La somma di tutti gli elementi e':", sum_tot)
print(" ")

sum_row  = []

for item in mat:
    print(item)

for item in mat:
    sum_row.append(sum(item))


print(len(sum_row))

i = 0
max = sum_row[0]

while i < len(sum_row):
    if sum_row[i] > max:
        row_count = i
        max = sum_row[i]
    i += 1
        
print('La riga con somma massima è la', row_count+1,'con valore',max)

    

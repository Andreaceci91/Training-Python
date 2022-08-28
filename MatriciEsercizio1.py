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


# print(len(sum_row))

i = 0
max = sum_row[0]

while i < len(sum_row):
    if sum_row[i] > max:
        row_count = i
        max = sum_row[i]
    i += 1
        
print('\nLa riga con somma massima è la', row_count+1,'con valore',max)

print(" ")

if len(mat) > 1:
    max_col = mat[0][0] + mat[1][0]

# print(max_col,"\n")

app = 0
i = 0
j = 0
while i < len(mat):
    
    while j < len(mat):
        app = app + mat[j][i]
        j += 1

    # print("App:", app)
    if app > max_col:
        col_count = j
        max_col = app  

    app = 0
    j = 0
    i += 1

print("La colonna con somma massima e la",col_count,"con valore", max_col)

print("Ciao")
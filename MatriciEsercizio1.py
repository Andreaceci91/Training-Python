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
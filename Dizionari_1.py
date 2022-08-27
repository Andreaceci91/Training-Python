# Dizionari

d = {}

d['Marco'] = 33
d['Claudia'] = 11

print(d)

p = {
     'nome':'Andrea',
     'cognome':'Ceci',
     'AnnoNascita':'1999'}


print(type(p))

print(p['nome'])

if 'Marco' in d:
    d['Marco'] = 55

print("****************")
for k in d.keys():
    print(k,d[k])

del d['Marco']

print("****************")
for k in d.keys():
    print(k,d[k])
    
print('*****************')
#Contro Frequenze valori

x = [1,2,1,2,3]
app = {}

for item in x:
    if item in app:
        app[item] += 1
    else:
        app[item] = 1

print(app)

    
    
    
    
    
    
    
    
    
    
    
    
    
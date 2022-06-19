dato=[0,0,0,1,0,0,0,0,0]
f=False

for i in range(len(dato)):
    if dato[i]==1:
        f=True
        break
if f==False:
    print('No hay vehiculos')
else:
    print('Hay vehiculos')


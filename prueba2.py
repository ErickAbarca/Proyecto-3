from pickle import *

f=open('prueba.dat','r')
line=f.read()
f.close()
lista=eval(line)
print(lista)
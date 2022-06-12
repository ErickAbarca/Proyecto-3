from pickle import *

fk=open('prueba.dat','w')
dato=[27,2500,1000,'mundo',20,5,10,25,1000,2000,5000,10000,20000]

fk.writelines(str(dato))

fk.close()
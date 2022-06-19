from pickle import *
from datetime import datetime

fk=open('parqueo.dat','w')
dato={1:['807580','23:02 17/06/2022',0,0,0,1],2:['25624','20:02 17/06/2022',0,0,0,2],3:['835582','20:02 17/06/2022',0,0,0,3]}
#dato={}

fk.write(str(dato))

fk.close()
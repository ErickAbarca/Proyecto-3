from pickle import *
from datetime import datetime

fk=open('parqueo.dat','w')
dato={1:[807580,datetime(2021,6,1,10,5,2),0,0],2:[25624,datetime(2021,6,1,10,5,2),0,0],3:[835582,datetime(2021,6,1,10,5,2),0,0]}

fk.write(str(dato))

fk.close()
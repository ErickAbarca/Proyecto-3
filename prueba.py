from datetime import datetime


dato={1:[807580,datetime(2021,6,1,10,5,2),0,0],3:[835582,datetime(2021,6,1,10,5,2),0,0]}

for i in range(7+1):
    if i not in dato:
        if i==0:
            pass
        else:
            espacio=i
            break

print(espacio)
from pylab import *
import db


import exceptions

def readData(filename):
    table = []
    fData = open(filename)

    while True:
        line = fData.readline().replace(" ", "").replace("'", "")
        if line == "":
            break
        line = line[:-1] # remove trailing \n
        try:
            q = float(line)
        except exceptions.ValueError:
           break
        table.append(q)
    fData.close()
    return table


x = array(db.list_annee)
y = array(db.list_population)
ylabel("évolution de la population (en milliard)")

xlabel("années")
plot(x,y,'b:o')
show()

    
    

    
    

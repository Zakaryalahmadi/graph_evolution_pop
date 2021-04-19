from pylab import *
import db




x = array(db.list_annee)
y = array(db.list_population)
ylabel("évolution de la population (en milliard)")

xlabel("années")
plot(x,y,'b:o')
show()

    
    

    
    

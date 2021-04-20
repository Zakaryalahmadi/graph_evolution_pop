from pylab import *
from modules import *


evolution_pop = lireDonnee("data/evolution_pop.txt")

taux_croissance = lireDonnee("data/taux_croissance.txt")

list_annee = year_interval(1960, 2019)

x = array(list_annee)

subplot(211)  
title("évolution de la population en milliard par an")
y = array(evolution_pop)
plot(x,y,'b:o')


subplot(212) 

y = array(taux_croissance)
ylabel("taux de croissance en %")
xlabel("années")
plot(x,y,'b:o')

show()

    
    

    
    

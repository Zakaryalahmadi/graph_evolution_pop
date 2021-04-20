import pylab
from modules import * 


pop_list = md.lireDonnee("data/evolution_pop.txt")



list_annee = md.year_interval(1960, 2020)

  
x = array(list_annee)
y = array(pop_list)
ylabel("évolution de la population (en milliard)")

xlabel("années")
plot(x,y,'b:o')
show()

    
    

    
    

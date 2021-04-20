from pylab import *
from modules import *


pop_list = lireDonnee("data/evolution_pop.txt")



list_annee = year_interval(1960, 2019)

  
x = array(list_annee)
y = array(pop_list)
ylabel("population en millard")

xlabel("années")
plot(x,y,'b:o')
show()

    
    

    
    

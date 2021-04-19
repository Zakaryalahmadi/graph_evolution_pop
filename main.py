from pylab import *


# fonction pour importer les donnees qu'il y a dans un fichier
def lireDonnee(nom_fichier):
    table = []
    fData = open(nom_fichier)

    while True:
        line = fData.readline().replace(" ", "").replace("'", "")
        if line == "":
            break
        line = line[:-1] # supprimer le '\n'
        
        q = float(line) 
        
        table.append(q)
    fData.close()
    return table

pop_list = lireDonnee("/home/lahmadi/Téléchargements/evolution_pop.txt")

list_annee = []
annee = 1959
for x in range(60):
  annee += 1
  list_annee.append(annee)
  

  
x = array(list_annee)
y = array(pop_list)
ylabel("évolution de la population (en milliard)")

xlabel("années")
plot(x,y,'b:o')
show()

    
    

    
    

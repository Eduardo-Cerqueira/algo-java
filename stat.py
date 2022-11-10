import random
from tri_bulles import *
from tribubulle import *
from triinsertion import *
from triselectif1 import *

def stat(min:int,max:int,step:int,nbr:int):
    tab = []
    s = 0
    for i in range(min,max):
        tab.append(round(random.uniform(0,50), 2))
    print("Tableau :",tab)
    print("")
    print("Tri à bulles :"), tri_bulle(tab)
    print("Tri à bulles optimisé :") , bubulle(tab)
    print("Tri à insertition :") , triinsertion(tab)
    print("Tri à sélection :"), triselectif1(tab)
    print("Stats :")
    p = min
    while s < len(tab):
        print (p, tab[s])
        if s == 0 and step!=1:
            p=p+step
            s=s+(step-1)
        else:
            p=p+step
            s=s+step

stat(10, 20, 5, 10)

"""
Ecrire une méthode stat (int min, int max, int step, int nbr) qui fait varier la taille des tableaux tirés
au sort de min jusqu’à max en avançant de step à chaque fois. Pour chaque taille, effectuez nbr
générations aléatoires de tableaux et appelez la fonction de tri à tester. Indiquez sur la sortie
standard la taille du tableau suivi du nombre moyen d’opérations effectués, avec une ligne pour
chaque taille. Par exemple pour min = 10, max = 20, step = 5 et nbr = 10 on obtient quelque chose
comme
10 12.3
15 27.4
20 32.4
"""
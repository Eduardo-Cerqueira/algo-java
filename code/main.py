from methodestat import *

print("Comparaison methodes de tri avec des tableaux aléatoires")
print("")
min = int(input("Quelle est la taille minimum des tableaux : "))
max = int(input("Quelle est la taille maximum des tableaux : "))
step = int(input("Combien de écart entre chaque tableau en valeur (ex: si un écart de 10 -> tableau de 10, 20, 30, ...) : "))
nbr = int(input("Nombre de tableaux pour faire une moyenne par taille de tableau : "))
stat(min,max,step,nbr)
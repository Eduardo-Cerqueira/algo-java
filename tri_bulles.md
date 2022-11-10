# Tri à bulles

Debut
Function tri_bulle(tableau)
    déclarer n qui est la longueur du tableau
    tant que i est dans la portée de n
        tant que j est dans la portée de 0 jusqu'à n-i-1
            si tableau[j] > tableau[j+1]
                alors tableau[j] et tableau [j+1] devient égal à tableau[j+1] et tableau[j]
    afficher le tableau

# Tri à bulles optimisé

Debut
Fonction bubulle (tableau)
déclarer tri -> False
Tant que tri == False
    tri -> True
    Pour loop de 0 à taille de tableau-1
        Si tableau position loop > tableau position loop+1
        déclarer v = tableau position loop
        tableau position loop = tableau position loop+1
        tableau position loop+1 = v
        tri -> False
    Fin de Si
Fin de Pour
Afficher tableau
Fin de Fonction
Fin



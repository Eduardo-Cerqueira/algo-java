# Tri à bulles
```
Debut
Function tri_bulle(tableau)
    déclarer n qui est la longueur du tableau
    tant que i est dans la portée de n
        tant que j est dans la portée de 0 jusqu'à n-i-1
            si tableau[j] > tableau[j+1]
                alors tableau[j] et tableau [j+1] devient égal à tableau[j+1] et tableau[j]
            fin de si
        fin de tant que
    fin de tant que
    afficher le tableau
Fin
```

# Tri à bulles optimisé

```
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
```

# Tri à insertion

```
Debut
    Fonction triinsertion(Tableau)
        pour i de Tableau
            declaration p = Tableau incrémentation list avec i
            declaration de m=i-1
            tant que m>=0 et que p < Tableau avec list m
                Tableau avec list m+1 = Tableau list m
                m - 1
            Tableau avec list m+1 = p
            fin tant que
            pour i de Tableau
            affichez Tableau avec list i
Fin
```

# Tri selectif

```
Debut
    Fonction tri_selection(tableau t)
        n ← longueur(t) 
        pour i de 0 à n - 2
            min ← i       
            pour j de i + 1 à n - 1
                si t[j] < t[min], alors min ← j
            fin pour
        si min ≠ i, alors échanger t[i] et t[min]
        fin pour
Fin
```
def triopti(array):
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]

triopti([6, 7, 4, 9, 0, 1, 5, 3, 8, 2])

def tri_bulle(tab):
    n = len(tab)
    # Traverser tous les éléments du tableau
    for i in range(n):
        for j in range(0, n-i-1):
            # échanger si l'élément trouvé est plus grand que le suivant
            if tab[j] > tab[j+1] :
                tab[j], tab[j+1] = tab[j+1], tab[j]
    print(tab)
# Programme principale pour tester le code ci-dessus
tab = [98, 22, 15, 32, 2, 74, 63, 70]
 
tri_bulle(tab)
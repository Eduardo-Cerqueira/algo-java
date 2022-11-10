def tri_bulle(tab):
    etape = 0
    changement = 0
    n = len(tab)
    for i in range(n):
        for j in range(0, n-i-1):
            if tab[j] > tab[j+1] :
                tab[j], tab[j+1] = tab[j+1], tab[j]
                changement += 1
            etape += 1
    return changement
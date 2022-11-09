def bubulle(tab):
    etape = 0
    tri = False
    while(tri == False):
        tri = True
        for loop in range(len(tab)-1):
            if tab[loop] > tab[loop+1]:
                tab[loop], tab[loop+1] = tab[loop+1],tab[loop]
                tri = False
            etape += 1
    print(tab)
    print(etape)
bubulle([6, 7, 4, 9, 0, 1, 5, 3, 8, 2])

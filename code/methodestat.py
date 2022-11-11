import random
from tribulles import *
from tribubulle import *
from triinsertion import *
from triselectif import *

def stat(min:int,max:int,step:int,nbr:int):
    e = min
    while e < max+1:
        tabgen(e, nbr)
        e += step
    

def tabgen(arraysize,nbr:int):
    bulle = []
    totalbulle = 0
    bulleopti = []
    totalbulleopti = 0
    selectif = []
    totalselectif = 0
    insertion = []
    totalinsertion = 0
    i = 0
    for x in range(0,nbr):
        tab = []
        tab1 = []
        tab2 = []
        tab3 = []
        for y in range(0,arraysize):
            tab.append(round(random.uniform(0,100)))
            tab1.append(tab[y])
            tab2.append(tab[y])
            tab3.append(tab[y])
        bulle.append(tri_bulle(tab))
        bulleopti.append(bubulle(tab1))
        insertion.append(triinsertion(tab2))
        selectif.append(triselectif(tab3))
    while i < len(bulle):
        totalbulle += bulle[i]
        totalbulleopti += bulleopti[i]
        totalinsertion += insertion[i]
        totalselectif += selectif[i]
        i += 1
    totalbulle /= len(bulle)
    totalbulleopti /= len(bulleopti)
    totalinsertion /= len(insertion)
    totalselectif /= len(selectif)
    print("Tableau de",arraysize)
    print("")
    print("bulle :",totalbulle)
    print("bulle opti :",totalbulleopti)
    print("insertion :",totalinsertion)
    print("selectif :",totalselectif)
    print("")
import random
from tri_bulles import *
from tribubulle import *
from triinsertion import *
from triselectif import *

def stat(min:int,max:int,step:int,nbr:int):
    e = min
    y = min
    i = min
    p = min
    print("")
    print("Bulle :")
    while e < max+1:
        tabgenbulle(e, nbr)
        e += step
    print("")
    print("Bulle Opti :")
    while y < max+1:
        tabgenbulleopti(y, nbr)
        y += step
    print("")
    print("Insertion :")
    while i < max+1:
        tabgeninsertion(i, nbr)
        i += step
    print("")
    print("Selectif :")
    while p < max+1:
        tabgenselectif(p, nbr)
        p += step
    

def tabgenbulle(arraysize,nbr:int):
    bulle = []
    totalbulle = 0
    i = 0
    for x in range(0,nbr):
        tab = []
        for y in range(0,arraysize):
            tab.append(round(random.uniform(0,100)))
        bulle.append(tri_bulle(tab))
    while i < len(bulle):
        totalbulle += bulle[i]
        i += 1
    totalbulle /= len(bulle)
    print(arraysize,totalbulle)
    
def tabgenbulleopti(arraysize,nbr:int):
    bulleopti = []
    totalbulleopti = 0
    i = 0
    for x in range(0,nbr):
        tab = []
        for y in range(0,arraysize):
            tab.append(round(random.uniform(0,100)))
        bulleopti.append(bubulle(tab))
    while i < len(bulleopti):
        totalbulleopti += bulleopti[i]
        i += 1
    totalbulleopti /= len(bulleopti)
    print(arraysize,totalbulleopti)

def tabgeninsertion(arraysize,nbr:int):
    insertion = []
    totalinsertion = 0
    i = 0
    for x in range(0,nbr):
        tab = []
        for y in range(0,arraysize):
            tab.append(round(random.uniform(0,100)))
        insertion.append(triinsertion(tab))
    while i < len(insertion):
        totalinsertion += insertion[i]
        i += 1
    totalinsertion /= len(insertion)
    print(arraysize,totalinsertion)

def tabgenselectif(arraysize,nbr:int):
    selectif = []
    totalselectif = 0
    i = 0
    for x in range(0,nbr):
        tab = []
        for y in range(0,arraysize):
            tab.append(round(random.uniform(0,100)))
        selectif.append(triselectif(tab))
    while i < len(selectif):
        totalselectif += selectif[i]
        i += 1
    totalselectif /= len(selectif)
    print(arraysize,totalselectif)
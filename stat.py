from tri_bulles import *
from tribubulle import *
from triinsertion import *
from triselectif1 import *

def stat(min:int,max:int,step:int,nbr:int):
    for i in range(n):
        for j in range(min, max-1):
            if tab[j] > tab[j+1] :
                tab[j], tab[j+1] = tab[j+1], tab[j]
    print(tab)

tri_bulle([1,3,1,4654654,456,789,2,3,9,8,6])
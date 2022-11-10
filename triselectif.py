 #  procédure tri_selection(tableau t)
 #    n ← longueur(t) 
 #   pour i de 0 à n - 2
 #       min ← i       
 #       pour j de i + 1 à n - 1
 #          si t[j] < t[min], alors min ← j
 #      fin pour
 #     si min ≠ i, alors échanger t[i] et t[min]
 # fin pour
 # fin procédure

tab = [216, 30, 22, 20, 5, 2, 1, 73]
for i in range(0,len(tab)-1):
  min = i
  for j in range(i+1,len(tab)):
    if tab[j]<tab[min]:
      min = j
  if (min != i):
    tmp = tab[i]
    tab[i] = tab[min]
    tab[min] = tmp
print(tab)
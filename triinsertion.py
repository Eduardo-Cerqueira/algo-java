#debut

        #function triinsertion(Tableau)
                #pour i de Tableau
                        #declaration p =Tableau incrémentation list avec i
                        #declaration de m=i-1
                        #tant que m>=0 et que p <Tableau avec list m
                                #Tableau avec list m+1 = Tableau list m
                                #m - 1
                        #Tableau avec list m+1 = p
                        #fin tant que
                #pour i de Tableau
                        #affichez Tableau avec list i

#tri insertion programmé
def triinsertion(tailleT):
        for i in range(len(tailleT)):
                p = tailleT[i]
                m=i-1
                while m>=0 and p <tailleT[m]:
                        tailleT[m+1]= tailleT[m]
                        m-=1
                tailleT[m+1] = p
                
        for i in range(len(tailleT)):
                
                print(tailleT[i])               
                
#tableau de bord
tailleT = [100,50,30,51,1000,5,400]
triinsertion(tailleT)

                
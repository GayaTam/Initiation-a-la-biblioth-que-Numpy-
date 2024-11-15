import numpy as np 

a = np.array([1,2,3,4])
print(a)
print (type(a))

print (a[0])

#créer un tableau 2D
b = np.array([[1,2,3], [4,5,6]])
print (b)
print (type(b))
print (b[0,1])
print (b[1,1])

#multiplication d'un tableau par un scalaire 

print ("------------------------")
mon_tab = np.array([2.5,7.9,6.3])
print (0.5 * mon_tab)

#operation arithmétique entre les tableaux
print ("---------------------")
Tab_A = np.array([0,5,9])
Tab_B = np.array([2,7,3])
print (Tab_A + Tab_B)
#Rechrche dans un tableau 
tableau = np.arange(1,25)
print ("Afficher les index des nombre devisible par 5 = ",np.where(tableau %5 == 0))
print ("Afficher les valeur -nombres- des divisible par 5 = ", np.extract(tableau%5 ==0, tableau))

# des fonction bien utiles 
print ("------------------------------------------------------")
tab = np.array([5,1,9,3])
print("Tri du tableau croissant = ",np.sort(tab))
print ("La moyenne du tableau = ", np.mean(tab))
print ("La mediane = ", np.median(tab))
print ("Le nombre des valeurs diffrente de zero = ", np.count_nonzero(tab))
matrice = np.array([[1,2,3],[4,5,6]])
print ("matrice = ", matrice)
print ("La transposer de la matrice = ",np.transpose(matrice))

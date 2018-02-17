
##############################
# Listes I
##############################


##############################
# Activité 5 - Tir balistique
##############################

import matplotlib.pyplot as plt
from math import *

def tir_parabolique(x,v,alpha):
    g = 9.81
    alpha = 2*pi/360*alpha  # angle en radians
    y = -1/2 * g / (v * cos(alpha))**2 * x**2  +  tan(alpha) * x
    return y

def liste_abscisse(xmax,n):
    liste_x = []
    for i in range(n+1):
        x = i * xmax/n  
        liste_x.append(x)
    return liste_x    

def liste_trajectoire(xmax,n,v,alpha):
    liste_y = []
    for i in range(n+1):
        x = i * xmax/n  
        y = tir_parabolique(x,v,alpha)
        liste_y.append(y)
    return liste_y

liste_x = liste_abscisse(270,100)
tir30 = liste_trajectoire(270,100,50,30)
tir45 = liste_trajectoire(270,100,50,45)
tir60 = liste_trajectoire(270,100,50,60)
plt.plot(liste_x,tir30,color="blue")
plt.plot(liste_x,tir45,color="red")
plt.plot(liste_x,tir60,color="green")
plt.grid()
plt.show()

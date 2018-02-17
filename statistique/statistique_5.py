
##############################
# Statistique - Visualisation de données - tkinter
##############################


##############################
# Activité 5 - Visualisation des données (bis)
##############################


##################################################
## Question 1 ##

from random import *

def cours_bourse(n):
    """ Simulation de n jours de bourse """
    val = 1000
    liste_val = [val]
    for i in range(n-1):
        val = val + randint(-10,12)/3
        liste_val = liste_val + [val]

    return liste_val


# Test
print(cours_bourse(100)) 


##################################################
## Question 2 ##

def graphique_point(liste):
    """ Affiche la courbe des cours """
    # Base 1000 en y = 300
    canvas.create_line(100,300,100+365,300,width=3)

    # Coordonnées verticale à gauche
    canvas.create_line(95,420,95,80)   
    for j in range(-1,3):
        canvas.create_line(90,300-100*j,95,300-100*j)
        canvas.create_text(72,300-100*j,text=str(1000+j*100))  

    # Un point par jour    
    for i in range(len(liste)):  
        canvas.create_rectangle(100+i,300+1000-liste[i],100+i+1,300+1000-liste[i],outline="red")

    return


# Fenêtre tkinter
from tkinter import *
root = Tk()      
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

# Test
liste = cours_bourse(365)
# graphique_point(liste)
# root.mainloop()


##################################################
## Question 3 ##

def moyenne_mobile(liste,duree):
    """ Calcule la moyenne mobile """
    moy_mob = []
    for i in range(len(liste)-duree+1):
        moy = sum(liste[i:i+duree])/duree
        moy_mob = moy_mob + [moy]

    return moy_mob


# Test
liste = [1,2,3,4,5,6]
print(liste)
print(moyenne_mobile(liste,2))


####################################################
## Question 4 ##

def graphique_moyenne_mobile(liste):
    """ Affiche les moyennes mobiles à 7 et 30 jours """
    # moyenne 7 derniers jours
    moyenne_7 = moyenne_mobile(liste,7) 
    for i in range(len(moyenne_7)):  
        canvas.create_rectangle(100+i+6,300+1000-moyenne_7[i],100+i+6+1,300+1000-moyenne_7[i],outline="blue")

    # moyenne 30 derniers jours
    moyenne_30 = moyenne_mobile(liste,30)   
    for i in range(len(moyenne_30)):  
        canvas.create_rectangle(100+i+29,300+1000-moyenne_30[i],100+i+29+1,300+1000-moyenne_30[i],outline="sienna")

    return


# Test
liste = cours_bourse(365)
graphique_point(liste)           # Le cours au jour le jour
graphique_moyenne_mobile(liste)  # La moyenne à 7 et 30 jours
root.mainloop()
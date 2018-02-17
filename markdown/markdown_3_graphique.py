

##############################
# Visualiseur de texte - Markdown
##############################

##############################
# Activité 3 - Justification
##############################

from random import randint
longueurs = [randint(5,15) for i in range(50)] 
#longueurs = [14, 3, 16, 9, 2, 11, 13, 5, 4, 19, 16, 6, 17, 16, 15, 5, 14, 12, 17, 7]
longueurs = [8, 11, 9, 14, 8, 8, 15, 10, 14, 11, 15, 15, 5, 12, 9, 9, 15, 10, 14, 5, 12, 8, 8, 13, 10, 11, 8, 13, 7, 5, 6, 11, 7, 7, 13, 6, 6, 9, 8, 12, 5, 8, 7, 6, 6, 15, 13, 11, 7, 12]

longueur_ligne = 100
longueur_espace = 1


##############################
# Version graphique
##############################

from tkinter import *
from tkinter.font import Font


# Fenêtre tkinter
root = Tk()
        
canvas = Canvas(root, width=900, height=600, background="white")
canvas.pack(fill="both", expand=True)

# Format de la page de texte
echelle = 6
largeur = longueur_ligne * echelle
hauteur = 250

# Cadre
canvas.create_rectangle(100,120,100+largeur,100+hauteur,width=2)


## Question 0 ##  

## Coupures comme avec Markdown : dès que l'on dépasse

################################################
def coupures_depasse(long):

    coupures = [0]

    i = 0
    somme  = 0
    while i < len(long):
        
        somme += long[i]

        if somme >= longueur_ligne:
            coupures += [i+1]
            somme = 0

        i += 1

    coupures += [len(long)]

    return coupures 


################################################
def afficher_coupures_depasse():
    print("\n--- Coupures dès que l'on dépasse la fin de ligne ---")
    print("Longueurs des mots :",longueurs)

    coupures = coupures_depasse(longueurs)   
    print("coupures",coupures)

    for i in range(len(coupures)-1):
        ligne = longueurs[coupures[i]:coupures[i+1]]
        somme = sum(ligne)
        print("\nLigne",i,":",ligne,"\nIndices",coupures[i],"à",coupures[i+1]-1,"= longueur[",coupures[i],":",coupures[i+1],"]","\nSomme =",somme,"Reste =",longueur_ligne-somme,)

    return




# Test
# afficher_coupures_depasse()

################################################
def afficher_ligne(ligne,posy,espace):
    posx = 100
    for long in ligne:
        canvas.create_rectangle(posx,posy,posx+long*echelle,posy+20,width=2,outline='red')
        canvas.create_text(posx+5,posy+4,anchor=NW,text=str(long),fill="blue")

        posx = posx + long*echelle + espace*echelle

        nb_espaces = len(ligne)-1
        somme = sum(ligne)+nb_espaces*espace

        canvas.create_text(100+largeur+50,posy+4,anchor=NW,text="somme = "+str(somme),fill="red")
    return


################################################
def graphique_coupures_depasse():

    coupures = coupures_depasse(longueurs)   

    posy = 150
    for i in range(len(coupures)-1):
        ligne = longueurs[coupures[i]:coupures[i+1]]
        afficher_ligne(ligne,posy,0)
        posy  += 30
    root.mainloop()
    return

# Test
graphique_coupures_depasse()


## Question 1 ##

################################################
def coupures_simples(long):

    coupures = [0]

    i = 1
    while i < len(long):
        somme = long[i-1]


        while (i < len(long)) and (somme <= longueur_ligne):
            somme +=  long[i]
            i += 1

        if somme > longueur_ligne:
            coupures +=  [i-1]

    coupures += [len(long)]

    return coupures  




################################################
def afficher_coupures_simples():
    print("\n--- Coupures sans espaces ---")
    print("Longueurs des mots :",longueurs)

    coupures = coupures_simples(longueurs)   
    print("coupures",coupures)

    for i in range(len(coupures)-1):
        ligne = longueurs[coupures[i]:coupures[i+1]]
        somme = sum(ligne)
        print("\nLigne",i,":",ligne,"\nIndices",coupures[i],"à",coupures[i+1]-1,"= longueur[",coupures[i],":",coupures[i+1],"]","\nSomme =",somme,"Reste =",longueur_ligne-somme,)

    return

# Test
#afficher_coupures_simples()





################################################
def graphique_coupures_simples():

    coupures = coupures_simple(longueurs)   

    posy = 150
    for i in range(len(coupures)-1):
        ligne = longueurs[coupures[i]:coupures[i+1]]
        afficher_ligne(ligne,posy,0)
        posy  += 30
    root.mainloop()
    return

# Test
# graphique_coupures_simples()




## Question 2 ##

################################################
def coupures_espaces(long):

    coupures = [0]

    i = 1

    while i < len(long):
        somme = long[i-1]

        while (i < len(long)) and (somme <= longueur_ligne):
            somme +=  longueur_espace + long[i]
            i += 1

        if somme > longueur_ligne:
            coupures +=  [i-1]            

    coupures += [len(long)]

    return coupures  



################################################
def afficher_coupures_espaces():
    print("\n--- Coupures avec espaces ---")
    print("Longueurs des mots :",longueurs)

    coupures = coupures_espaces(longueurs) 
    print("Coupures :",coupures)

    for i in range(len(coupures)-1):
        ligne = longueurs[coupures[i]:coupures[i+1]]
        nb_espaces = len(ligne)-1       
        somme =  sum(ligne) + nb_espaces*longueur_espace      
        print("\nLigne",i,":",ligne,"\nIndices",coupures[i],"à",coupures[i+1]-1,"= longueur[",coupures[i],":",coupures[i+1],"]","\nSomme avec espaces =",somme,"Reste =",longueur_ligne-somme,)

    return

# Test 
#afficher_coupures_espaces()

################################################
def graphique_coupures_espaces():

    coupures = coupures_espaces(longueurs)   

    posy = 150
    for i in range(len(coupures)-1):
        ligne = longueurs[coupures[i]:coupures[i+1]]
        afficher_ligne(ligne,posy,longueur_espace)
        posy  += 30
    root.mainloop()
    return

# Test
# graphique_coupures_espaces()


## Question 3 ##

################################################
def calcul_longueur_espaces(long,coupures):

    longueur_espaces_ligne = []
    
    for i in range(len(coupures)-2):

        ligne = long[coupures[i]:coupures[i+1] ] 
        nb_espaces = len(ligne)-1
        somme =  sum(ligne) + nb_espaces*longueur_espace
        restant = longueur_ligne - somme
        
        if nb_espaces > 0:
            nouvel_espace = longueur_espace + restant / nb_espaces
        else:
            nouvel_espace = longueur_espace

        longueur_espaces_ligne += [nouvel_espace]

    # Dernière ligne du paragraphe pas justifiée
    longueur_espaces_ligne += [longueur_espace] 

    return longueur_espaces_ligne



################################################
def afficher_calcul_longueur_espaces():


    print("\n--- Coupures avec espaces et justification ---")
    print("Longueurs des mots :",longueurs)

    coupures = coupures_espaces(longueurs) 
    print("Coupures :",coupures)

    longueur_espaces_ligne = calcul_longueur_espaces(longueurs,coupures)
    print("Longueur des espaces de chaque ligne :",[float("{0:0.2f}".format(l)) for l in longueur_espaces_ligne])

    for i in range(len(coupures)-1):
        ligne = longueurs[coupures[i]:coupures[i+1]]
        nb_espaces = len(ligne) - 1     
        somme =  sum(ligne) + nb_espaces*longueur_espaces_ligne[i]   

        print("\nLigne",i,":",ligne,"\nIndices",coupures[i],"à",coupures[i+1]-1,"= longueur[",coupures[i],":",coupures[i+1],"]","\nSomme avec espaces =",somme,"Reste =",longueur_ligne-somme,)
        print("Longueur espace de cette ligne",longueur_espaces_ligne[i])

    return

# Test
#afficher_calcul_longueur_espaces()



################################################
def graphique_coupures_justification():

    coupures = coupures_espaces(longueurs)
    longueur_espaces_ligne = calcul_longueur_espaces(longueurs,coupures) 

    posy = 150
    for i in range(len(coupures)-1):
        ligne = longueurs[coupures[i]:coupures[i+1]]
        afficher_ligne(ligne,posy,longueur_espaces_ligne[i])
        posy  += 30
    root.mainloop()
    return

# Test
# graphique_coupures_justification()


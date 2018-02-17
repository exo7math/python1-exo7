
##############################
# Statistique - Visualisation de données - tkinter
##############################


##############################
# Activité 2 - Visualisation des données
##############################


##############################
## Question 0 ##

from math import *
from random import *
from tkinter import *

# Fenêtre tkinter
root = Tk()
        
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

def une_couleur():
    """ Renvoie une couleur au hasard
    Entrée : rien
    Sortie : une couleur """    

    # Méthode 1 - Choix limité
    # couleurs = ["red","orange","yellow","green","cyan","blue","violet","purple"]
    # coul = random.choice(couleurs)

    # Méthode 2 - Choix "infini"
    R = randint(0,255)    
    V = randint(0,255)    
    B = randint(0,255)
    coul = '#%02x%02x%02x' % (R, V, B)

    return coul



##################################################
## Question 1 ##

def graphique_barres(liste):
    """Graphique avec une barre par élément de la liste"""
    posx = 100
    for x in liste:
        hauteur = x * echelle
        canvas.create_rectangle(posx,400,posx+10,400-hauteur,fill="red")
        posx = posx + 30

    # Bonus : Coordonnées verticales à gauche
    max_liste = max(liste)
    canvas.create_line(90,400,90,400-echelle*max_liste)   
    for j in range(max_liste+1):
        canvas.create_line(85,400-echelle*j,90,400-echelle*j)
        canvas.create_text(80,400-echelle*j,text=str(j)) 

    return


# Test
# echelle = 20
# liste = [5,8,6,3,7,10,4]
# graphique_barres(liste)
# root.mainloop()


##################################################
## Question 2 ##

def graphique_cumulatif(liste):
    """Graphique avec rectangles superposés"""
    bas = 500
    for x in liste:
        hauteur = x * echelle
        canvas.create_rectangle(100,bas,200,bas-hauteur,fill=une_couleur())
        bas = bas - hauteur

    # Bonus : Coordonnées verticales à gauche
    max_liste = sum(liste)
    canvas.create_line(90,500,90,500-echelle*max_liste)   
    for j in range(0,max_liste+1,5):
        canvas.create_line(85,500-echelle*j,90,500-echelle*j)
        canvas.create_text(80,500-echelle*j,text=str(j)) 
    
    return


# Test
# echelle = 5
# liste = [5,8,6,3,7,10,4,12]
# graphique_cumulatif(liste)
# root.mainloop()

##################################################
## Question 3 ##

def graphique_pourcentage(liste):
    """Graphique rectangulaire divisé en sous-rectangles"""
    somme = sum(liste)
    posx = 100
    for x in liste:
        largeur = x/somme*100 * 5
        canvas.create_rectangle(posx,300,posx+largeur,200,fill=une_couleur())
        posx = posx + largeur

    # Bonus : Coordonnées horizontales en dessous
    canvas.create_line(100,325,600,325)   
    for i in range(0,11):
        canvas.create_line(100+i*50,325,100+i*50,330)
        canvas.create_text(100+i*50,340,text=str(i*10)+"%") 
    return    

# Test
# echelle = 5
# liste = [5,8,6,3,7,10,4,12]
# graphique_pourcentage(liste)
# root.mainloop()

##################################################
## Question 4 ##

def graphique_secteurs(liste):
    """Graphique en camenbert"""
    somme = sum(liste)
    debut_angle = 0
    for x in liste:
        angle = x/somme*360 
        canvas.create_arc(200,100,550,450,start=debut_angle,extent=angle,style=PIESLICE,fill=une_couleur())
        debut_angle = debut_angle + angle
    return


# Test
# echelle = 5
# liste = [5,8,6,3,7,10,4,12]
# graphique_secteurs(liste)
# root.mainloop()

##################################################
## Question 5 ##

longueurs = [randint(5,15) for i in range(103)] 

liste = [15,8,6,13,17,10,14,12]

def action_bouton1():
    global echelle
    echelle = 15
    canvas.delete("all")
    graphique_barres(liste)
    return

def action_bouton2():
    global echelle
    echelle = 4
    canvas.delete("all")
    graphique_cumulatif(liste)
    return

def action_bouton3():
    canvas.delete("all")
    graphique_pourcentage(liste)
    return

def action_bouton4():
    canvas.delete("all")
    graphique_secteurs(liste)
    return

def nouvelle_liste():
    """Génère une nouvelle liste aléatoire"""
    global liste
    n = randint(3,10)
    liste = [randint(1,20) for i in range(n)] 
    canvas.delete("all")   
    return    

# Titre
root.title("Visualisation de données")

# Boutons
bouton_quitter = Button(root,text="Quitter", width=8, command=root.quit)
bouton_quitter.pack(side=BOTTOM, padx=5, pady=20)

bouton_changer = Button(root,text="Changer les données", width=30, command=nouvelle_liste)
bouton_changer.pack(side=BOTTOM, padx=5, pady=20)

bouton1 = Button(root,text="Graphique en barres", width=30, command=action_bouton1)
bouton1.pack(padx=5, pady=20)

bouton2 = Button(root,text="Graphique cumulatif", width=30, command=action_bouton2)
bouton2.pack(padx=5, pady=20)

bouton3 = Button(root,text="Graphique en pourcentage", width=30, command=action_bouton3)
bouton3.pack(padx=5, pady=20)

bouton4 = Button(root,text="Graphique en secteurs", width=30, command=action_bouton4)
bouton4.pack(padx=5, pady=20)

root.mainloop()

##############################
# Graphes et combinatoire de Ramsey
##############################



##############################
# Activité 2 - Affichage graphique
##############################


from tkinter import *
from math import *
from tkinter.font import Font


from ramsey_1 import *  # Pour les exemples

# Fenêtre tkinter
root = Tk()

canvas = Canvas(root, width=800, height=500, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)


# Echelle 
echelle = 200

##################################################
# Un graphe 

## Question 1 ##

# Version basique (recalcule plein de fois la même chose)
##################################################
def afficher_graphe_basic(graphe):
    """
    Affiche un graphe à l'écran
    Entrée : un graphe
    Sortie : rien (affichage à l'écran)
    """    
    n = len(graphe)

    # Arêtes
    for j in range(n):
        for i in range(n):
            xi = 2*echelle + cos(2*i*pi/n)*echelle
            yi = 1.5*echelle + sin(2*i*pi/n)*echelle
            xj = 2*echelle + cos(2*j*pi/n)*echelle
            yj = 1.5*echelle + sin(2*j*pi/n)*echelle        
            if graphe[i][j] == 0:
                canvas.create_line(xi,yi,xj,yj,width=4,fill="red") 
            if graphe[i][j] == 1:
                canvas.create_line(xi,yi,xj,yj,width=4,fill="green") 

    # Sommets                 
    for i in range(n):
        x = 2*echelle + cos(2*i*pi/n)*echelle
        y = echelle + sin(2*i*pi/n)*echelle
        canvas.create_oval(x-5,y-5,x+5,y+5,fill="black")

    return


# Version optimale 
##################################################
def afficher_graphe(graphe):
    """
    Affiche un graphe à l'écran
    Entrée : un graphe
    Sortie : rien (affichage à l'écran)
    """    
    n = len(graphe)  # Nombre de sommets

    # Liste des coordonnées (x,y) des sommets
    coord = [(2*echelle + cos(2*i*pi/n)*echelle,1.2*echelle + sin(2*i*pi/n)*echelle) for i in range(n)]

    # Arêtes
    for j in range(n):
        for i in range(j+1,n):  # i>j
            if graphe[i][j] == 0:
                canvas.create_line(coord[i],coord[j],width=4,fill="red",dash=(6, 2)) 
            if graphe[i][j] == 1:
                canvas.create_line(coord[i],coord[j],width=4,fill="green")

    mafonte = Font(family="Courier", weight="bold",size=18)
     # Sommets                  
    for i in range(n):
        x,y = coord[i]
        canvas.create_oval(x-15,y-15,x+15,y+15,fill="black")
        canvas.create_text(x,y,text=str(i),font=mafonte,fill="white")

    # Numéro


    return

# Lancement de la fenêtre 
if __name__ == '__main__':
    bouton_quitter = Button(root,text="Quitter", width=8, command=root.quit)
    bouton_quitter.pack(side=BOTTOM, padx=5, pady=20)

    # Test d'un exemple
    afficher_graphe(exemple_graphe_2)
    root.mainloop()


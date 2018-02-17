
##############################
# Jeu de la vie
##############################


##############################
# Rappels - Activité 1
##############################

n, p = 5, 8;
tableau = [[0 for j in range(p)] for i in range(n)] 

# Clignotant
tableau[2][2] = 1
tableau[2][3] = 1
tableau[2][4] = 1


##############################
# Activité 2 - Affichage graphique
##############################

##################################################
## Question 1 ##

from tkinter import *

# Fenêtre tkinter
root = Tk()

canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

# Echelle 
echelle = 100


def afficher_lignes():
    """ Affiche la grille à l'écran """    

    for i in range(n+1):
        canvas.create_line(0,i*echelle,p*echelle,i*echelle)

    for j in range(p+1):
        canvas.create_line(j*echelle,0,j*echelle,n*echelle)
        
    for i in range(n):
        canvas.create_text(echelle//3,i*echelle+echelle//2,text=str(i)) 

    for j in range(p):        
        canvas.create_text(j*echelle+echelle//2,echelle//3,text=str(j)) 

    return


##################################################
## Question 2 ##

def afficher_tableau(tab):
    """ Affiche un tableau à l'écran
    Entrée : un tableau à deux dimension
    Sortie : rien (affichage à l'écran) """    

    for i in range(n):
        for j in range(p):
            if tab[i][j] != 0:
                canvas.create_rectangle(j*echelle,i*echelle,(j+1)*echelle,(i+1)*echelle,fill="red")
        
    return


# Boutons
def action_bouton_afficher():
    canvas.delete("all")
    afficher_lignes()
    afficher_tableau(tableau)
    return


bouton_quitter = Button(root,text="Quitter", width=8, command=root.quit)
bouton_quitter.pack(side=BOTTOM, padx=5, pady=20)

bouton_afficher = Button(root,text="Afficher", width=30, command=action_bouton_afficher)
bouton_afficher.pack(side=BOTTOM, padx=5, pady=20)

# Test
afficher_lignes()
# afficher_tableau(tableau)
root.mainloop()





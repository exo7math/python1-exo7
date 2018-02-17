
##############################
# Aléatoire - Idées
##############################

from random import *
from tkinter import *
import time 

##############################
# Activité 1 - Faire tourner des blocs
##############################

n = 10   # nb de lignes
p = 10   # nb de colonnes 
bord = min(n,p)//5  # distance au bord

tableau = [[0 for j in range(p)] for i in range(n)]

tableau[(n-1)//2][(p-1)//2] = 1  # Centre


##################################################
def voir_tableau():

    for i in range(n):
        for j in range(p):
            print(tableau[i][j], end="")
        print()

    return

# voir_tableau()   

    
##################################################
def est_libre(i,j):
    # if tableau[i][j]:   # sur un bloc existant
    #     return False

    if i>0 and tableau[i-1][j]:   # au dessus
        return False

    if i<n-1 and tableau[i+1][j]:  # en-dessous
        return False

    if j>0 and tableau[i][j-1]:   # à gauche
        return False

    if j<p-1 and tableau[i][j+1]:  # à droite
        return False

    return True

##################################################
def est_dedans(i,j):
    if (0 <= i < n) and (0 <= j < p):
        return True
    else:
        return False 


##################################################
def lancer_un_bloc():
    i = randint(0+bord,n-1-bord)
    j = randint(0+bord,p-1-bord)

    while est_dedans(i,j) and est_libre(i,j):
        dx = randint(-1,1)
        dy = randint(-1,1)
        i = i + dx
        j = j + dy

    if est_dedans(i,j):
        tableau[i][j] = 1

    return i,j


##################################################
def lancer_des_blocs(k):
    # voir_tableau()
    # print()
    for __ in range(k):
        lancer_un_bloc()
        # voir_tableau()
        # print()

    return

lancer_des_blocs(5)



##############################
# Activité 2 - Affichage tkinter statique
##############################

n = 170   # nb de lignes
p = 200   # nb de colonnes

bord = min(n,p)//10  # distance au bord pour lancement
echelle = 5

tableau = [[0 for j in range(p)] for i in range(n)]

tableau[(n-1)//2][(p-1)//2] = 1  # Centre

nb_blocs = 500

root = Tk()  

canvas = Canvas(root, width=p*echelle, height=n*echelle, background="white")
canvas.pack(fill="both", expand=True)


def afficher_tableau():
    canvas.delete("all")   # Efface tout

    for i in range(n):
        for j in range(p):
            if tableau[i][j]:
                canvas.create_rectangle(j*echelle,i*echelle,j*echelle+echelle-1,i*echelle+echelle-1,width=1,fill='green')
    return


def action_bloc():
    lancer_des_blocs(nb_blocs)
    afficher_tableau()

    return

bouton_bloc = Button(root,text="Lancer des blocs", width=20, command=action_bloc)
bouton_bloc.pack(pady=10)

bouton_quitter = Button(root,text="Quitter", width=20, command=root.quit)
bouton_quitter.pack(side=BOTTOM, pady=10)

root.mainloop()


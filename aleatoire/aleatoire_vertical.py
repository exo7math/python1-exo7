
##############################
# Aléatoire
##############################

from random import *
from tkinter import *
import time 

##############################
# Activité 1 - Faire tomber des blocs
##############################

n = 4   # nb de lignes
p = 6   # nb de colonnes 

tableau = [[0 for j in range(p)] for i in range(n)]

tableau[3][3] = 1
tableau[3][2] = 1
tableau[2][2] = 1
tableau[1][2] = 1
tableau[0][4] = 1

##################################################
def voir_tableau():

    for i in range(n):
        for j in range(p):
            print(tableau[i][j], end="")
        print()

    return

voir_tableau()   

    
##################################################
def peut_tomber(i,j):
    if i == n-1:      # tout en bas
        return False

    if tableau[i+1][j]:  # case juste en-dessous
        return False
    
    if j>0 and tableau[i][j-1]:   # à gauche
        return False

    if j<p-1 and tableau[i][j+1]:  # à droite
        return False

    return True


##################################################
def faire_tomber_un_bloc(j):
    # j = nouveau_bloc()
    i = 0
    while peut_tomber(i,j):
        i = i + 1

    tableau[i][j] = 1

    return i,j


##################################################
def faire_tomber_des_blocs(k):
    # voir_tableau()
    # print()
    for __ in range(k):
        j = randint(0,p-1)
        faire_tomber_un_bloc(j)
        # voir_tableau()
        # print()

    return


# faire_tomber_des_blocs(7)
# print()
# voir_tableau()


# exit()

##############################
# Activité 2 - Affichage tkinter statique
##############################

n = 125   # nb de lignes
p = 250   # nb de colonnes 

tableau = [[0 for j in range(p)] for i in range(n)]

echelle = 5  # échelle 
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

# Test
# afficher_tableau()

def action_bloc():
    faire_tomber_des_blocs(nb_blocs)
    afficher_tableau()

    return

bouton_bloc = Button(root,text="Afficher blocs", width=20, command=action_bloc)
bouton_bloc.pack(pady=10)

bouton_quitter = Button(root,text="Quitter", width=20, command=root.quit)
bouton_quitter.pack(side=BOTTOM, pady=10)

root.mainloop()


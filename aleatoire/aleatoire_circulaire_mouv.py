
##############################
# Aléatoire - Idées
##############################

from random import *
from tkinter import *
import time 

##############################
# Rappels de l'activité 1
##############################
    
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

##############################
# Activité 3 - Affichage tkinter dynamique
##############################


n = 20   # nb de lignes
p = 20   # nb de colonnes

bord = min(n,p)//10  # distance au bord pour lancement
echelle = 20
tempo = 20 # milli-secondes

tableau = [[0 for j in range(p)] for i in range(n)]

tableau[(n-1)//2][(p-1)//2] = 1  # Centre

termine = False # est-ce que le bord est atteint

root = Tk()  

canvas = Canvas(root, width=p*echelle, height=n*echelle, background="white")
canvas.pack(fill="both", expand=True)

def deplacer_bloc():
    global i,j,tableau,bloc

    if est_dedans(i,j) and est_libre(i,j): 
        dx = randint(-1,1)
        dy = randint(-1,1)
        tableau[i][j] = 0
        i = i + dx
        j = j + dy
        if est_dedans(i,j):
            # print('coucou')
            tableau[i][j] = 1    
            canvas.coords(bloc,j*echelle,i*echelle,j*echelle+echelle-1,i*echelle+echelle-1)
            canvas.after(tempo,deplacer_bloc)
        else:
            canvas.delete(bloc)



def lancer_un_bloc():
    global i,j,bloc,tableau,termine

    i = randint(0+bord,n-1-bord)
    j = randint(0+bord,p-1-bord)
    bloc = canvas.create_rectangle(j*echelle,i*echelle,j*echelle+echelle-1,i*echelle+echelle-1,width=1,fill='green')

    deplacer_bloc()
    return


def action_bloc():
    # Affichage centre
    i = (n-1)//2
    j = (p-1)//2
    canvas.create_rectangle(j*echelle,i*echelle,j*echelle+echelle-1,i*echelle+echelle-1,width=1,fill='green')

    lancer_un_bloc()

    return


bouton_bloc = Button(root,text="Lancer un bloc", width=20, command=action_bloc)
bouton_bloc.pack(pady=10)

bouton_quitter = Button(root,text="Quitter", width=20, command=root.quit)
bouton_quitter.pack(side=BOTTOM, pady=10)

root.mainloop()






##############################
# Aléatoire - Idées
##############################

from random import *
from tkinter import *
import time 

##############################
# Activité 1 - Rappels
##############################


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



##############################
# Activité 3 - Affichage tkinter dynamique
##############################

n = 50   # nb de lignes
p = 100  # nb de colonnes 
echelle = 10
tableau = [[0 for j in range(p)] for i in range(n)]

tempo = 100 # milli-secondes

liste_blocs = []

termine = False # est-ce que le haut est ateint

root = Tk()  

canvas = Canvas(root, width=p*echelle, height=n*echelle, background="white")
canvas.pack(fill="both", expand=True)


def descendre_les_blocs():
    global tableau, liste_blocs, termine
    new_list_blocs = []  # seulement les blocs qui bougent
    for n in range(len(liste_blocs)):
        i,j,bloc = liste_blocs[n]
        if peut_tomber(i,j):
            tableau[i][j] = 0
            i = i + 1
            tableau[i][j] = 1
            canvas.coords(bloc,j*echelle,i*echelle,j*echelle+echelle-1,i*echelle+echelle-1)
            liste_blocs[n] = (i,j,bloc)
            new_list_blocs = new_list_blocs + [(i,j,bloc)]
        else:
            if i == 0:
                termine = True
    #print('blocs',liste_blocs)
    #print('new',new_list_blocs)
    list_blocs = new_list_blocs[:]
    return


def action_bloc():

    global liste_blocs
    i = 0
    j = randint(0,p-1)
    bloc = canvas.create_rectangle(j*echelle,i*echelle,j*echelle+echelle-1,i*echelle+echelle-1,width=1,fill='green')
    liste_blocs = liste_blocs + [(i,j,bloc)]
    descendre_les_blocs()
    if not(termine): # si le haut pas atteint
        canvas.after(tempo,action_bloc) # appel après un certain temps
    return

    

bouton_bloc = Button(root,text="Démarrer", width=20, command=action_bloc)
bouton_bloc.pack(pady=10)

bouton_quitter = Button(root,text="Quitter", width=20, command=root.quit)
bouton_quitter.pack(side=BOTTOM, pady=10)

root.mainloop()

# voir_tableau()




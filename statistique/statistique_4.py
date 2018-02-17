
##############################
# Statistique - Visualisation de données - tkinter
##############################


##############################
# Activité 4 - Visualisation des données (bis)
##############################

from math import *
from tkinter import *
from random import *

from statistique_3 import * 


root = Tk()  # Fenêtre tkinter
        
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

echelle = 15  # Echelle pour mieux voir les données

##################################################
##################################################

def diagramme_boite(effectif_notes):
    """ Boîte à moustaches """

    # Graphique en barres
    for i in range(len(effectif_notes)):  # i varie de 0 à 20
        hauteur = effectif_notes[i] * echelle
        canvas.create_rectangle(100+2*i*10,300,100+(2*i+1)*10,300-hauteur,fill="red")
        canvas.create_text(100+2*i*10+5,320,text=str(i),fill="red")

    # Coordonnées verticale à gauche
    max_effectifs = max(effectif_notes)
    canvas.create_line(95,300,95,300-echelle*max_effectifs)   
    for j in range(max_effectifs+1):
        canvas.create_line(90,300-echelle*j,95,300-echelle*j)
        canvas.create_text(85,300-echelle*j,text=str(j))       

    # Passage à une liste
    liste = notes_vers_liste(effectif_notes)

    # Calculs des quartiles & co
    mini = min(liste)
    maxi = max(liste)
    Q1,Q2,Q3 = calcule_quartiles(liste)
    #  Diagramme
    canvas.create_rectangle(100+2*mini*10+5,197,100+2*Q1*10+5,203,fill="blue")  
    canvas.create_rectangle(100+2*Q1*10+5,185,100+2*Q3*10+5,215,width=3,outline="blue")  
    canvas.create_rectangle(100+2*Q2*10+5-2,185,100+2*Q2*10+5+2,215,fill="blue")     
    canvas.create_rectangle(100+2*Q3*10+5,197,100+2*maxi*10+5,203,fill="blue") 

    return


# Test 
effectif_notes = [0,0,0,0,0,1,0,2,0,1,5,1,2,3,2,4,1,2,0,1,0]
diagramme_boite(effectif_notes)
root.mainloop()
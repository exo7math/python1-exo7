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
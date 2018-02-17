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
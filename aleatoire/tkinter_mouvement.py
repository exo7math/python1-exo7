
##############################
# Tkinter - Mouvement
##############################

from tkinter import *

Largeur = 400
Hauteur = 200

root = Tk()     
canvas = Canvas(root, width=Largeur, height=Hauteur, background="white")
canvas.pack(fill="both", expand=True)

# Les coordonnées et la vitesse
x0, y0 = 100,100
dx = +5  # Vitesse horizontale
dy = +2  # Vitesse verticale

# Le rectangle à déplacer
rect = canvas.create_rectangle(x0,y0,x0+20,y0+20,width=2,fill="red")

# Fonction principale
def deplacer():
    global x0, y0, dx, dy

    x0 = x0 + dx  # Nouvelle abscisse
    y0 = y0 + dy  # Nouvelle ordonnée

    canvas.coords(rect,x0,y0,x0+20,y0+20)  # Déplacement

    if x0 < 0 or x0 > Largeur:
        dx = -dx  # Changement de sens horizontal
    if y0 < 0 or y0 > Hauteur:
        dy = -dy  # Changement de sens vertical

    canvas.after(50,deplacer)  # Appel après 50 millisecondes
 
    return
    
# Fonctions pour les boutons
def action_deplacer():
    deplacer()
    return

# Boutons
bouton_couleur = Button(root,text="Déplacer", width=20, command=action_deplacer)
bouton_couleur.pack(pady=10)

bouton_quitter = Button(root,text="Quitter", width=20, command=root.quit)
bouton_quitter.pack(side=BOTTOM, pady=10)

root.mainloop()


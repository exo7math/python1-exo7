
##############################
# Visualisation de données - Statistique
##############################


##############################
# Cours tkinter - Boutons
##############################


from tkinter import *
from random import *

root = Tk()     
canvas = Canvas(root, width=400, height=200, background="white")
canvas.pack(fill="both", expand=True)

def action_bouton():
    canvas.delete("all")        # Efface tout
    couleurs = ["red","orange","yellow","green","cyan","blue","violet","purple"]
    coul = choice(couleurs)      # Couleur au hasard
    canvas.create_rectangle(100,50,300,150,width=5,fill=coul)
    return

bouton_couleur = Button(root,text="Afficher", width=20, command=action_bouton)
bouton_couleur.pack(pady=10)

bouton_quitter = Button(root,text="Quitter", width=20, command=root.quit)
bouton_quitter.pack(side=BOTTOM, pady=10)

root.mainloop()


from tkinter import *
from tkinter.font import Font

# Fenêtre tkinter
root = Tk()
        
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(fill="both", expand=True)

# Format de la page de texte
largeur = 700
hauteur = 500

# Couleurs
couleur_fond = "lightgray"
couleur_texte = "black"

# Cadre
canvas.create_rectangle(10,10,largeur,hauteur,width=2,fill=couleur_fond)

# Fontes
fonte_texte = Font(family="Times", size=12)
fonte_italique = Font(family="Times", slant="italic", size=12)
fonte_gras = Font(family="Times", weight="bold", size=12)
fonte_titre = Font(family="Times", weight="bold", size=20)
fonte_sous_titre = Font(family="Times", weight="bold", size=16)

# Test
canvas.create_text(100,100, text="Vive les maths !",anchor=NW,font=fonte_titre,fill=couleur_texte)
canvas.create_text(200,200, text="Vive Python !",anchor=NW,font=fonte_sous_titre,fill="red")
root.mainloop()
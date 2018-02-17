
##############################
# Visualiseur de texte - Markdown
##############################


##############################
# Cours tkinter
##############################


from tkinter import *
from tkinter.font import Font

# Fenêtre tkinter
root = Tk()
        
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(fill="both", expand=True)

# Fonte
mafonte = Font(family="Times", size=20)

# Le texte
#canvas.create_text(100,100, text="Du texte avec Python !",anchor=NW,font=mafonte,fill="blue")

# Lancement de la fenêtre
#root.mainloop()


##################################################
##################################################

# Bounding box

# Fonte
mafonte = Font(family="Courier", weight="bold",size=20)

# Affiche un texte
montexte = canvas.create_text(300,100, text="Texte dans une boîte",anchor=NW,font=mafonte,fill="red")

# Coordonnées du rectangle (x1,y1,x2,y2)
x1,y1,x2,y2 = canvas.bbox(montexte)

# Un rectangle
canvas.create_rectangle(100,50,250,250,width=2)

# Affichage du cadre
canvas.create_rectangle(x1,y1,x2,y2,width=2)

# Fonte
mafonte = Font(family="Times", size=12)

root.mainloop()

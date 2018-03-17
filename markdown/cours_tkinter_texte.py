
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
mafonte = Font(family="Times", size=30)

# Le texte
canvas.create_text(100,100, text="Du texte avec Python !",anchor=NW,font=mafonte,fill="blue")


# Fonte
mafonte = Font(family="Courier", weight="bold",size=30)

# Affiche un texte
canvas.create_text(100,200, text="Texte en gras",anchor=NW,font=mafonte,fill="black")


# Fonte
mafonte = Font(family="Helvetica", slant="italic",size=30)

# Affiche un texte
canvas.create_text(100,300, text="Texte en italique",anchor=NW,font=mafonte,fill="red")



# Bounding box

# Fonte
mafonte = Font(family="Courier", weight="bold",size=30)

# Affiche un texte
montexte = canvas.create_text(200,400, text="Texte dans une boîte",anchor=NW,font=mafonte,fill="black")

# Coordonnées du rectangle (x1,y1,x2,y2)
x1,y1,x2,y2 = canvas.bbox(montexte)

# Affichage du cadre
canvas.create_rectangle(x1,y1,x2,y2,width=2)


root.mainloop()

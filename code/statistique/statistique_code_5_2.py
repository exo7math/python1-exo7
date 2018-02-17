def graphique_point(liste):
    """ Affiche la courbe des cours """
    
    # Base 1000 en y = 300
    canvas.create_line(100,300,100+365,300,width=3)

    # Coordonnées verticale à gauche
    canvas.create_line(95,420,95,80)   
    for j in range(-1,3):
        canvas.create_line(90,300-100*j,95,300-100*j)
        canvas.create_text(72,300-100*j,text=str(1000+j*100))  

    # Un point par jour    
    for i in range(len(liste)):  
        canvas.create_rectangle(100+i,300+1000-liste[i],100+i+1,300+1000-liste[i],outline="red")

    return

# Fenêtre tkinter
from tkinter import *
root = Tk()      
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

# Test
liste = cours_bourse(365)
graphique_point(liste)
root.mainloop()
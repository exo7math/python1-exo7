
##############################
# Jeu de la vie
##############################


##############################
# Activité 4 - Cours
##############################





##################################################

from tkinter import *

# Fenetre
root = Tk()
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

# Capture des clics de souris
def action_clic_souris(event):
    canvas.focus_set()
    x = event.x
    y = event.y
    print("Clic à x =",x,", y =",y)
    return

# Association clic/action
canvas.bind("<Button-1>", action_clic_souris)

# # Lancement
# root.mainloop()


##################################################

# Mauvaise methode
ma_liste = [1,2,3,4]
copie_liste = ma_liste
copie_liste[1] = 7
print(ma_liste)
print(copie_liste)

# Bonne methode pour les listes
ma_liste = [1,2,3,4]
copie_liste = list(ma_liste)
copie_liste[1] = 7
print(ma_liste)
print(copie_liste)


# Ne marche pas pour les listes de listes 
ma_liste = [[1,2],[3,4],[4,5]]
copie_liste = list(ma_liste)
copie_liste[1][1] = 7
print(ma_liste)
print(copie_liste)

# Pour les listes de listes il faut utiliser 'deepcopy'
from copy import *
ma_liste = [[1,2],[3,4],[4,5]]
copie_liste = deepcopy(ma_liste)
copie_liste[1][1] = 7
print(ma_liste)
print(copie_liste)


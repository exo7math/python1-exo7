
##############################
# Jeu de la vie
##############################

##############################
# Rappels - Activité précédentes
##############################


from tkinter import *

# Fenêtre tkinter
root = Tk()
        
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

# Par défaut : rien
n, p = 25, 25
echelle = 40
# n, p = 8, 5
# echelle = 80

tableau = [[0 for j in range(p)] for i in range(n)] 


##################################################

def nombre_voisins(i,j,tab):
    """ Calcule le nb de voisins de la cellule(i,j)
    Entrée : une cellule dans un tableau à deux dimension
    Sortie : le nb de cellules voisines """ 

    nb = 0
    # Voisin en haut à gauche
    if (i>0) and (j>0) and (tab[i-1][j-1] != 0):
        nb += 1
    # Voisin juste au-dessus
    if (i>0) and (tab[i-1][j] != 0):
        nb += 1
    # Voisin en haut à droite
    if (i>0) and (j<p-1) and (tab[i-1][j+1] != 0):
        nb += 1
    # Voisin juste à gauche
    if (j>0) and (tab[i][j-1] != 0):
        nb += 1
    # Voisin juste à droite
    if (j<p-1) and (tab[i][j+1] != 0):
        nb += 1
   # Voisin en bas à gauche
    if (i<n-1) and (j>0) and (tab[i+1][j-1] != 0):
        nb += 1
    # Voisin juste en-dessous
    if (i<n-1) and (tab[i+1][j] != 0):
        nb += 1
    # Voisin en bas à droite
    if (i<n-1) and (j<p-1) and (tab[i+1][j+1] != 0):
        nb += 1

    return nb

def evolution(tab):
    """ Calcule l'évolution en un jour
    Entrée : un tableau à deux dimension
    Sortie : un tableau à deux dimension """    

    nouv_tab = [[0 for j in range(p)] for i in range(n)]

    for j in range(p):
        for i in range(n):
            # Cellule vivante ou pas ?
            if tab[i][j] != 0:
                cellule_vivante = True
            else:
                cellule_vivante = False

            # Nombres de voisins
            nb_voisins = nombre_voisins(i,j,tab)

            # Règle du jeu de la vie
            if cellule_vivante == True and (nb_voisins == 2 or nb_voisins == 3):
                nouv_tab[i][j] = 1
            if cellule_vivante == False and nb_voisins == 3:
                nouv_tab[i][j] = 1          

    return nouv_tab
   

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


def afficher_tableau(tab):
    """ Affiche un tableau à l'écran
    Entrée : un tableau à deux dimension
    Sortie : rien (affichage à l'écran) """    

    for i in range(n):
        for j in range(p):
            if tab[i][j] != 0:
                canvas.create_rectangle(j*echelle,i*echelle,(j+1)*echelle,(i+1)*echelle,fill="red")
        
    return


##############################
# Activité 4 - Jeu de la vie en entier
##############################

##################################################
## Question 0 ##

# Clignotant
def clignotant():
    """ Définition du clignotant """
    global tableau
    tableau = [[0 for j in range(p)] for i in range(n)] 
    tableau[4][7] = 1
    tableau[4][8] = 1
    tableau[4][9] = 1
    canvas.delete("all")   
    afficher_lignes()   
    afficher_tableau(tableau)
    return


# Vaisseau
def vaisseau():
    """ Définition du vasseau spatial """
    global tableau
    tableau = [[0 for j in range(p)] for i in range(n)] 
    tableau[3][4] = 1
    tableau[3][5] = 1
    tableau[3][6] = 1
    tableau[2][6] = 1
    tableau[1][5] = 1
    canvas.delete("all")    
    afficher_lignes()   
    afficher_tableau(tableau)
    return


# Pentadecathlon
def pentadecathlon():
    """ Définition du pentadecathlon """
    global tableau
    tableau = [[0 for j in range(p)] for i in range(n)] 
    tableau[6][4] = 1
    tableau[6][5] = 1
    tableau[6][7] = 1
    tableau[6][8] = 1    
    tableau[6][9] = 1
    tableau[6][10] = 1
    tableau[6][12] = 1
    tableau[6][13] = 1  
    tableau[5][6] = 1
    tableau[7][6] = 1
    tableau[5][11] = 1
    tableau[7][11] = 1 
    canvas.delete("all")      
    afficher_lignes()                    
    afficher_tableau(tableau)
    return


##################################################
## Question 1 ##

# Boutons

def action_bouton_evolution():
    global tableau
    tableau = evolution(tableau)
    canvas.delete("all")
    afficher_lignes()
    afficher_tableau(tableau)
    return


bouton_quitter = Button(root,text="Quitter", width=8, command=root.quit)
bouton_quitter.pack(side=BOTTOM, padx=5, pady=20)

bouton_afficher = Button(root,text="Évoluer", width=20, command=action_bouton_evolution)
bouton_afficher.pack(side=BOTTOM, padx=5, pady=20)

bouton_clignotant = Button(root,text="Clignotant", width=20, command=clignotant)
bouton_clignotant.pack(side=TOP, padx=5, pady=5)

bouton_vaisseau = Button(root,text="Vaisseau", width=20, command=vaisseau)
bouton_vaisseau.pack(side=TOP, padx=5, pady=5)

bouton_pentadecathlon = Button(root,text="Pentadecathlon", width=20, command=pentadecathlon)
bouton_pentadecathlon.pack(side=TOP, padx=5, pady=5)


# root.mainloop()


##################################################
## Question 2 ##

def allumer_eteindre(i,j):
    """ Commute une cellule """
    global tableau
    if tableau[i][j] == 0:
        tableau[i][j] = 1
    else: 
        tableau[i][j] = 0
    return


def xy_vers_ij(x,y):
    """ Coordonnées (x,y) vers coordonnées (i,j) """
    i = y // echelle
    j = x // echelle
    return i, j


def action_clic_souris(event):
    canvas.focus_set()
    # print("Clic à", event.x, event.y)
    x = event.x
    y = event.y
    allumer_eteindre(*xy_vers_ij(x,y))
    canvas.delete("all")   
    afficher_lignes()    
    afficher_tableau(tableau)
    return

# Liaison clic de souris/action
canvas.bind("<Button-1>",action_clic_souris)

afficher_lignes()
afficher_tableau(tableau)
root.mainloop()
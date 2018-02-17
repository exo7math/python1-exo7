
##############################
# L-système
##############################

from turtle import *


##############################
# Activité 1 - Tracer un L-système
##############################


def trace_lsysteme(mot,angle=90,echelle=1):

    speed("fastest")
    width(2)
    color('blue')
    up()
    goto(-150,-150)
    down()

    for c in mot:
        if c == "A" or c == "B":
            forward(100*echelle)
        if c == "g":
            left(angle)
        if c == "d":
            right(angle) 

    exitonclick()

    return

## Test ##
# trace_lsysteme("AgAdAAdAdA")


##############################
# Activité 2 - Une seule règle : le flocon de Koch
##############################

# Un L-système
# un mot de départ
# des règles de remplacement

##################################################
## Question 1 ##

def remplacer_1(mot,lettre,motif):
    nouv_mot = ""
    for l in mot:
        if l == lettre:
            nouv_mot = nouv_mot + motif
        else:
            nouv_mot = nouv_mot + l

    return nouv_mot

## Test ##
print("--- Remplacer une lettre ---")
mot = "AdAAg"
nouv_mot = remplacer_1(mot,"A","Ag")
print(mot)
print(nouv_mot)


##################################################
## Question 2 ##

def iterer_lsysteme_1(depart,regle,k):
    mot = depart
    lettre = regle[0]
    motif = regle[1]

    for i in range(k):
        mot = remplacer_1(mot,lettre,motif)

    return mot

##################################################
## Question 3 ##

## Flocon de Koch
depart_Koch = "A"
regle_Koch = ("A","AgAdAdAgA")

## Test
for k in range(4):
    print(k,iterer_lsysteme_1(depart_Koch,regle_Koch,k))
    print()

k = 3
mot = iterer_lsysteme_1(depart_Koch,regle_Koch,k)
# trace_lsysteme(mot,echelle=5/3**k)


##################################################
## Question 4 ##

#####################
## Autres exemples ##

#####################
depart = "AdAdAdA"
regle = ("A"," AdAgAgAAdAdAgA")
k = 3
mot = iterer_lsysteme_1(depart,regle,k)
#trace_lsysteme(mot,echelle=0.05)

#####################
depart = "AdAdAdA"
regle = ("A","AgAAdAAdAdAgAgAAdAdAgAgAAgAAdA")
k = 2
mot = iterer_lsysteme_1(depart,regle,k)
#trace_lsysteme(mot,echelle=0.07)

#####################
depart = "AdAdAdA"
regle = ("A","AAdAdAdAdAA")
k = 3
mot = iterer_lsysteme_1(depart,regle,k)
# trace_lsysteme(mot,echelle=0.1)

#####################
depart = "AdAdAdA"
regle = ("A","AAdAddAdA")
k = 3
mot = iterer_lsysteme_1(depart,regle,k)
# trace_lsysteme(mot,echelle=0.1)

#####################
depart = "AdAdAdA"
regle = ("A","AAdAdAdAdAdAgA")
k = 3
mot = iterer_lsysteme_1(depart,regle,k)
# trace_lsysteme(mot,echelle=0.1)

#####################
depart = "AdAdAdA"
regle = ("A","AAdAgAdAdAA")
k = 3
mot = iterer_lsysteme_1(depart,regle,k)
# trace_lsysteme(mot,echelle=0.15)

#####################
depart = "AdAdAdA"
regle = ("A","AdAAddAdA")
k = 3
mot = iterer_lsysteme_1(depart,regle,k)
# trace_lsysteme(mot,echelle=0.15)

#####################
depart = "AdAdAdA"
regle = ("A","AdAgAdAdA")
k = 4
mot = iterer_lsysteme_1(depart,regle,k)
# trace_lsysteme(mot,echelle=0.15)



##############################
# Activité 3 - Deux règles : Triangle de Sierpinski
##############################

##################################################
## Question 1 ##

def remplacer_2(mot,lettre1,motif1,lettre2,motif2):
    nouv_mot = ""
    for l in mot:
        if l == lettre1:
            nouv_mot = nouv_mot + motif1
        elif l == lettre2:
            nouv_mot = nouv_mot + motif2
        else:
            nouv_mot = nouv_mot + l

    return nouv_mot

## Test ##
print("--- Remplacer deux lettres ---")
mot = "AdBgA"
nouv_mot = remplacer_2(mot,"A","ABg","B","Bd")
print(mot)
print(nouv_mot)

# mot1 = remplacer_1(mot,"A","ABg")
# mot2 = remplacer_1(mot1,"B","Bd")
# print(mot2)

##################################################
## Question 2 ##

def iterer_lsysteme_2(depart,regle1,regle2,k):
    mot = depart
    lettre1 = regle1[0]
    motif1 = regle1[1]
    lettre2 = regle2[0]
    motif2 = regle2[1]

    for i in range(k):
        mot = remplacer_2(mot,lettre1,motif1,lettre2,motif2)

    return mot


##################################################
## Question 3 ##

## Triangle de Sierpinski
depart_Sierp = "AdBdB"
regle_Sierp_1 = ("A","AdBgAgBdA")
regle_Sierp_2 = ("B","BB")

## Test
print("--- Sierpinski ---")
for k in range(3):
    print(iterer_lsysteme_2(depart_Sierp,regle_Sierp_1,regle_Sierp_2,k))
    print()

k = 4
mot = iterer_lsysteme_2(depart_Sierp,regle_Sierp_1,regle_Sierp_2,k)
# trace_lsysteme(mot,angle=-120,echelle=5/2**k)

##################################################
## Question 4 ##

#####################
## Autres exemples ##

#####################
## Courbe du dragon
depart_dragon = "AX"
regle_dragon_1 = ("X","XgYAg")
regle_dragon_2 = ("Y","dAXdY")

k = 9
mot = iterer_lsysteme_2(depart_dragon,regle_dragon_1,regle_dragon_2,k)
# trace_lsysteme(mot,echelle=2/k)

#####################
## Variante Sierpinski (angle = 60)
depart = "A"
regle1 = ("A","BdAdB")
regle2 = ("B","AgBgA")
# angle = 60

k = 3
mot = iterer_lsysteme_2(depart,regle1,regle2,k)
# trace_lsysteme(mot,angle=60,echelle=2/k**2)


#####################
## Courbe de Gosper
depart = "A"
regle1 = ("A","AgBggBdAddAAdBg")
regle2 = ("B","dAgBBggBgAddAdB")
k = 3
mot = iterer_lsysteme_2(depart,regle1,regle2,k)
# trace_lsysteme(mot,angle=60,echelle=2/k**2)


##############################
# Activité 4 - Tracer un L-système avec pile
##############################


##################################################
## Question 1 ##

def trace_lsysteme_pile(mot,angle=90,echelle=1):

    speed("fastest")
    width(3)
    color('blue')
    up()
    goto(0,-300)
    down()

    pile = []

    for c in mot:
        if c == "A" or c == "B":
            forward(100*echelle)
        if c == "a":
            up()
            forward(100*echelle)
            down()
        if c == "g":
            left(angle)
        if c == "d":
            right(angle)
        if c == "[":
            pile = pile + [(position(),heading())]
        if c == "]":
            up()
            pos,direc = pile.pop()
            goto(pos)
            setheading(direc)
            down()

    exitonclick()

    return

## Test
# trace_lsysteme_pile("AaAgAA[gAAA][dAA]A",angle=90,echelle=1)
# trace_lsysteme_pile("AgA[gAAA]A[dAA]A",angle=90,echelle=1)

##################################################
## Question 2 ##

# Plante
depart_plante = "gggX"
regle_plante_1 = ("X","A[gX][X]A[gX]dAX")
regle_plante_2 = ("A","AA")


k = 5
mot = iterer_lsysteme_2(depart_plante,regle_plante_1,regle_plante_2,k)
# trace_lsysteme_pile(mot,angle=30,echelle=1/k**(3/2))



#####################
## Exemples avec up-down ##
depart = "AdAdAdA"
regle1 = ("A","AgadAAgAgAAgAagAAdagAAdAdAAdAadAAA")
regle2 = ("a","aaaaaa")
k = 2
mot = iterer_lsysteme_2(depart,regle1,regle2,k)
# trace_lsysteme_pile(mot,echelle=0.1)



#####################
## Autres exemples de plantes ##


# #####################
# angle = 22.5
# F →
depart = "gggA"
regle = ("A","A[gA]A[dA][A]")
k = 4
mot = iterer_lsysteme_1(depart,regle,k)
# trace_lsysteme_pile(mot,angle=30,echelle=0.2)


# #####################
# angle = 20
depart = "A"
regle = ("A","A[gA]A[dA]A")
k = 4
mot = iterer_lsysteme_1(depart,regle,k)
# trace_lsysteme_pile(mot,angle=30,echelle=0.075)

# ####################
# angle = 22.5
depart = "A"
regle = ("A","AAd[dAgAgA]g[gAdAdA]")
k = 3
mot = iterer_lsysteme_1(depart,regle,k)
# trace_lsysteme_pile(mot,angle=30,echelle=0.2)


# #####################
# angle = 25.7
depart = "X"
regle1 = ("X","A[gX]A[dX]AX")
regle2 = ("A","AA")
k = 5
mot = iterer_lsysteme_2(depart,regle1,regle2,k)
# trace_lsysteme_pile(mot,angle=30,echelle=0.07)


# #####################
# angle = 30
depart = "A"
regle1 = ("A","A[dB][gB]")
regle2 = ("B","A[dB]A[gAdB]")
k = 5
mot = iterer_lsysteme_2(depart,regle1,regle2,k)
# trace_lsysteme_pile(mot,angle=30,echelle=0.25)

#####################
# angle = 30
depart = "X"
regle1 = ("X","Ad[[X]gX]gA[gAX]dX")
regle2 = ("A","AA")
k = 4
mot = iterer_lsysteme_2(depart,regle1,regle2,k)
# trace_lsysteme_pile(mot,angle=30,echelle=0.15)




#####################
#####################
# Courbe de Hilbert
# Pour les illustrations de livre
  # \rule{L -> +RF-LFL-FR+}
  # \rule{R -> -LF+RFR+FL-}}
# angle = 30
depart = "X"
regle1 = ("X","gYAdXAXdAYg")
regle2 = ("Y","dXAgYAYgAXd")
k = 4
mot = iterer_lsysteme_2(depart,regle1,regle2,k)
trace_lsysteme_pile(mot,angle=90,echelle=0.15)
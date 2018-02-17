
##############################
# Probablité - Paradoxe de Parrondo
##############################

# Référence : "Paradoxe de Parrondo", La gazette des mathématiciens, juillet 2017

from random import *


##############################
# Activité 1 - Jeu A : premier jeu perdant
##############################

## Question 1 ##

def tirage_jeu_A():
    x = random()
    if x <= 0.49:
        return +1
    else:
        return -1


## Question 2 ##

def gain_jeu_A(N):
    gain = 0
    for i in range(N):
        gain = gain + tirage_jeu_A()

    return gain


## Question 3 ##


def esperance_jeu_A(N):
    esperance = gain_jeu_A(N)/N
    return esperance

# Test
print("--- Jeu A ---")
N = 1000000
print(esperance_jeu_A(N))


##############################
# Activité 2 - Jeu B : premier jeu perdant
##############################

## Question 1 ##

def tirage_jeu_B(g):
    if g%3 == 0:
        x = random()
        if x <= 0.09:
            return +1
        else:
            return -1
    else:
        x = random()
        if x <= 0.74:
            return +1
        else:
            return -1


## Question 2 ##

def gain_jeu_B(N):
    gain = 0
    for i in range(N):
        gain = gain + tirage_jeu_B(gain)

    return gain


## Question 3 ##


def esperance_jeu_B(N):
    esperance = gain_jeu_B(N)/N
    return esperance

# Test
print("--- Jeu B ---")
N = 1000000
print(esperance_jeu_B(N))


##############################
# Activité 3 -  Paradoxe de Parrondo
##############################

## Question 1 ##
def tirage_jeu_AB(g):
    x = random()
    if x < 0.5:
        return tirage_jeu_A()
    else:
        return tirage_jeu_B(g)
    
## Question 2 ##
def gain_jeu_AB(N):
    gain = 0
    for i in range(N):
        gain = gain + tirage_jeu_AB(gain)
    return gain

## Question 3 ##
def esperance_jeu_AB(N):
    esperance = gain_jeu_AB(N)/N
    return esperance

# Test
print("--- Jeu AB ---")
N = 1000000
print(esperance_jeu_AB(N))

##############################
# Piles - Calculatrice polonaise
##############################


##############################
# Rappels - Activité 1
##############################

def empile(element):
    global pile
    pile = pile + [element]
    return None

def depile():
    global pile
    sommet = pile[len(pile)-1]
    pile = pile[0:len(pile)-1]
    return sommet   

def pile_est_vide():
    if len(pile) == 0:
        return True
    else:
        return False

##############################
# Activité 3 - La gare de triage
##############################


def tri_wagons(train):
    """ Trie les wagons rouges/bleus d'un train
    Entrée : un train avec des wagons bleus (nombre) et rouges (lettres)
    Sortie : les wagons triés avec les bleus d'abord et les rouges ensuite
    Action : utilise une pile """
    
    global pile   # Doit être globale pour pouvoir être modifiée
    pile = []

    nouv_train = ""

    for wagon in train.split():
        if wagon.isdigit():   # Wagon bleu directement dans le nouveau train
            nouv_train = nouv_train + wagon + " "
        else:                 # Wagon rouge en attente
            empile(wagon)

    # Tous les wagon bleus sont maintenant rangés
    # On s'occupe des wagons rouges en attente
    while not pile_est_vide():
        wagon = depile()
        nouv_train = nouv_train + wagon + " "

    return nouv_train


# Tests
print("--- Tri rouge/bleu ---")

train = "A 4 C 12"
train_trie = tri_wagons(train)
print(train,' -> ',train_trie)

train = "9 K 8 P 17 L B R 3 10 2 N"
train_trie = tri_wagons(train)
print(train,' -> ',train_trie)
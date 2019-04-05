
##############################
# Fonctions
##############################

##############################
# Activité 4 - Fonctions
##############################

##################################################
## Question 1 ##

def reduction(age): 
    """ Renvoie le pourcentage de réduction en fonction de l'âge """

    if age < 10:
        reduc = 50 
    elif age <= 18:
        reduc = 30
    elif age >= 60:
        reduc = 20
    else:
        reduc = 0

    return reduc


# Test
print("--- Réduction ---")
mon_age = 16 
print("J'ai",mon_age,"ans et ma réduction est de",reduction(mon_age),"%.")


##################################################


def montant(tarif_normal,age):
    """ Calcule le montant dû, en fonction du tarif normal et de l'âge """

    reduc = reduction(age)
    tarif = tarif_normal * (100-reduc)/100

    return tarif

# Test
print("--- Coût total des billets ---")
montant_famille = montant(30,9) + 2*montant(20,16) + 2*montant(35,40)
print(montant_famille)


##################################################
## Question 2 ##


def calcul_est_exact(a,b,reponse):
    """ Teste si le résultat de a*b est correct """

    if reponse == a * b:
        return True
    else:
        return False


# Test
print("--- Test résultat multiplication ---")
print(calcul_est_exact(6,7,42))

def test_multiplication(a,b,lang):
    """ Pose une multiplication en français ou en anglais 
    et affiche si la réponse est correcte ou pas """

    # Phrases en français et en anglais
    if lang == "francais":
        question = "Combien vaut le produit a x b ? "
        reponse_juste = "Bravo !"
        reponse_fausse = "Eh non !"
    
    if lang == "anglais":
        question = "How much is the product a x b? "
        reponse_juste = "Well done!"
        reponse_fausse = "It's wrong!"

    # Interrogation
    print("--- Question ---")
    print("a =",a)
    print("b =",b)
    reponse = int(input(question))

    if calcul_est_exact(a,b,reponse):
        print(reponse_juste)
    else:
        print(reponse_fausse)

    return


# Test
print("--- Quiz multiplication français/anglais ---")
test_multiplication(6,7,"anglais")

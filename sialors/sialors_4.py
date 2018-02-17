
##############################
# Si ... alors ...
##############################

##############################
# Activité 4 - Triangles
##############################


# a,b,c = 3,4,5


##############################
## Question 1 ##

a = 4
b = 5
c = 8
print("Triangle",a,b,c)

# A-t-on a <= b <= c ?

if a <= b and b <= c:
    print("Longueurs dans le bon ordre.")
else:
    print("Longueurs dans le mauvais ordre.")


##############################
## Question 2 ##

# Un triangle peut-il être construit à partir de ces longueurs ?

if a+b >= c:
    print("Un tel triangle existe.")
else:
    print("Un tel triangle n'existe pas.")


##############################
## Question 3 ##

# Le triangle est-il rectangle ?

if a**2 + b**2 == c**2:
    print("Le triangle est rectangle.")
else:
    print("Le triangle n'est pas rectangle.")


##############################
## Question 3 ##

# Le triangle est-il equilatéral ?

if (a == b) and (b == c) and (a == c):
    print("Le triangle est équilatéral.")
else:
    print("Le triangle n'est pas équilatéral.")


##############################
## Question 4 ##

# Le triangle est-il isocèle ?

if (a == b) or (b == c) or (a == c):
    print("Le triangle est isocèle.")
else:
    print("Le triangle n'est pas isocèle.")


##############################
## Question 5 ##

# Tous les angles sont-ils aigus ?

cosalpha = (-a**2 + b**2 + c**2)/(2*b*c)
cosbeta = (a**2 - b**2 + c**2)/(2*a*c)
cosgamma = (a**2 + b**2 - c**2)/(2*a*b)

if (cosalpha >= 0) and (cosbeta >= 0) and (cosgamma >= 0):
    print("Tous les angles sont aigus.")
else:
    print("Tous les angles ne sont pas aigus. (Il existe un angle obtu).")
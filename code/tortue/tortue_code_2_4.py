# Une spirale

color("green")
longueur = 10
for i in range(25):
    forward(longueur)
    left(40)
    longueur = longueur + 10

exitonclick()
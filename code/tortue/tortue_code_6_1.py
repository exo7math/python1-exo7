# Préparation

from turtle import *

tortue1 = Turtle()
tortue2 = Turtle()
tortue3 = Turtle()
tortue4 = Turtle()

tortue1.speed("fastest")
tortue2.speed("fastest")
tortue3.speed("fastest")
tortue4.speed("fastest")

tortue1.color('red')
tortue2.color('blue')
tortue3.color('orange')
tortue4.color('green')

# tortue1.width(5)
# tortue2.width(5)
# tortue3.width(5)
# tortue4.width(5)

tortue1.up()
tortue1.goto(-200,-200)
tortue1.down()

tortue2.up()
tortue2.goto(200,-200)
tortue2.down()

tortue3.up()
tortue3.goto(200,200)
tortue3.down()

tortue4.up()
tortue4.goto(-200,200)
tortue4.down()

print(tortue1.position())
print(tortue1.towards(0,0))
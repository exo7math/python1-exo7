from turtle import *
from math import *

speed("fastest")

n = 100
b = 2
r = 200

for i in range(n):
    up()
    goto(r*cos(2*i*pi/n),r*sin(2*i*pi/n))
    down()
    j = (b*i) % n
    goto(r*cos(2*j*pi/n),r*sin(2*j*pi/n))

exitonclick()
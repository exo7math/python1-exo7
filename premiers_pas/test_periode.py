
##############################
# Premiers pas
##############################

##############################
# Activité 1 - Nombres
##############################

from math import *
epsilon = 10**-8

for n in range(1,1000):
    e = floor(log(n,10))
    m = 10**e * ( 1/n*10**(7) - 1/n )
    p = m - round(m)
    # print(e,n,m,p,1/n)
    if abs(p) < epsilon:
        print("--->",n,1/n)

# Q4
# Premier 1/n avec période 7
print("--- Question 4 ---")
print(1/7)     # Période 6
print(1/239)   # Période 7


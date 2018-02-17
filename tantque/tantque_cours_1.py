
##############################
# Tant que - Booléen - Arithmétiques
##############################

##############################
# Cours 1
##############################


n = 10
while n >= 0:
    print(n)
    n = n - 1


n = 100
p = 1
while p < n:
    p = 2*p
print(p)


def est_paire(n):
    return n%2 == 0


n = 56
while est_paire(n) == True:
    n = n // 2
print(n)
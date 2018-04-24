# Première fonction (pas très maligne)
def ma_fonction_1(n):
    divis = False
    for k in range(n):
        if k*7 == n:
            divis = True
    return divis

# Seconde fonction (plus rapide)
def ma_fonction_2(n):
    if n % 7 == 0:
        return True
    else:
        return False

# Mesure des temps d'exécution
import timeit

print(timeit.timeit("ma_fonction_1(1000)", 
    setup="from __main__ import ma_fonction_1", 
    number=100000))
print(timeit.timeit("ma_fonction_2(1000)", 
    setup="from __main__ import ma_fonction_2", 
    number=100000))

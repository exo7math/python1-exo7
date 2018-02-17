
##############################
# Tant que - Booléen - Arithmétiques
##############################

##############################
# Activité 6 - Conjecture fausse : 1211111... n'est jamais premier
##############################


##############################
# Rappel : activité 2

def est_premier(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False

    d = 3    
    while (n % d != 0) and (d**2 <= n):
        d = d + 2

    if d ** 2 > n:
        return True    
    else:
        return False

       
##############################
## Question 1 ##

def un_deux_un(k):
    """ Calcule un entier 121111... """
    u = 12
    for i in range(k):
        u = 10*u + 1
    return u


# Test 
print("--- 121111.... ---")
u = un_deux_un(10)
print(u) 



##############################
## Question 2 ##

# Conjecture 1211111... n'est jamais premier

def test_premier_un_deux_un(kmax):
    """ Teste si 121111... est premier ou pas """
    for k in range(kmax):
        uk = un_deux_un(k)
        print(uk,est_premier(uk))      
    return


# Test 
print("--- Test conj 121111.... jamais premier ---")
test_premier_un_deux_un(21)

# N'aboutira pas au contre-exemple 
# Les calculs sont trop longs


##############################
## Question 3 ##

def est_presque_premier(n,r):
    """ Teste si n n'a pas de diviseurs <= r """

    if n < 2: return False
    if n == 2: return True    
    if n % 2 == 0: return False

    d = 3    
    while (n % d != 0) and (d ** 2 <= n) and (d <= r):
        d = d + 2

    if (d ** 2 > n) or (d > r):
        return True    
    else:
        return False

# Test 
print("--- Test presque premier ---")
print(est_presque_premier(101,13))

##############################

## Question 4 ##

def test_presque_un_deux_un(kmax):
    """ Teste si 121111... est presque premier """

    n = 12
    for k in range(kmax):
        if est_presque_premier(n,1000000):
            print(k,'Presque premier',n)
        n = 10*n + 1
    return

# Test 
print("--- Test conj 121111.... jamais presque premier ---")
test_presque_un_deux_un(151)
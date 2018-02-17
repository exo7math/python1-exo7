# load("conj_un_deux_un.sage")
##############################
# Conjecture 1211111... n'est jamais premier

def un_deux_un(k):
    u = 12
    for i in range(k):
        u = 10*u + 1
    return u

def test_premier_un_deux_un(kmax):
    for k in range(kmax):
        uk = un_deux_un(k)
        print(k,uk,is_prime(uk))      
    return


# Test 
print("--- Test conj 121111.... jamais premier ---")

test_premier_un_deux_un(140)

print(factor(un_deux_un(34)))
# 


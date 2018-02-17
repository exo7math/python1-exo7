def operation(a,b,op):
    """ Calcule l'opération 'a + b 'ou 'a * b'...
    Entrée : a,b (nombres) et 'op' un ccaractère '+'' ou '*'
    Sortie : le résultat du calcul """
    
    if op == '+':
        return a + b
    if op == '*':
        return a * b


# Tests
print("--- Opérations ---")
a=5 ; b=7
print("La somme de",a,"et",b,"vaut",operation(a,b,'+'))
print("Le produit de",a,"et",b,"vaut",operation(a,b,'*'))
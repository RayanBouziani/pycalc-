import sys

def divisions(a,b):
    resul = a/b 
    return resul

def addition(a,b):
    resul = a + b
    return resul

def soustraction(a,b):
    resul = a - b
    return resul

def multiplication(a, b):
    if b < 0:
        signe = -1  
    else:
        signe = 1
    b = abs(b)

    partie_entiere = int(b)
    partie_decimale = b - partie_entiere

    resultat = 0
    for _ in range(partie_entiere):
        resultat += a

    resultat += a * partie_decimale

    return signe * resultat

op1 = float(sys.argv[1])
operrande = sys.argv[2]
op2 = float(sys.argv[3])


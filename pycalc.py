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
    resul = a *b
    return resul

op1 = float(sys.argv[1])
operrande = sys.argv[2]
op2 = float(sys.argv[3])


if operrande == '+':
    print("Le Résultat est :" ,addition(op1,op2))
elif operrande == "/":
    print("Le Résultat est :" ,divisions(op1,op2))
elif operrande == '-':
    print("Le Résultat est :" ,soustraction(op1,op2))
elif operrande == "*":
    print("Le Résultat est :" ,multiplication(op1,op2))
else:
    print("Erreur Opperande")

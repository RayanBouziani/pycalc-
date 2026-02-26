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

def multiplication(a,b):
    resul = a*b
    return resul

op1 = float(sys.argv[1])
operrande = sys.argv[2]
op2 = float(sys.argv[3])


if operrande == '+':
    print(addition(op1,op2))
elif operrande == "/":
    print(divisions(op1,op2))
elif operrande == '-':
    print(soustraction(op1,op2))
elif operrande == "*":
    print(multiplication(op1,op2))
else:
    print("Erreur Opperande")
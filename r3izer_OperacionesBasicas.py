### METODOS PARA OPERACIONES PYTHON##
def Sumar(a,b):
    return a+b
    
def Restar(a,b):
    return a-b

def Multiplicar(a,b):
    return a*b

def Dividir(a,b):
    if(b!=0):
        return a/b
    else:
        return("La division entre 0 no esta definida")
    
## OPERACIONES BASICAS USANDO METODOS
x = input("Ingrese un numero : ")
y = input("Ingrese un numero : ")
print("OPERACIONES")
print("La suma de X e Y es : " + str(Sumar(x,y)))
print("La resta de X e Y es : " + str(Restar(x,y)))
print("La multiplicacion de X e Y es : " + str(Multiplicar(x,y)))
print("La division de X e Y es : " + str(Dividir(x,y)))

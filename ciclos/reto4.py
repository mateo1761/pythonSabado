import math

opcion = 1
numero = 0

print("***MENU***")
print("1. Encuentre si el numero es multiplo de 2")
print("2. Encuentre la raiz cuadrada del numero")
print("3.Sume 100 al numero ingresado")
print("4. Elevar a la 2 el numero ingresado")

while (opcion != 0):

    opcion = int(input("Digite un numero del menu: "))

    if (opcion == 1):
        numero = int(input('Digite un numero: '))
        if (numero % 2 == 0):
            print(f'El numero {numero} es multiplo de 2')
        else:
            print(f'El numero {numero} no es multiplo de 2')
    elif (opcion == 2):
        numero = int(input('Digite un numero: '))
        print(math.sqrt(numero))
    elif (opcion == 3):
        numero = int(input('Digite un numero: '))
        numero += 100
        print(numero)
    elif (opcion == 4):
        numero = int(input('Digite un numero: '))
        print(pow(numero, 2))
else:
    print('Digite un numero del menu de opciones')

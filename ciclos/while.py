observador = 1

print("**Menu**")
print("0.SALIR")
print("1.SALUDAR")
print("2.DESPEDIR")

while(observador != 0):
    observador=int(input("Digite una opcion: "))

    if(observador == 0):
        print('Salir')
        break
    elif(observador == 1):
        print('Hola')
    elif(observador == 2):
        print('Chao')
    else:
        print('Digite una opcion valida')


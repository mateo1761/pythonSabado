sumaPositive = 0

numerosPositives = int(input('Ingrese un numero: '))
while (numerosPositives > 0):
    numerosPositives = int(input('Ingrese un numero: '))

    if (numerosPositives > 0):
        sumaPositive += numerosPositives

print(f'Valor de numeros positivos: {sumaPositive}')

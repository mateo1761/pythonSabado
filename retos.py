cont_neg = 0

cont_positive = 0

for i in range(20):
    numerosPositives = int(input('Ingrese un numero: '))

    if (numerosPositives < 0):
        cont_neg = cont_neg + 1
    elif (numerosPositives > 0):
        cont_positive = cont_positive + 1

print(f'La cantidad de numeros negativos es de: {cont_neg}')

print(f'La cantidad de numeros positivos es de: {cont_positive}')

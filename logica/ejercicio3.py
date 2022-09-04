numeroUno = int(input('Ingrese un numero: '))

numeroDos = int(input('Ingrese otro numero: '))

if (numeroUno > numeroDos):
    print(f'El numero {numeroUno} es mayor que numero {numeroDos}')
elif (numeroUno < numeroDos):
    print(f'El numero {numeroUno} es menor que numero {numeroDos}')
elif (numeroUno == numeroDos):
    print(f'El numero {numeroUno} y numero {numeroDos} son iguales')
else:
    print(f'Ingrese un valor valido')

salarioMensual = 3500000

valorLicencia = 1500000

licencias = int(input('licencias vendidas: '))

valorLicencia *= licencias

salarioBruto = salarioMensual + valorLicencia

deduciones = (salarioBruto * 5)/100

print(f'El salario mensual del vendedor es de: {deduciones}')

print('Inversor de números')

num = int(input('Entre com um número de 3 dígitos:'))
print('\n-------------------------------------------------------')

c = int(num / 100)
d = int(num % 100 / 10)
u = int(num % 10)

resultado = (u*100) + (d*10) + c
print(f'\nO novo número é {resultado}')
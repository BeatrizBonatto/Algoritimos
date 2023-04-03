print('\nCalculadora de divisão\n------------------------------------------')

val1 = int(input('Digite o dividendo:'))
print(val1)
val2 = int(input('Digite o divisor:'))
print(val2)

quociente = int(val1/val2)
resto = int(val1%val2)

print(f'\n------------------------------------------\nDividendo:{val1}\nDivisor:{val2}\nQuociente:{quociente}\nResto:{resto}')
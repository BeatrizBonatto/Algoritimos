print('Entrar com as notas da PR 1 e PR2 e imprimir a média final:\n')

pr1 = float(input('Digite a primeira nota:'))
pr2 = float(input('Digite a segunda nota:'))

media_final = (pr1+pr2)/2
md_trunc = (media_final - 0.5) + 0.001
md_arrd = int(media_final + 0.001)

print(f'Média truncada ={md_trunc:.2f}\nMédia arredondada ={md_arrd:.2f}')

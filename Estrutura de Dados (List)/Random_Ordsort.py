import random
n = int(input('\nInforme quantos números você quer: '))
inicio = 0
fim = 99
lista = list()
if n > 0:
    for num in range(n):
        lista.append(random.randint(inicio,fim))
    print(f'A lista original é:\n{lista}')
    print('-'*150)
    lista.sort(reverse=True)
    print(f'A lista alterada é:\n{lista}')
else:
    print('Informe um número Positivo!')
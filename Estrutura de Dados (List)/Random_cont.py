import random
n = int(input('Informe quantos numerais você quer: '))
inicio = 0
fim = 9
lista = list()
if n > 0:
    for i in range(n):
        lista.append(random.randint(inicio,fim))
    print(f'\nOs números foram: {lista}')
    print('\nA quantidade de repitação de cada número foi: ')
    for i in range(inicio, fim+1):
        print(f'{i} -> {lista.count(i)}')
    print('\nFIM!')
else:
    print('Informe um Número Positivo!')

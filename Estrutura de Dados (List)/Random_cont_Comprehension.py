import random
n = int(input('Informe quantos numerais você quer: '))
inicio = 0
fim = 9
lista = list()
if n > 0:
    var1 = [lista.append(random.randint(inicio,fim)) for i in range(n)]
    print(f'\nOs números foram: {lista}\n')
    print('\nA quantidade de repitação de cada número foi: ')
    var2 = [print(f'{i} -> {lista.count(i)}') for i in range(inicio,fim+1) ]
    print('\nFIM!')
else: 
    print('Informe um Número Positivo!')
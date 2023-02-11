import statistics
import random
n = int(input('Informe quantos numerais você quer: '))
inicio = 0
fim = 99
lista = list()
if n > 0:
    var1 = [lista.append(random.randint(inicio,fim)) for i in range(n)]
    lista.sort()
    print(f'\nOs números foram: {lista}\n')
    print(f'A média é -> {statistics.mean(lista):.2f}')
    print(f'A médiana é -> {statistics.median(lista):.2f}')
    print(f'A variação é -> {statistics.variance(lista):.2f}')
    print(f'O Desvio é -> {statistics.stdev(lista):.2f}')
else:
    print('Informe um Número Positivo!')
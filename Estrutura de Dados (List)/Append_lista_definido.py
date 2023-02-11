n = int(input('Informe quantos numerais você quer: '))
lista = list()
num = int(input('Informe um número: '))
lista.append(num)
print(lista)
if n > 0:
    while True:
        num = int(input('Informe outro número: '))
        if num == 0: break
        lista.append(num)
        lista.sort()
        if len(lista) > n:
            lista.remove(lista[n])
        print(lista)
else:
    print('Informe um Número Positivo!')
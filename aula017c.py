# Listas: Criando relações ou cópias nas listas

print('\033[1;32mCriando relação: altera uma, altera a outra:\033[m')
a = [3,4,7,5]
b = a
b[2] = 0
print(f'Lista A: {a}')
print(f'Lista B: {b}')

print('\033[1;32m\nCriando uma cópia da lista:\033[m')
a = [3,4,7,5]
b = a [:] # Dessa forma, consideramos toda a lista e criamos uma cópia
b[2] = 0
print(f'Lista A: {a}')
print(f'Lista B: {b}')
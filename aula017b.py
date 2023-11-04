# aula prática

valor = []
"""valor.append(5)
valor.append(3)
valor.append(9)"""
for cont in range (0,5): # vai do 0 até o 4
    valor.append(int(input('Insira um valor: ')))

for c, v in enumerate(valor): # c para chave (posição) e v para valor
    print(f'Eu encontrei na posição {c} o valor {v}!')
print('Final da lista')

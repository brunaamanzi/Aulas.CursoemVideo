# Aula 16: Prática
lanche = ('hambúrger','suco','pizza','pudim')
# uma forma de utilizar o for em tuplas
print('-'*30)
print('\033[1;35mfor comida in lanche:\033[m')
for comida in lanche:
    print(f'Eu comi {comida}')

# outra forma de ter o mesmo resultado e um contator para mostrar a posição do item.
print('-'*30)
print('\033[1;35mfor cont in range (0,len(lanche)):\033[m')
for cont in range (0,len(lanche)):
    print(f'Eu comi {lanche[cont]} na posição {cont}')

# Outra opção quando for necessário utilizar contador:
print('-'*30)
print('\033[1;35mfor pos, comida in enumerate(lanche):\033[m')
for pos, comida in enumerate(lanche):
    print(f'Eu comi {comida} na posição {pos}')

print('-'*30)
print('Eu comi pra caramba!')
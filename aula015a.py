# Aula 15: Interrompendo repetições WHILE
soma = num = 0
while True:
    num = int(input('Insira um número: '))
    if num == 999:
        break
    soma += num
# print('A soma é {}.'.format(soma))
print(f'A soma é {soma}')
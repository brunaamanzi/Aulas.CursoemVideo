# estrutura de repetição for
"""for c in range (0,3):
    print('oi')
    print('*-*')

for c in range (0,7):
    print(c)
print('fim')

n = int(input('Escreva um número: '))
for c in range (0,n+1):
    print(c)
print('fim')

i = int(input('Insira o início: '))
f = int(input('Insira o fim: '))
p = int(input('Insira o passo: '))
for c in range (i,f+1,p):
    print(c)
print('fim')"""

s = 0
for c in range (0,4):
    n = int(input('Insira um número: '))
    s += n
print('o somatório de todos os valores foi {}.'.format(s))
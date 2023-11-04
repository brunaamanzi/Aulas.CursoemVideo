# utilizando a estrutura WHILE
n = 1
impar = par = 0
while n != 0:
    n = int(input('Escreva um número: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Quantidade de números ímpares: {}\nQuantidade de números pares: {}'.format(impar,par))
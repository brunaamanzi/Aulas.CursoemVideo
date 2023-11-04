n1= int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma entre {} e {} vale {}.'.format(n1,n2,n1+n2))
s = n1 + n2
m = n1 + n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} e a divisão é {:.3f}'.format(s,m,d),end='. ')
print('A divisão inteira é {} e a potência é {}.'.format(di,e))
print('escreve algo, \n escreve em outra linha')
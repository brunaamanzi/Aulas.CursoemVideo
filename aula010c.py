n1 = float(input('Qual foi a primeira nota? '))
n2 = float(input('Qual foi a segunda nota? '))
m = (n1+n2)/2
print('Sua média foi {:.1f}.'.format(m))
#if m < 7:
#    print('Você não foi aprovado. Estude mais!')
#else:
#    print('Parabéns, você foi aprovado!')
print('Parabéns, você foi aprovado!' if m>7 else 'Você não foi aprovado. Estude mais!')
# Trabalhando com módulos: import
import math
num = int(input('digite um número: '))
raiz = math.sqrt(num)
# se eu tivesse importado apenas a função sqrt, poderia escrever: raiz = sqrt(num)
print('A raiz quadrada de {} é {}.'.format(num,raiz))
# Outra forma arredondando pra cima:
print('A raiz quadrada de {} é {}.'.format(num,math.ceil(raiz)))


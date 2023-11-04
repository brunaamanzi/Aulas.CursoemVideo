# Aula 21: Escopo de Variáveis
def aula (b): # b recebeu o valor da variável "a" informada mais no cód global
    global a
    a = 8 # redefiniu a
    b += 4 # Nesse caso, b continua considerando o valor original de a (5), pois considera o valor de quando a função é chamada
    c = 2
    print(f'Variável "a" local vale {a}')
    print(f'Variável "b" local vale {b}')
    print(f'Variável "c" local vale {c}')

a = 5
aula(a)
print(f'Variável "a" global vale {a}')
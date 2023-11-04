# Aula 21: Retorno de Resultados
def somar(a=0,b=0,c=0):
    s = a + b + c
    return s # podemos utilizar return para que a função retorne o valor desejado
    #print(f'A soma vale {s}')

n1 = somar(3,2,5)
n2 = somar(3,2)
n3 = somar(2)
print(f'Os resultados foram {n1}, {n2} e {n3}.')
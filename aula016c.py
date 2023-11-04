# tentando mudar uma tupla:

lanche_tupla = ('hambúrger','suco','pizza','pudim','batata frita')
print(sorted(lanche_tupla))
sorted(lanche_tupla)
print(lanche_tupla)

print('-'*30)

a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c)
print(c.count(9)) # para contar quantas vezes um valor aparece
print(c.index(1)) # para verificar a posição de um valor - considerando apenas a 1º ocorrência
# Se tiver dois valores, e quiser verificar após determinada posição:
print(c.index(2,1))

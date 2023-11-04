# Criando funções para realizar soma de 2 números
def lin():
    print('-'*30)
def soma(a,b):
    s = a + b
    print(s)
lin()
soma(2,8)
soma(4,7)
lin()
#Outra forma:
def soma(a,b): # python irá seguir a ordem colocada. se fosse soma(b,a), em soma(3,2) b=3 a=2
    print(f'A = {a}, B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
lin()
soma(a=3,b=5) # pode ser soma(3,5) / soma(b=5,a=3)
lin()

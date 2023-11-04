# Empacotar parâmetros: quando não sabemos quantos números serão inseridos
def lin():
    print('-'*30)
def contador(*num):
    soma = sum(num)
    print(soma)
lin()
contador(2,5,4)
contador(2,7,9,5,3,2,45,7) # podemos inserir quantos números quisermos
lin()
def contador(*num): # empacotamento utilizando for
    for valor in num:
        print(f'{valor} ',end='')
    print('FIM!')

contador(3,4,6,3,1)
contador(21,3,1996)
lin()

def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números!!')

contador(3,2,8,5,3,1,77)




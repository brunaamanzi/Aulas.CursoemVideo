# Aula 20: Funções (parte 1)
def mostralinha():
    print('-'*30)
mostralinha()
print(f'{"Olá, Mundo!":^30}')
mostralinha()

# Podemos inserir o pontilhado, texto e outro pontilhado:
def título(txt):
    print('-'*30)
    print(f'{txt:^30}')
    print('-'*30)

título('Olá, Mundo!')
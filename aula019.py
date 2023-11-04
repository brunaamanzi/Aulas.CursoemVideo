# Aula 19: Dicionários
dados = {'nome': 'Pedro','idade':25,'sexo':'M'}
# Utilizando print formatado:
print(f'O {dados["nome"]} tem {dados["idade"]} anos.')
for k,v in dados.items():
    print(f'O {k} é {v}.')
# Podemos ter dicionários dentro de listas:
lista = [{'nome': 'Pedro','idade':25,'sexo':'M'},{'nome': 'Bruna','idade':24,'sexo':'F'},{'nome': 'Allan','idade':31,'sexo':'M'}]
print(lista[1]['nome'])
print(lista[2]['idade'])

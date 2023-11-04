# Dicionários
"""estado = dict()
brasil = list()
for c in range (0,3):
    estado['uf']=input('Unidade Federativa: ')
    estado['sigla']=input('Sigla do Estado: ')
    brasil.append(estado.copy())
print(brasil)
for e in brasil: # vai imprimir cada dicionário de uma vez
    print(e)

for e in brasil: # vai imprimir dentro de cada dicionário, a chave e o valor guardado
    for k,v in e.items():
        print(f'O campo {k} tem o valor {v}')

print(brasil)"""
brasil = [{'uf': 'bahia', 'sigla': 'ba'}, {'uf': 'pernambuco', 'sigla': 'pe'}, {'uf': 'paraiba', 'sigla': 'pb'}]
for i, e in enumerate(brasil): # vai imprimir dentro de cada dicionário, apenas o valor guardado
    print(f'{i}: {e["uf"]} ({e["sigla"]})')


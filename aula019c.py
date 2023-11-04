# Utilizando enumerate em Dicionários
dicionário = {'a':10,
              'b':5,
              'c':8,
              'd':10}
for i,(k,v) in enumerate(dicionário.items()):
    print(f'Posição {i}, Chave {k}, Valor {v}')

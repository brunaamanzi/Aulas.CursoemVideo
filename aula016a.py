# Aula 16: TUPLAS (Variáveis compostas; Rotinas; Tratamento de Erros)
# Exemplos de fatiamento:
lanche = ('hambúrger','suco','pizza','pudim')
print(lanche)
print(lanche[2]) # para ler apenas o 3º item
print(lanche[0:2]) # para ler do primeiro até o segundo (0 e 1, desconsiderando o 2)
print(lanche[1:]) # para ler do segundo até o final
print(lanche[2:]) # para ler do terceiro até o final
print(lanche[-1]) # para ler o último item
print(lanche[3]) # para ler apenas o 4º item
print(len(lanche)) # para ver nº de itens
print(lanche[-2::-1]) # para inverter a ordem
for c in lanche:
    print(c)
print(lanche[-2::-1]) # para inverter a ordem
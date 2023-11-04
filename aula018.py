# Aula 18: Listas Compostas
# Recriando a lista
"""teste = []
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = []
galera.append(teste)
teste[0]='Maria'
teste[1]=22
galera.append(teste)
print(galera)"""

# Criando uma cópia da lista
teste = []
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = []
galera.append(teste[:])
teste[0]='Maria'
teste[1]=22
galera.append(teste[:])
print(galera)

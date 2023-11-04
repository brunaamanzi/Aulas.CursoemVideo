# Aula 18: Criando Listas Compostas
galera = [['João',19],['Ana',33],['Joaquim',13],['Maria',45]]
"""print(galera[1]) # vai imprimir a primeira lista da lista
print(galera[2][0]) # vai imprimir o primeiro item da terceira lista"""
# Para imprimir apenas os nomes:
for p in galera: # p imprime cada lista dentro da lista
    #print(p[0]) # imprime o primeiro item da primeira lista
    #print(galera[0]) iria imprimir a primeira lista toda
    print(f'{p[0]} tem {p[1]} anos de idade.')

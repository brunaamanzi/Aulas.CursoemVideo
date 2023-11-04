# Aula 17: LISTAS
lista = ['a','o','u','e','i']
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

num = [2,5,9,1]
num[2] = 3 # vai alterar o número da posição 2 (num 9)
num.append(7) # vai inserir ao final da lista o número 7
num.sort(reverse=True)
num.insert(2,2) # insere na posição 2, o número 0.
num.pop()
num.remove(2) # procura do início da lista e elimina a primeira ocorrência
print(len(num)) # quantos elementos tem na lista
print(num)
# Criando listas compostas com append e clear
lista = []
grupo = []
total_maior = total_menor = 0
for c in range (0,3):
    lista.append(str(input('Nome: ')))
    lista.append(int(input('Idade: ')))
    grupo.append(lista[:]) # precisa do [:] para criar uma cópia independente
    lista.clear()
print(grupo)
for p in grupo:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        total_maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        total_menor += 1
print(f'Temos {total_maior} pessoas de maior e {total_menor} pessoas de menor.')
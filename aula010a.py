# aula 10: condições simples e compostas
#condição: executa um bloco ou outro
#if objeto.esquerda():
#    bloco True
#else:
#    bloco False

tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('- FIM -')
# TODO COMANDO QUE ESTIVER COLADO DO LADO ESQUERDO, VAI SER EXECUTADO TODAS AS VEZES.
#outra opção de fazer a condição:
print('carro novo') if tempo <=3 else print('carro velho')
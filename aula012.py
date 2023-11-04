# Condições aninhadas - Estruturas de Controle
# if ... :
# elif ... :
# else ... :

nome = str(input('Qual é o seu nome? ')).title()
if nome == 'Bruna':
    print('Que nome bonito!')
elif nome == 'Bruna' or nome == 'Rebecca' or nome == 'Simone':
    print('Tenho parentes mulheres com esse nome')
elif nome in 'Allan Biagio Vinicius':
    print('Tenho parentes homens com esse nome.')
else: # opcional
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

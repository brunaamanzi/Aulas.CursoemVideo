# Aula 23: Erros e Exceções
"""
try: #operação
except: #falhou #nesse passo, podemos incluir mensagens para cada tipo de erro, especificando qual erro trará a mensagem "except (ValueError,TypeError):","except ZeroDivisionError:"...
else: #deu certo
finally: #deu certo/falhou
"""
"""try: # comando que será executado
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except: # vai aparecer quando o comando der erro
    print('Infelizmente tivemos um problema :(')
else: # vai mostrar quando o comando não der erro
    print(f'O resultado é {r:.1f}')
finally: # mensagem que aparecerá quando der ou não der erro: ou seja, sempre que o programa for finalizado.
    print('Volte sempre! Muito obrigado!')"""


try: # comando que será executado
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro: # vai aparecer quando o comando der erro, mostrando info sobre o erro
    print(f'O problema encontrado foi {erro.__class__}')
else: # vai mostrar quando o comando não der erro
    print(f'O resultado é {r:.1f}')
finally: # mensagem que aparecerá quando der ou não der erro: ou seja, sempre que o programa for finalizado.
    print('Volte sempre! Muito obrigado!')
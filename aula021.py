# Aula 21: Funções - Parte 2
def somar(a=0,b=0,c=0):
    """
    Faz a soma de três valores e mostra o resultado na tela. Os três valores são opcionais.
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    Função criada por Bruna Manzi
    """
    s = a + b + c
    print(f'A soma vale {s}')
somar(3,2,5)
somar()
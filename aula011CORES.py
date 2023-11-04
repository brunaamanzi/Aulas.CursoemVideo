# Cores no Terminal: insere dentro do print \033[ ; ; m
#\033[# insere aqui o código para definir estilo (n,s,i)); insere código para definir cor do texto ; insere código para definir cor de fundo m ]
'''Códigos para ESTILO:
    0 sem estilo;
    1 em negrito;
    4 sublinhado;
    7 inverte config fundo e texto
Códigos para COR:
    30 branco
    31 vermelho
    32 verde
    33 amarelo
    34 azul escuro
    35 roxo
    36 azul claro
    37 cinza
Códigos para FUNDO:
    40 fundo branco
    41 fundo vermelho
    42 fundo verde
    43 fundo amarelo
    44 fundo azul escuro
    45 fundo roxo
    46 fundo azul claro
    47 fundo cinza'''
print('\033[0;33;44m Olá, mundo!')
print('\033[4;35;40m testando\033[m')
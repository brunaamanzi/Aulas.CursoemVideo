def soma(*lista):
    s = 0
    for num in lista:
        s += num
    print(f'A soma dos valores {lista} é {s}')

soma(2,4,6)

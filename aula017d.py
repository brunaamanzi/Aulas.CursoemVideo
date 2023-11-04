# A quem interessar, bisect.insort(lista, n) já insere n na lista de forma ordenada:
import bisect
numbers = []
for i in range(5):
    n = int(input('Type a number: '))
    bisect.insort(numbers, n)
    print(f'Number {n} included in position {numbers.index(n)}')
print(f'Numbers typed: {numbers}')


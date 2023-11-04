# utilizando funções para listas:
def pont():
    print('-'*30)
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

pont()
valores = [2,4,6,8,10]
print(valores)
dobra(valores) # essa função vai modificar a lista valores original
print(valores)
pont()

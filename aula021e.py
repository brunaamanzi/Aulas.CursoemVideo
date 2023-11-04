# Aula 21: Prática
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
print(par(num))
# Print com base em True/False
if par(num):
    print('É par!') # True
else:
    print('Não é par!') # False
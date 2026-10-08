numeros = []

for i in range(8):
    numero = int(input('Digite um número: '))
    numeros.append(numero)

i = 0
while i < len(numeros):
    if (numeros[i] % 2) > 0:
        numeros.pop(i)
        i += 1

print('Numeros pares: ', numeros)

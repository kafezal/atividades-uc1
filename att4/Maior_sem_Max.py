numeros = [1, 5, 34, 90, 23, 43, 2, 3, 44]
maior = numeros[0]

for num in numeros:
    if numeros[num + 1] > maior:
        maior = numeros[num]

print('O maior número é: ', maior)

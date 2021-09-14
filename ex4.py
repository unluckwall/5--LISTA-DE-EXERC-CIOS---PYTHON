#4) Escreva um algoritmo que imprima na tela os números de 0 a 10, com exceção do 7.

n = 0

while n <= 9:
    if n == 6:
        n += 1
    n += 1
    print(n)
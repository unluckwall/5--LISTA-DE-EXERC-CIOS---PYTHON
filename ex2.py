#2) Escreva um algoritmo que receba 10 valores digitados pelo usuário e no final exiba o maior número.

cont = 1
num = 0
mairovalor = 0

while cont <= 10:
    num = int(input('Digite um número :'))
    cont += 1
    if num > mairovalor:
        mairovalor -= mairovalor
        mairovalor = num
print('O maior valor é {}'.format(mairovalor))
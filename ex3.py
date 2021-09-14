#3) Escreva um algoritmo que leia o ano de nascimento de dez pessoas e no final mostre quantas pessoas são maiores de idade.

cont = 1
cont2 = 0
num = 0
maioridade = 18

while cont <= 10:
    num = int(input('Digite sua idade :'))
    cont += 1
    if num >= maioridade:
        cont2 += 1
print('Pessoas maiores de idade {}'.format(cont2))
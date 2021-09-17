#7) Escreva um algoritmo que receba dois números e exiba para o usuário todos os valores
#intermediários a eles, veja exemplo:
#Primeiro número: 5
#Segundo número: 15
#Resultado: 6 7 8 9 10 11 12 13 14

n = int(input('Digite um número :'))
n2 = int(input('Digite outro número :'))

while n < n2:
    print(n)
    n += 1

while  n > n2:
    print(n)
    n -= 1
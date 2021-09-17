#6) Escreva um programa que receba o preço de dois produtos. Calcule um desconto de 8% no primeiro produto, 11% no segundo e apresente o valor final a ser pago.

p1 = int(input('Digite o valor do produto :'))
p2 = int(input('Digite o valor do segundo produto :'))

p1des = (p1 -(p1 * 8)/100)
p2des = (p2 -(p2 * 11)/100)
total = p1des + p2des 

print('O valor total e {}'.format(total))

#5) Escreva um algoritmo para calcular o fatorial de um número. Se o usuário digitou, por exemplo,o valor 5, o resultado a ser exibido pelo algoritmo é: 5! é igual a 120



numero = int(input("Fatorial de: ") )

resultado=1
count=1

while count <= numero:
    resultado *= count
    count += 1

print(resultado)
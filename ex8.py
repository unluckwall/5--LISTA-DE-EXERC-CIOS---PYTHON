#8) Escreva um algoritmo que receba um nome e três notas e atenda exiba uma mensagem
#diferente para cada um dos casos a seguir:
#A) Se a média for maior que 7, exiba a mensagem “Parabéns (nome)! Você foi aprovado”;
#B) Se a média for menor que 7 e maior que 5, exiba a mensagem “Você ficou com média
#(media) e está de recuperação;
#C) Se a média for menor que 5, exiba a mensagem “(Nome), você está reprovado”.


name = str(input('Digite seu nome :'))
n1 = int(input('Insira a 1º nota :'))
n2 = int(input('Insira a 2º nota :'))
n3 = int(input('Insira a 3º nota :'))

media = (n1 + n2 + n3) / 3

if  media >= 7:
    print('Parabéns {}! Você foi aprovado'.format(name))

elif   media < 7 and media >= 5:
    print('Você ficou com média {} e está de recuperação'.format(media))

elif  media < 5:
    print('{}, você está reprovado'.format(name))

"""
Crie um programa que leia um número inteiro
e mostre na tela se ele é PAR ou ÍMPAR.


"""


numero = int(input('Me diga um número qualquer:'))

valor = numero % 2

if valor != 1:
    print('O número {} é PAR'.format(numero))

else:
    print('O número {} é Ímpar'.format(numero))
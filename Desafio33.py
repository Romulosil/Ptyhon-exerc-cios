"""
Faça um programa que leia três e mostre qual
é o maior e qual é o menor.


"""


primeiro = int(input('Primeiro valor:'))
segundo = int(input('Segundo valor: '))
terceiro = int(input('Terceiro valor:'))

maior = primeiro

if segundo > maior:
    maior = segundo

if terceiro > maior:
    maior = terceiro

print('O maior valor digitado foi {}'.format(maior))

menor = primeiro

if segundo < menor:
    menor = segundo

if terceiro < menor:
    menor = terceiro

print('O menor valor digitado foi {}'.format(menor))
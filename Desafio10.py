"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos Dólares ela pode comprar.

Considere US$1,00 = R$4,20

"""

dinheiro = float(input('Quanto dinheiro você tem na carteira? R$'))

dolar = dinheiro / 4.19

print('Com R${:.2f} você pode comprar US${:.2f}'.format(dinheiro, dolar))


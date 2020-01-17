"""
Escreva um programa para aprovar o empréstimo bancário para
compra de uma casa.Pergunte o valor da casa, salário do comprador
e em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.
"""


valorCasa = float(input("Valor da casa : R$"))
salaComprador = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento?"))

prestacao =  valorCasa / (anos *12)
mi = salaComprador * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos'.format(valorCasa, anos), end='')
print('a prestação será de R${:.2f}'.format(prestacao))

if prestacao <= mi:
    print('Empréstimo pode ser CONCEDIDO!')

else:
    print('Empréstimo NEGADO!')

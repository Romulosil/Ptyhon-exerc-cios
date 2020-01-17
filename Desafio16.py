"""
Crie um programa que leia um número Real qualquer pelo teclado
e mostre na tela a sua porção inteira.

Ex:Digite um número:6.127
O número 6.127 tem a parte Inteira 6.
"""



from math  import floor

valor = float(input("Digite um valor:"))
print("O valor digitado foi {} e a sua porção inteira é a {}".format(valor,floor(valor)))


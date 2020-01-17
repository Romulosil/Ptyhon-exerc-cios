"""
Faça um programa que leia um número
inteiro e mostre na tela o seu sucessor
e seu antesessor.


"""

nu = int(input("Digite um número: "))

maior = nu + 1
menor = nu - 1

print('Analisando o valor {} seu antecessor é {} e o sucessor é {}'.format(nu,menor,maior))
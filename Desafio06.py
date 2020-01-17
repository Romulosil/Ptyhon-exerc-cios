"""
Crie um algoritmo que leia um número e
mostre o seu dobro, triplo e raiz quadrada.

"""
import math
numero = int(input("Digite um número: "))
dobro =  numero * 2
tiplo =  numero * 3
raiz =   math.sqrt(numero)

print("O dobro de {} vale {}.".format(numero,dobro))
print("O triplo de {} vale {}.".format(numero, tiplo))
print("A raiz quadrada de {} é igual a {:.2f} .".format(numero, raiz))
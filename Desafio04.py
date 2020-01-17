"""
Faça um programa que leia algo pelo e mostre na
tela o seu tipo primitivo e todas as informações possíveis
sobre ele.

"""

pri = input('Digite algo:')

print('O tipo primitivo desse valor é', type(pri))
print('Só tem espaços? ',pri.isspace())
print('É um número? ',pri.isnumeric())
print('É  alfabético?',pri.isalpha())
print('É alfanumérico?', pri.isalnum())
print('Está em maiúsculas?', pri.isupper())
print('Está em minúsculas?', pri.islower())
print('Está capitalizada?', pri.istitle())
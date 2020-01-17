"""
Faça um program que leia um Ângulo qualquer e mostre
na tela o valor de seno, cosseno e tangente desse ângulo

"""

from math import radians,sin, cos, tan

angulo = float(input("Dgite o ângulo que voçê deseja:"))



print("O ângulo de {:.1f} tem o SENO de {:.2f}".format(angulo, sin(radians(angulo))))
print("O ângulo de {:.1f} tem o COSSENO de {:.2f}".format(angulo,cos(radians(angulo))))
print("O âmgulo de {:.1f} tem a TANGENTE de {:.2f}".format(angulo,tan(radians(angulo))))
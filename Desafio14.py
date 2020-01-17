"""

Eecreva um programa que converta uma temperatura digitada em ºC e converta ºF.

"""

celsius = float(input("Informe a temperatura em ºC:"))

Fahrenheit = (celsius * 1.8) + 32

print("A temperatura de {}ºC corresponde a {:.1f}ºF".format(celsius,Fahrenheit))
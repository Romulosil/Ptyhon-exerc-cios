"""
Faça um algoritmo que leia o salário de um funcionário e mostre
seu novo salário, com 15% de aumento.

"""

saFun  = float(input("Qual é o salário do Funcionário? R$"))

multi = saFun * 15
aumento = saFun + (multi / 100)

print("Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}".format(saFun,aumento))
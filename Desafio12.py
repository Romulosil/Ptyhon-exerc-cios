"""

Faça um algoritmo que leia preço de um produto e mostre seu novo preço, com  5% de desconto.


"""

preço = float(input("Qual é o preço do produto? R$ "))

porcetagem = preço * 5
desconto = preço - (porcetagem /100)

print("O produto que custava R${}, promoção com desconto de 5% vai custar R${:.2f}".format(preço,desconto))
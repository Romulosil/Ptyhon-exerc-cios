"""
Desenvolva um programa que pergunte a distância de uma viagem
em KM.Calcule o preço da passagem, cobrando R$0,50 por KM para
viagens de até 200KM e R$0,45 para viagens mais longas.


"""

distancia = float(input('Qual é distância da sua viagem?'))

duzento = distancia * 0.50
longa = distancia * 0.45


print('Voçê está prestes a começar uma viagem de {:.1f}Km'.format(distancia))

if distancia <= 200:
    print('E o preço da sua passagem será de R${:.2f}'.format(duzento))


else:
    print('E o preço da sua passagem será de R${:.2f}'.format(longa))



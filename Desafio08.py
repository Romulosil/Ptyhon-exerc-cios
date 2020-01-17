"""
Escreva um programa que leia um valor metros e o exiba
convertido em centímetros e milímetros


"""


dis = int(input('Uma distância em metros: '))
print('A medida de {:.1f} corresponde a '.format(dis))
print('{}km'.format(dis/1000))
print('{}hm'.format(dis/100))
print('{}dam'.format(dis/10))
print('{}dm'.format(dis * 10))
print('{}cm'.format(dis * 100))
print('{}mm'.format(dis * 1000 ))

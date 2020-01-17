
from random import randint
from time import sleep
numero = int(input('Em que número eu pensei?'))
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' *20)

computador = randint(0,5)

print('Processando...')
sleep(2)
if numero == computador:
    print('PARABÉNS! Voçê conseguiu me vencer!')


else:
    print('GANHEI! Eu pensei no número {} e não no {} '.format(computador,numero))


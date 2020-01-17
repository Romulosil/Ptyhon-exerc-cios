"""
Crie um programa que leia o nome completo de uma pessoa e
mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considera espaços).
- Qauntas letras tem o primeiro nome.


"""



nome = str(input('Digite seu nome completo:')).strip()
print('Analisando seu nome...')

print('Seu nome maiúsculas é',nome.upper())
print('Seu nome em minúculas é',nome.lower())
print('Seu nome tem ao todo' , len(nome)- nome.count(' '),'letras')
print('Quantas letras tem o primeiro nome',nome.find(' '))
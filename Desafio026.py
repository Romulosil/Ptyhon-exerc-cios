"""
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A".
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.



"""

frase = str(input("Digite uma frase: ")).strip()

print("A letra A aparece {} vezes na frase.".format(frase.lower().count('a')))
print("A primeira letra A apareceu na posição", frase.upper().find('A')+1)
print("A última letra A apareceu na posição ", frase.upper().rfind('A')+1)
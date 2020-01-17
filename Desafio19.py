"""
Um professor quer sortear um dos seus quatro alunos para apagar
o quadro.Faça um programa que ajude ele, lendo o nome delas e es-
crevendo o nome do escolhido.

"""
import random

alunoPri = str(input("Primeiro aluno: "))
alunoSeg = str(input("Segundo aluno: "))
alunoTer = str(input("Terceiro aluno: "))
alunoQua = str(input("Quarto aluno: "))

sort = random.randint(1,4)

if sort == 1:
    print("O aluno escolhido foi",alunoPri)
elif sort == 2:
    print("O aluno escolhido foi",alunoSeg)

elif sort == 3:
    print("O aluno escolhido foi",alunoTer)

elif sort == 4:
    print("O aluno escolhido foi" ,alunoQua)
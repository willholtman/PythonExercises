#SORTEAR ALUNOS - LER NOME E ESCOLHER
import random

a = input('Digite o primeiro nome: ')
b = input('Digite o segundo nome: ')
c = input('Digite o terceiro nome: ')
d = input('Digite o quarto nome: ')
list = a, b, c, d
print(random.choices(list))






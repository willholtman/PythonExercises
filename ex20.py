#ler quatro nomes e mostrar ordem sorteada
import random

a = input('Digite o primeiro nome: ')
b = input('Digite o segundo nome: ')
c = input('Digite o terceiro nome: ')
d = input('Digite o quarto nome: ')
list = a, b, c, d
print(random.sample([a, b, c, d], k=4))




#UM PROGRAMA QUE LEIA ALGO E MOSTRE SEU TIPO PRIMITIVO E OUTRAS INFORMAÇÕES POSSIVEIS
n = input('Digite algo:')
print('O tipo primitivo deste número é ', type(n))
print('É numérico?',n.isnumeric())
print('É alfanumérico?',n.isalnum())
print('É decimal?',n.isdecimal())
print('É alfabético?',n.isalpha())
print('Esta escrito em maiúsculo?',n.isupper())
print('Esta escrito em minúsculo?',n.islower())
print('Esta capitalizada?',n.istitle())
print('É um espaço?',n.isspace())

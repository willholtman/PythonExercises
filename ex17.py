# ler comprimento do cateto oposto e adj e calcular hip
from math import hypot
co = float(input('Informe o cateto oposto: '))
ca = float(input('Informe o cateto adjacente: '))
print('A hipotenusa é {:.2f}'.format(hypot(co, ca)))

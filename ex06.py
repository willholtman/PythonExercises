#LER O NÚMERO E MOSTRE O SEU DOBRO, TRIPLO E RAIZ
n1 = float(input('Digite um valor:'))
d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)
print('O dobro é {}, \n o triplo é {} \n e a raiz é {:.3f}'.format(d,t,r))

#CODIGO DA AULA
n = int(input("Digite um número:"))
print('O dobro de {} vale {}'.format(n, (n*2)))
print('O triplo de {} vale {}. \n A raiz quadrada de {} vale {:.3f}'.format(n, (n*3),n, pow(n, (1/2))))

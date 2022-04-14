#AULA
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite mais um valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n a multiplicação é {}, \n a divisão é {:.3f}'.format(s,m,d), end=' ')
print('A divisão inteira é {}, \n a potência é {}'.format(di,e))

#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E SEU ANTECESSOR
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
a = s - 1
d = s + 1
print('A soma é {}, o número antecessor é {} e o número sucessor é {}'.format(s,a,d))

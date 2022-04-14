#LER PREÇO E APRESENTAR NOVO VALOR COM 5% DE DESCONTO
n1 = float(input('Digite o valor do produto:R$'))
tx = n1 * 0.05
vd = n1 - tx
print('O novo valor do produto, com desconto de 5% é de R${:.2f}'.format(vd))

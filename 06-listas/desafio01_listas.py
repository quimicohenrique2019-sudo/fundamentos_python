# Autor: Henrique Prestes
# Projeto: Criar uma lista de pedidos

pedido = ['4 queijos', 'calabresa', 'costela', 'portuguesa', 'lombo']
nome = input('Digite seu nome para continuarmos')
comando = 'sim'

while comando == 'sim':
    print (pedido)
    comando=input('Olá, Digite seu pedido')
    print(f'Anotado! Deseja adicionar mais um item a sua lista? (sim ou não)')

if comando == 'não':
    print ('pedido finalizado')
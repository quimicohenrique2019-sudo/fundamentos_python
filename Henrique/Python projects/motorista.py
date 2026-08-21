# Autor: Henrique Prestes
# Projeto: Motorista if/else | and | variáveis

nome = input('Digite seu nome aqui: ')
idade = int(input('Digite sua idade: '))
carteira = True

# Estrutura Condicional
# and -> todas as condições tem que ser verdadeiras
if idade >= 18 and carteira:
    print('pode dirigir')
else:
    print('não pode dirigir')
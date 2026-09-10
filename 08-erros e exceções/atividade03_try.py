# Autor: Henrique Prestes
# Projeto: 


def divisao():
    try:
       valor1 = float(input('Digite o 1º valor: '))
       valor2 = float(input('Digite o 2º valor: '))
       divisao = valor1/valor2

    except ZeroDivisionError:
        print('Pare de tentar dividir por zero')
        print('Digite um valor maior que zero')
    except ValueError:
        print('Digite apenas números')
    else:
        print(f'O resultado da divisão é {divisao}')

divisao()
# Autor: Henrique Prestes
# Projeto: 


def IMC():
    try:
       valor1 = float(input('Digite o seu peso(kg): '))
       valor2 = float(input('Digite a sua altura(m): '))
       IMC = valor1/(valor2**2)

    except ZeroDivisionError:
        print('Sua altura não é zero')
        print('Digite sua altura correta')
    except ValueError:
        print('Digite apenas números')
    else:
        print(f'O resultado da divisão é {IMC:.2f}')

IMC()
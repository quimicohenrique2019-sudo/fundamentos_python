# Autor: Henrique Prestes
# Projeto: calculadora de IMC

print ('====== Calculadora de IMC ======\n')
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua sua altura (m): '))
imc = peso / (altura * altura)
print(f'seu IMC é: {imc:.2f}')

# 
if imc<= 18.5:
    print('Cuidado! Magreza')
elif imc <= 25:
    print('Peso ideal. Parabéns!')
elif imc <= 30:
    print('Cuidade! Sobrepeso')
elif imc <= 35:
    print('Cuidado! Obesidade grau I')
elif imc <= 40:
    print('Cuidado! Obesidade grau II')
else:
    print('Alerta Máximo!!! Obesidade grau III')
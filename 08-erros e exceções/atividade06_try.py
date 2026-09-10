# Autor: Henrique Prestes
# Projeto: Salvar dados em arquivos TXT


nome = input('Digite seu nome: ')
celular = input('Digite seu celular: ')
peso = float(input('Digite seu peso(kg): '))
altura = float(input('Digite sua altura(m): '))
imc = peso/(altura * altura)

arquivo = open('agenda.txt', 'a')
# arquivo.write(str(nome) +  ' | ' + str(celular) +  ' | '  + str(imc:.2f) + '\n')
arquivo.write(f'{nome} | {celular} | {imc:.2f}\n')
arquivo.close()
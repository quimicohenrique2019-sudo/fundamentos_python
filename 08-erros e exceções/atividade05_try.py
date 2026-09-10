# Autor: Henrique Prestes
# Projeto: Salvar dados em arquivos TXT


nome = input('Digite seu nome: ')
celular = input('Digite seu celular: ')

arquivo = open('agenda.txt', 'a')
arquivo.write(nome +  ' | ' + celular + '\n')
arquivo.close()
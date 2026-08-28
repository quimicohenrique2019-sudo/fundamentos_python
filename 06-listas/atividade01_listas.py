# Autor: Henrique Prestes
# Projeto: Listas

# Lista de frutas
#             0        1        2          3       4
frutas = ['banana', 'maçã', 'abacaxi', 'goiaba', 'kiwi']

print(frutas)

# adicionar um item na lista
frutas.append('laranja')
print(frutas)

# alterar o conteúdo de uma posição
# mudar a fruta kiwi para morango
frutas[4]='morango'
print (frutas)

# deletar um item por posição
# excluir a maça
del frutas[1]
print (frutas)

# inserir uma nova fruta na posição 1
frutas.insert(1,'mamão')
print(frutas)

# ordena a lista (ordem alfabética)
frutas.sort()
print(frutas)

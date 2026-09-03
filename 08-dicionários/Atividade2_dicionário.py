# Autor: Henrique Prestes
# Projeto: Uso de API (conceito de sicionário)

import requests

# uso da API do ViaCEP
# 18.125-170 | 18125170
cep = input("Digite seu CEP (somente números): ").strip().replace("-", "")

url = f"https://viacep.com.br/ws/{cep}/json/"
resposta = requests.get(url)
dados = resposta.json()

print(f"Logradouro: {dados['logradouro']}")
print(f"Bairro: {dados['bairro']}")
print(f"Cidade: {dados['localidade']}")
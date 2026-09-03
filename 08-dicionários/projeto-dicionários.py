# Autor: Henrique
# Projeto: Dicionários

# Projeto aquele lá
escola = {
    "salas": "sala_musica",
    "localização": "bloco_A",
    "qtd_lugares": "40",
    "caracteristica": "acustica"
}

# Acessando dados do dicionário:
print(f"Sala disponível{escola["salas"]}")

# Acessando mais itens ao dicionário
escola["iluminacao"] = "led"
print(f"print(f"Sala disponivel {escola["iluminacao"]}")")

# Acessando um valor do dicionário
escola["salas"] = "sala"
print(f"print (f"Sala disponível {escola["salas"]}")")

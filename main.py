import random  # Importando a biblioteca random para gerar números aleatórios
from  caracters import npcs  # Importando a lista de NPCs do arquivo caracters.py

def criacaoNpcs(lista):
    print("Criando NPCs")
    nome = input("Digite o nome do NPC: ")
    print("Sorteando os atributos do NPC")
    classe = input("Digite a classe do NPC: ")
    ataque = random.randint(1, 30)
    agilidade = random.randint(1, 100)
    vida = random.randint(1, 100)
    novoNpc = {"Nome": nome, "Vida": vida, "Ataque": ataque, "Destreza": agilidade, "Classe": classe}
    npcs.append(novoNpc)
    print(f"Vida: {vida} d100 \n Ataque: {ataque} d30\n Destreza: {agilidade} d100")
    print("NPC criado com sucesso!")

criacaoNpcs(npcs)
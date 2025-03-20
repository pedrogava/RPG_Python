import random  # Importando a biblioteca random para gerar números aleatórios       

npcs = []  # Lista de NPCs

def criacaoNpcs(lista):
    print("Criando NPCs")
    nome = input("Digite o nome do NPC: ")
    print("Sorteando os atributos do NPC")
    classe = input("Digite a classe do NPC: ")
    ataque = random.randint(1, 100)
    agilidade = random.randint(1, 100)
    vida = random.randint(1, 100)
    novoNpc = {"Nome": nome, "Vida": vida, "Ataque": ataque, "Destreza": agilidade, "Classe": classe}
    npcs.append(novoNpc)
    # print(f"Vida: {vida} d100 \n Ataque: {ataque} d100\n Destreza: {agilidade} d100")
    print("NPC criado com sucesso!")

# Verificação se a lista de NPCs não está vazia
if npcs:
    # Contando e exibindo cada npc da lista de NPCs
    for i, npc in enumerate(npcs):
        print(f"NPC {i+1}:")
        # Exibindo cada atributo do NPC
        for key, value in npc.items():
            print(f"  {key}: {value}")
else:
    # Caso a lista de NPCs esteja vazia, chama a função de criação de NPCs
    print("Não há NPCs na lista")
    criacaoNpcs(npcs)  # Chama a função de criação de NPCs




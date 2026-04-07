# Desafio 3: Lista de 5 nomes
# Cria lista com 5 nomes e imprime formatado
print("=== DESAFIO 3 - LISTA DE NOMES ===")
# Cria lista com 5 nomes (podem ser alterados)
nomes = ["Ana", "Bruno", "Carla", "Diego", "Elisa"]
# Imprime a lista completa
print("Lista de nomes:", nomes)
# Imprime cada nome numerado
print("\nNomes numerados:")
for i in range(len(nomes)):
    print(f"{i+1}. {nomes[i]}")
# Imprime quantidade total
print(f"\nTotal de nomes na lista: {len(nomes)}")

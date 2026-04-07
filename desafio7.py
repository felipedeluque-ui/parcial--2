# Desafio 7: Juros simples
# J = C × i × t (Juros = Capital × taxa × tempo)
print("=== DESAFIO 7 - JUROS SIMPLES ===")
# Recebe os dados do usuário
capital = float(input("Digite o capital inicial (R$): "))
taxa = float(input("Digite a taxa de juros anual (%): ")) / 100  # Converte % para decimal
tempo = float(input("Digite o tempo em anos: "))
# Calcula os juros imples
juros = capital * taxa * tempo
# Calcula o montante (capital + juros)
montante = capital + juros
# Exibe todos os resultados
print(f"\nCÁLCULO DE JUROS SIMPLES")
print(f"Capital inicial: R$ {capital:.2f}")
print(f"Taxa de juros: {taxa*100:.2f}% a.a.")
print(f"Tempo: {tempo} anos")
print(f"Juros = C × i × t = R$ {juros:.2f}")
print(f"Montante final: R$ {montante:.2f}")

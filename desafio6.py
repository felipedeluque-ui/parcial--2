# Desafio 5: Área de um triângulo
# Calcula área usando base e altura (Área = (base * altura) / 2)
print("=== DESAFIO 5 - ÁREA DO TRIÂNGULO ===")
# Recebe base e altura do usuário
base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))
# Calcla a área usando a fórmula
area = (base * altura) / 2
# Exibe o resultado formatado
print(f"\nÁREA DO TRIÂNGULO")
print(f"Base: {base}")
print(f"Altura: {altura}")
print(f"Área = (base × altura) ÷ 2")
print(f"Área = {area:.2f}")

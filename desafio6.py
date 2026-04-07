# Desafio 6: Conversão de tempo (segundos ↔ h/m/s)
# Converte segundos para horas/minutos/segundos e vice-versa
print("=== DESAFIO 6 - CONVERSÃO DE TEMPO ===")
print("1- Segundos → Horas/Minutos/Segundos")
print("2 - Horas/Minutos/Segundos → Segundos")
opcao = input("Escolha a conversão (1 ou 2): ")
if opcao == "1":
    # Segundos para H/M/S
    segundos_total = int(input("Digite a quantidade de segundos: "))
    horas = segundos_total // 3600
    minutos = (segundos_total % 3600) // 60
    segundos = segundos_total % 60
    print(f"\n{segundos_total} segundos = {horas:02d}:{minutos:02d}:{segundos:02d}")
elif opcao == "2":
    # H/M/S para segundos
    horas = int(input("Digite as horas: "))
    minutos = int(input("Digite os minutos: "))
    segundos = int(input("Digite os segundos: "))
    total_segundos = (horas * 3600) + (minutos * 60) + segundos
    print(f"\n{horas:02d}:{minutos:02d}:{segundos:02d} = {total_segundos} segundos")
else:
    print("Opção inválida!")

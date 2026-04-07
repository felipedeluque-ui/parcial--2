# Desafio 4: Calculadora simples
# Calculadora com operações básicas (+, -, *, /)
print("=== DESAFIO 4 - CALCULADORA SIMPLES ===")
# Recebe os números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
# Menu de operações
print("\nEscolha a operação:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")
opcao = input("Digite o número da operação (1-4): ")
# Executa a operação escolhida
if opcao == "1":
    resultado = num1 + num2
    operacao = "soma"
elif opcao == "2":
    resultado = num1 - num2
    operacao = "subtração"
elif opcao == "3":
    resultado = num1 * num2
    operacao = "multiplicação"
elif opcao == "4":
    if num2 != 0:
        resultado = num1 / num2
        operacao = "divisão"
    else:
        print("Erro: Divisão por zero!")
        exit()
else:
    print("Opção inválida!")
    exit()
# Exibe resultado
print(f"\nResultado da {operacao}: {num1} {opcao} {num2} = {resultado}")

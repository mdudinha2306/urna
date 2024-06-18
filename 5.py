import math

def calculadora():
    print("Calculadora simples:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Raiz quadrada")
    print("6 - Potenciação")
    
    opcao = int(input("Escolha a operação desejada (1-6): "))
    
    if opcao in [1, 2, 3, 4, 6]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        if opcao == 1:
            resultado = num1 + num2
        elif opcao == 2:
            resultado = num1 - num2
        elif opcao == 3:
            resultado = num1 * num2
        elif opcao == 4:
            resultado = num1 / num2
        elif opcao == 6:
            resultado = num1 ** num2
        
        print(f"Resultado: {resultado}")
    
    elif opcao == 5:
        num = float(input("Digite o número para calcular a raiz quadrada: "))
        resultado = math.sqrt(num)
        print(f"Raiz quadrada de {num} é {resultado}")
    
    else:
        print("Opção inválida.")

# Para testar a função:
calculadora()

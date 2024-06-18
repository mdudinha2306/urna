def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

# Exemplo de uso:
numero = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {numero} é {fatorial(numero)}")

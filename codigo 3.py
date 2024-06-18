
Você
Desafios para praticar PYTHON

Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 51-5.4.3.2.1-120. A saída deve ser conforme o exemplo abaixo:

Faça um Programa para um caixa eletronico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor minino e de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saida. Registre a informação A.M./P.M. como um valor "A" para A.M. e 'P' para P.M. Assin, a função para efetuar as conversões terá um parametro formal para registrar se é A.M. ου Ρ.Μ. Inclua um loop que permita que o usuario repita esse cálculo para novos valores de entrada
todas as vezes que desejar.

Faça uma calculadora em PYTHON que realize as 4 operacoes basicas, e tanben realize raiz quadrada e potenciação
ChatGPT
ChatGPT
Aqui estão as soluções para os desafios em Python conforme solicitado:

Desafio 1: Contagem de votos em uma eleição
python
Copiar código
def eleicao():
    candidatos = ['Candidato 1', 'Candidato 2', 'Candidato 3']
    num_candidatos = len(candidatos)
    
    num_eleitores = int(input("Digite o número total de eleitores: "))
    
    votos = [0] * num_candidatos
    
    for i in range(num_eleitores):
        print(f"Eleitor {i+1}, vote em um dos candidatos:")
        for j, candidato in enumerate(candidatos):
            print(f"{j+1} - {candidato}")
        
        voto = int(input("Digite o número do candidato escolhido: "))
        if 1 <= voto <= num_candidatos:
            votos[voto - 1] += 1
        else:
            print("Opção inválida. Voto não contabilizado.")
    
    print("\nResultado da eleição:")
    for i, candidato in enumerate(candidatos):
        print(f"{candidato} recebeu {votos[i]} votos.")

# Para testar a função:
eleicao()
Desafio 2: Cálculo do fatorial de um número
python
Copiar código
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

# Exemplo de uso:
numero = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {numero} é {fatorial(numero)}")
Desafio 3: Simulação de um caixa eletrônico
python
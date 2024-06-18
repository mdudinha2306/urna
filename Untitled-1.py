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

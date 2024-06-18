def converter_para_12h(hora, minuto):
    periodo = 'AM'
    if hora >= 12:
        periodo = 'PM'
        if hora > 12:
            hora -= 12
    if hora == 0:
        hora = 12
    return hora, minuto, periodo

# Função para formatar a saída
def imprimir_horario(hora, minuto, periodo):
    print(f"{hora}:{minuto:02d} {periodo}")

# Loop para permitir múltiplas conversões
while True:
    hora = int(input("Digite a hora (0-23): "))
    minuto = int(input("Digite os minutos (0-59): "))
    
    hora12, minuto, periodo = converter_para_12h(hora, minuto)
    imprimir_horario(hora12, minuto, periodo)
    
    continuar = input("Deseja converter outro horário? (s/n): ")
    if continuar.lower() != 's':
        break

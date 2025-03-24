procedimentos = {
    1: {"nome": "Consulta de Rotina", "duracao": "30 minutos"},
    2: {"nome": "Cardiologista", "duracao": "45 minutos"},
    3: {"nome": "Dermatologista", "duracao": "1 hora"},
    4: {"nome": "Nutricionista", "duracao": "15 minutos"}
}

horarios_disponiveis = ["09:00", "10:00", "11:00", "14:00", "15:00", "16:00"]

def mostrar_procedimentos():
    print("Escolha o procedimento desejado:")
    for codigo, info in procedimentos.items():
        print(f"{codigo}: {info['nome']} ({info['duracao']})")

def mostrar_horarios():
    print("\nHorários disponíveis:")
    for i, horario in enumerate(horarios_disponiveis, start=1):
        print(f"{i}: {horario}")

def agendar_consulta():
    print("Bem-vindo ao sistema de agendamento do consultório Bloom!\n")
    
    mostrar_procedimentos()
    while True:
        try:
            escolha_procedimento = int(input("\nDigite o número do procedimento: "))
            if escolha_procedimento in procedimentos:
                procedimento = procedimentos[escolha_procedimento]["nome"]
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
    
    mostrar_horarios()
    while True:
        try:
            escolha_horario = int(input("\nDigite o número do horário desejado: "))
            if 1 <= escolha_horario <= len(horarios_disponiveis):
                horario = horarios_disponiveis[escolha_horario - 1]
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
    
    print(f"\nVocê agendou: {procedimento} às {horario}.")
    print("A sua consulta foi agendada com sucesso!")

agendar_consulta()
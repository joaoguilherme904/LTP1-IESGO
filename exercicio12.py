from datetime import datetime

def calcular_idade_em_meses():
    data_de_nascimento = input("Digite sua data de nascimento (formato: AAAA-MM-DD): ")
    data_de_nascimento = datetime.strptime(data_de_nascimento, "%Y-%m-%d")
    hoje = datetime.now()
    diferenca = hoje - data_de_nascimento
    meses = diferenca.days // 30
    print(f"Sua idade em meses é aproximadamente: {meses} meses")

def calcular_idade_em_dias():
    data_de_nascimento = input("Digite sua data de nascimento (formato: AAAA-MM-DD): ")
    data_de_nascimento = datetime.strptime(data_de_nascimento, "%Y-%m-%d")
    hoje = datetime.now()
    diferenca = hoje - data_de_nascimento
    dias = diferenca.days
    print(f"Sua idade em dias é aproximadamente: {dias} dias")

def calcular_idade_em_horas():
    data_de_nascimento = input("Digite sua data de nascimento (formato: AAAA-MM-DD): ")
    data_de_nascimento = datetime.strptime(data_de_nascimento, "%Y-%m-%d")
    hoje = datetime.now()
    diferenca = hoje - data_de_nascimento
    horas = diferenca.days * 24 + diferenca.seconds // 3600
    print(f"Sua idade em horas é aproximadamente: {horas} horas")

def calcular_idade_em_minutos():
    data_de_nascimento = input("Digite sua data de nascimento (formato: AAAA-MM-DD): ")
    data_de_nascimento = datetime.strptime(data_de_nascimento, "%Y-%m-%d")
    hoje = datetime.now()
    diferenca = hoje - data_de_nascimento
    minutos = diferenca.days * 24 * 60 + diferenca.seconds // 60
    print(f"Sua idade em minutos é aproximadamente: {minutos} minutos")

def calcular_idade_em_segundos():
    data_de_nascimento = input("Digite sua data de nascimento (formato: AAAA-MM-DD): ")
    data_de_nascimento = datetime.strptime(data_de_nascimento, "%Y-%m-%d")
    hoje = datetime.now()
    diferenca = hoje - data_de_nascimento
    segundos = diferenca.days * 24 * 60 * 60 + diferenca.seconds
    print(f"Sua idade em segundos é aproximadamente: {segundos} segundos")

def main():
    while True:
        print("\nMenu de Opções:")
        print("1. Calcular idade em meses")
        print("2. Calcular idade em dias")
        print("3. Calcular idade em horas")
        print("4. Calcular idade em minutos")
        print("5. Calcular idade em segundos")
        print("6. Sair do programa")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            calcular_idade_em_meses()
        elif escolha == "2":
            calcular_idade_em_dias()
        elif escolha == "3":
            calcular_idade_em_horas()
        elif escolha == "4":
            calcular_idade_em_minutos()
        elif escolha == "5":
            calcular_idade_em_segundos()
        elif escolha == "6":
            print("Obrigado por usar o programa. Adeus!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
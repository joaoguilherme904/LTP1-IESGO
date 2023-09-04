#conversor de temperatura

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Bem-vindo ao Conversor de Temperatura!")
    escolha = input("Escolha uma opção:\n1. Celsius para Fahrenheit\n2. Fahrenheit para Celsius\n")
    
    if escolha == '1':
        celsius = float(input("Digite a temperatura em graus Celsius: "))
        casas_decimais = int(input("Digite o número de casas decimais para a resposta: "))
        fahrenheit = celsius_para_fahrenheit(celsius)
        resultado = round(fahrenheit, casas_decimais)
        print(f"{celsius} graus Celsius são aproximadamente {resultado} graus Fahrenheit.")
    elif escolha == '2':
        fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))
        casas_decimais = int(input("Digite o número de casas decimais para a resposta: "))
        celsius = fahrenheit_para_celsius(fahrenheit)
        resultado = round(celsius, casas_decimais)
        print(f"{fahrenheit} graus Fahrenheit são aproximadamente {resultado} graus Celsius.")
    else:
        print("Opção inválida. escolha 1 ou 2.")

if __name__ == "__main__":
    main()
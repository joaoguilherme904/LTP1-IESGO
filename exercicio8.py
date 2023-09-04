def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def interpretar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc >= 18.5 and imc < 24.9:
        return "Peso normal"
    elif imc >= 24.9 and imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

# Adquirir peso e altura do usuario
peso = float(input("Digite seu peso em quilogramas: "))
altura = float(input("Digite sua altura em metros: "))

# Calcular o IMC
imc = calcular_imc(peso, altura)

#interpretar imc
resultado = interpretar_imc(imc)

#Mostrar o imc
print(f"Seu IMC é {imc:.2f}, o que é classificado como '{resultado}'.")
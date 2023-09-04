# Calculadora de Idade:
### Crie um programa que recebe o ano de nascimento do usuário e calcula a idade atual.
### Bônus: faça o programa retornar o signo do usuário de acordo com o mês e dia do seu nascimento.

# Função para determinar o signo com base no mês e dia de nascimento
def determinar_signo(dia, mes):
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Áries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Touro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Gêmeos"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Câncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leão"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgem"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpião"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitário"
    else:
        return "Capricórnio"

ano_nascimento = int(input("Digite o ano de nascimento: "))
mes_nascimento = int(input("Digite o mês de nascimento (1-12): "))
dia_nascimento = int(input("Digite o dia de nascimento: "))

ano_atual = 2023

idade = ano_atual - ano_nascimento

signo = determinar_signo(dia_nascimento, mes_nascimento)

print(f"Sua idade atual é {idade} anos.")
print(f"Seu signo é {signo}.")
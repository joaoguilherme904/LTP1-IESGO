import random

def obter_resposta_aleatoria():
    respostas = ["Sim", "Não"]
    return random.choice(respostas)

pergunta = input("Digite sua pergunta: ")

resposta = obter_resposta_aleatoria()

print(f"A resposta para '{pergunta}' é: {resposta}")
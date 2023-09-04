import random

def gerar_numero():
    return random.randint(1, 100)

def adivinhar_par_ou_impar(numero):
    escolha = input("Digite 'par' ou 'impar': ").lower()
    if escolha == 'par' or escolha == 'impar':
        return escolha
    else:
        print("Escolha inválida. Digite 'par' ou 'impar'.")
        return adivinhar_par_ou_impar(numero)

def jogo_par_ou_impar():
    print("Esse e o jogo do Par ou Impar!")
    jogador1 = input("Jogador 1, digite seu nome: ")
    jogador2 = input("Jogador 2, digite seu nome: ")

    while True:
        numero = gerar_numero()
        print(f"O número sorteado é: {numero}")
        
        jogador1_escolha = adivinhar_par_ou_impar(numero)
        jogador2_escolha = adivinhar_par_ou_impar(numero)

        if (numero % 2 == 0 and jogador1_escolha == 'par') or (numero % 2 != 0 and jogador1_escolha == 'impar'):
            vencedor = jogador1
        else:
            vencedor = jogador2

        print(f"O vencedor desta rodada é: {vencedor}")
        continuar = input("Deseja jogar novamente? (sim/não): ").lower()
        if continuar != 'sim':
            break

if __name__ == "__main__":
    jogo_par_ou_impar()
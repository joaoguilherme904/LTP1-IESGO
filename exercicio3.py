import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Solicitar ao usuário o comprimento desejado da senha
tamanho_da_senha = int(input("Digite o comprimento da senha desejada: "))

# Gerar e exibir a senha
senha_gerada = gerar_senha(tamanho_da_senha)
print(f"Sua senha gerada é: {senha_gerada}")
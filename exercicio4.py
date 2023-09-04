# Pegar a frase do usuario
frase = input("Digite uma frase: ")

palavras = frase.split()

#contar palavras
numero_de_palavras = len(palavras)

frase_formatada = ''.join(palavras).upper()

#mostrar resultado
print(f"A frase contém {numero_de_palavras} palavra(s).")
print(f"Frase em letras maiúsculas e sem espaços em branco: {frase_formatada}")
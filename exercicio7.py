def analisar_string(string):
    # iniciar contadores
    maiusculas = 0
    minusculas = 0
    digitos = 0
    especiais = 0

    for char in string:
        if char.isupper():
            maiusculas += 1
        elif char.islower():
            minusculas += 1
        elif char.isdigit():
            digitos += 1
        else:
            especiais += 1

    return maiusculas, minusculas, digitos, especiais

texto = input("Digite uma string: ")

maiusculas, minusculas, digitos, especiais = analisar_string(texto)

print(f"Letras maiúsculas: {maiusculas}")
print(f"Letras minúsculas: {minusculas}")
print(f"Dígitos: {digitos}")
print(f"Caracteres especiais: {especiais}")
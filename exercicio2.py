# Dicionário de taxas de câmbio (moeda base: dólar americano)
taxas_de_cambio = {
    "USD": 1.0,    # Dólar 
    "EUR": 0.85,   # Euro
    "GBP": 0.73,   # Libra esterlina
    "JPY": 109.53, # Iene japonês
    "CAD": 1.25,   # Dólar canadense
    
}

def converter_moeda(valor, moeda_de, moeda_para):
    if moeda_de in taxas_de_cambio and moeda_para in taxas_de_cambio:
        taxa_de_cambio_de = taxas_de_cambio[moeda_de]
        taxa_de_cambio_para = taxas_de_cambio[moeda_para]
        valor_convertido = valor * (taxa_de_cambio_para / taxa_de_cambio_de)
        return valor_convertido
    else:
        return None

valor = float(input("Digite o valor a ser convertido: "))
moeda_de = input("Digite a moeda de origem (ex: USD, EUR, GBP, JPY, CAD): ").upper()
moeda_para = input("Digite a moeda de destino (ex: USD, EUR, GBP, JPY, CAD): ").upper()

valor_convertido = converter_moeda(valor, moeda_de, moeda_para)

if valor_convertido is not None:
    print(f"{valor} {moeda_de} equivalem a {valor_convertido} {moeda_para}")
else:
    print("Moeda de origem ou moeda de destino não encontrada nas taxas de câmbio predefinidas.")
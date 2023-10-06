#Crie uma classe chamada Carro que represente diferentes carros em uma revendedora de automóveis. A classe deve ter os seguintes atributos e métodos:

class Carro:
    modelos = {
        "Corolla": 18000,
        "Mustang": 100000,
        "Uno Mille": 1000,
        "Gol G3": 2000,
        "Marea Turbo": 1
    }
    def __init__(self, marca, modelo, ano, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = max(preco, self.modelos.get(modelo, 0))
        self.vendido = False

    def exibir_informacoes(self):
        if self.vendido == False:
            return f"Marca: {self.marca} \n Modelo: {self.modelo} \n Ano: {self.ano} \n Preço: R$ {self.preco} \n Em estoque."
        else:
            return f"Marca: {self.marca} \n Modelo: {self.modelo} \n Ano: {self.ano} \n Preço: R$ {self.preco} \n Veículo vendido!"
    def vender(self):
        self.vendido  = True
        print(f"Carro {self.marca} vendido com sucesso")
    
    def ajustar_preco(self, novo_preco):
        preco_minimo = self.modelos.get(self.modelo, 0)
        if novo_preco >= preco_minimo:
            self.preco = novo_preco
        else:
            print(f"Erro! O valor informado é menor que o aceito!. \n O preço mínimo para esse veículo é R$ {preco_minimo}. ")
        
        
    


carro1 = Carro("Fiat", "Uno Fire", 2002, 12000)

carro1.ajustar_preco(13500)
    
print(carro1.preco)

carro1.preco = 12222

print(carro1.preco)
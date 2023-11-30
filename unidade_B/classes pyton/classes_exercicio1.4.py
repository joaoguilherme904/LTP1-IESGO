class Jogo:
    def __init__(self, nome, categoria, taxa_entrada, id):
        self.nome = nome
        self.categoria = categoria
        self.taxa_entrada = taxa_entrada
        self.id = id

    def __str__(self):
        return f"Nome: {self.nome}, Categoria: {self.categoria}, Taxa de Entrada: {self.taxa_entrada}, ID: {self.id}"

class Plataforma:
    def __init__(self):
        self.jogos = []

    def adicionar_jogo(self, jogo):
        self.jogos.append(jogo)

    def remover_jogo(self, id):
        self.jogos = [jogo for jogo in self.jogos if jogo.id != id]

    def listar_jogos(self):
        for jogo in self.jogos:
            print(jogo)

    def __str__(self):
        return f"A plataforma tem {len(self.jogos)} jogos."

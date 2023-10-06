class Estudante:
    def __init__(self, nome, idade, nota, id):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        self.id = id

    def alterar_nota(self, nova_nota):
        self.nota = nova_nota

    def informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Nota: {self.nota}, ID: {self.id}"

class Turma:
    def __init__(self):
        self.estudantes = []

    def adicionar_estudante(self, estudante):
        self.estudantes.append(estudante)

    def remover_estudante(self, id):
        self.estudantes = [estudante for estudante in self.estudantes if estudante.id != id]

    def media_da_turma(self):
        return sum(estudante.nota for estudante in self.estudantes) / len(self.estudantes)

    def melhor_estudante(self):
        return max(self.estudantes, key=lambda estudante: estudante.nota)

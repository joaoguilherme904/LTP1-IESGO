class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.status = 'disponível'

class Membro:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.membros = []

    def adicionar_livro(self, titulo, autor):
        livro = Livro(titulo, autor)
        self.livros.append(livro)

    def adicionar_membro(self, nome):
        membro = Membro(nome)
        self.membros.append(membro)

    def emprestar_livro(self, titulo_livro, nome_membro):
        for livro in self.livros:
            if livro.titulo == titulo_livro and livro.status == 'disponível':
                for membro in self.membros:
                    if membro.nome == nome_membro:
                        membro.livros_emprestados.append(livro)
                        livro.status = 'emprestado'
                        return 'Livro emprestado com sucesso!'
        return 'Não foi possível emprestar o livro.'

    def retornar_livro(self, titulo_livro, nome_membro):
        for membro in self.membros:
            if membro.nome == nome_membro:
                for livro in membro.livros_emprestados:
                    if livro.titulo == titulo_livro:
                        membro.livros_emprestados.remove(livro)
                        livro.status = 'disponível'
                        return 'Livro retornado com sucesso!'
        return 'Não foi possível retornar o livro.'

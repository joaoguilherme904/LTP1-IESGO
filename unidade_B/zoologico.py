class Animal:
    def __init__(self, nome, especie, idade, dieta, id):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.dieta = dieta
        self.habitat = ""
        self.id = id
        
    def __str__(self):
        return (f"\nEspecie: {self.especie} \nNome: {self.nome} \nIdade: {self.idade} \nDieta: {self.dieta}")

    def descricao(self):
        return (f"\n{self.especie} {self.nome}, tem {self.idade} anos e é {self.dieta}")
    # Leo é um Leão de 5 anos que é Carnívoro").

class Zoologico:
    def __init__(self):
        self.animais = {}
        self.animais_lista = []


    def __str__(self):
        return (f"\nO zoologico tem {len(self.animais_lista)} animais sobre nossos cuidados! ")

    def adicionar_animal(self, animal):# para adicionar um novo animal ao zoológico.
        self.animais_lista.append(animal)
        # self.animais.append(animal)
        # print("")


    def remover_animal(self, nome): #para remover um animal do zoológico usando seu nome.
        print(f"{nome.especie} {nome.nome} morreu...\n")
        self.animais_lista.remove(nome)
        

    def listar_animais(self): #para listar todos os animais no zoológico e suas informações.
        print("Animais No Zoologio:")
        for for_animal in self.animais_lista:
            print("\t",for_animal.descricao())


leao_billy = Animal("Billy", "Leão", "4", "Carnivoro", "001")
leao_wendy = Animal("Wendy", "Leão", "3.5", "Carnivoro", "002")
vaca_maru = Animal("Maru", "Vaca", "3", "Herbívoro", "003")
porco_jose = Animal("José", "Porco", "7", "Onívoro", "004")
# print(leao_billy.descricao())

brasilia_zoo = Zoologico()
brasilia_zoo.adicionar_animal(leao_billy)
brasilia_zoo.adicionar_animal(leao_wendy)
brasilia_zoo.adicionar_animal(vaca_maru)
brasilia_zoo.adicionar_animal(porco_jose)

brasilia_zoo.listar_animais()

brasilia_zoo.remover_animal(porco_jose)
brasilia_zoo.listar_animais()


print(brasilia_zoo)
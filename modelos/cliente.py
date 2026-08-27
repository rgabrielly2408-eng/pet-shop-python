class Cliente:

    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def exibir_cliente(self):
        print("\n===== CLIENTE =====")
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"Quantidade de animais: {len(self.animais)}")

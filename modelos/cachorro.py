from modelos.animal import Animal


class Cachorro(Animal):

    def emitir_som(self):
        return "Au au!"

    def descricao(self):
        return (
            f"Cachorro: {self.nome} | "
            f"Idade: {self.idade} anos | "
            f"Peso: {self.peso} kg"
        )

from modelos.animal import Animal


class Gato(Animal):

    def emitir_som(self):
        return "Miau!"

    def descricao(self):
        return (
            f"Gato: {self.nome} | "
            f"Idade: {self.idade} anos | "
            f"Peso: {self.peso} kg"
        )

class Servico:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def descricao(self):
        return f"{self.nome} - R$ {self.preco:.2f}"

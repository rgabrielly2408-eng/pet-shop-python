from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    @abstractmethod
    def emitir_som(self):
        pass

    @abstractmethod
    def descricao(self):
        pass

Implementar classe abstrata Animal

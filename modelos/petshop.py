class PetShop:

    def __init__(self):
        self.clientes = []
        self.servicos = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_servico(self, servico):
        self.servicos.append(servico)

    def exibir_petshop(self):
        print("===== PET SHOP =====")
        print(f"Quantidade de clientes: {len(self.clientes)}")
        print(f"Quantidade de serviços: {len(self.servicos)}")

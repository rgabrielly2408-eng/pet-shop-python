#  Sistema de Pet Shop

Sistema desenvolvido em Python para simular o gerenciamento de um Pet Shop, permitindo cadastrar clientes e animais e organizar os serviços oferecidos.

##  Objetivo

O objetivo do projeto é desenvolver um sistema de terminal em Python para facilitar o cadastro de clientes e animais e o gerenciamento das informações do Pet Shop.

##  Integrantes

* gabrielly
* kiara
* ian geovanne
* joão arthur 


##  Arquitetura do projeto

O projeto foi organizado utilizando programação orientada a objetos (POO).

### Classes utilizadas

* **Animal** — classe abstrata que representa um animal.
* **Cachorro** — classe que herda de Animal.
* **Gato** — classe que herda de Animal.
* **Cliente** — representa o cliente do Pet Shop.
* **PetShop** — responsável por armazenar e gerenciar clientes e serviços.

### Estrutura dos arquivos

```text
piton-loja de animais/
│
├── main.py
├── README.md
│
└── modelos/
    ├── animal.py
    ├── cachorro.py
    ├── gato.py
    ├── cliente.py
    └── servico.py
```

##  Herança

A classe Animal é utilizada como classe base. As classes Cachorro e Gato herdam características de Animal e possuem comportamentos próprios.

```text
Animal
├── Cachorro
└── Gato
```

##  Tecnologias utilizadas

* Python
* Programação Orientada a Objetos
* GitHub

##  Como executar

1. Baixe ou clone o repositório.
2. Abra a pasta do projeto.
3. Execute o arquivo `main.py`.
4. Utilize o menu apresentado no terminal.

Exemplo:

```bash
python main.py
```

##  Organização

Os arquivos das classes ficam dentro da pasta modelos, enquanto o main.py é responsável pelo fluxo principal do sistema.

##  Desenvolvimento

O projeto foi desenvolvido de forma gradual, com utilização de commits para registrar as alterações realizadas durante o desenvolvimento.

##  Observação

O sistema poderá receber novas funcionalidades durante o desenvolvimento, como cadastro de serviços, consultas, histórico de atendimentos e outras melhorias.


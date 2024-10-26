import os
os.system("cls || clear")
def biblioteca():
    print("""=== Bem vindo à nossa biblioteca ===
    1 - Criar cadastro para comprar um livro
    2 - Comprar um livro
    3 - Alugar um livro
    4 - Devolução de um livro
    5 - Estoque de livros
    6 - Carrinho de compras
    0 - Sair do sistema
    (Para comprar/alugar um livro, primeiro solicite ver o estoque e depois coloque o id do livro que deseja)
    """)

def cadastro():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    cpf = input("Digite seu cpf: ")
    data_de_nascimento = input("Digite sua data de nascimento: ")
    print("Cadastro realizado com sucesso.")

def calcular_preco(preco, forma_de_pagamento):
    desconto = preco * 0.1
    if forma_de_pagamento == "A":
        return preco - desconto
    return preco + desconto

def compras_de_livros(carrinho):
    livros = {
        '123': ('Anabele', 150.00),
        '456': ('Chucky', 170.00),
        '789': ('It - A coisa', 190.00),
        '111': ('Diário de um banana', 150.00),
        '112': ('Auto da compadecida', 150.00),
        '113': ('A troca', 150.00),
        '101': ('Romeu e Julieta', 150.00),
        '102': ('Orgulho e preconceito', 150.00),
        '103': ('A culpa é das estrelas', 150.00),
    }

    codigo = input("Digite o código do livro que deseja: ")
    if codigo in livros:
        nome, preco = livros[codigo]
        print(f"Livro escolhido: {nome}")
        print(f"Valor do livro: R$ {preco:.2f}")
        forma_de_pagamento = input("Digite a forma de pagamento(À vista (A) e Crédito (C)): ")
        total_a_pagar = calcular_preco(preco, forma_de_pagamento)
        carrinho.append(total_a_pagar)
        print(f"Total à pagar: R$ {total_a_pagar:.2f}")
    else:
        print("Código do livro inválido!")


def alugar_um_livro():
    pass

def devolucao_de_um_livro():
    pass

def estoque_de_livro():
    print("""
    Estoque de livros:
    Livros de terror: 
    Anabele (123), Chucky (456), It - A coisa (789)
    Livros de humor: 
    Diário de um banana (111), Auto da compadecida (112), A troca (113)
    Livros de romance: 
    Romeu e Julieta (101), Orgulho e preconceito (102), A culpa é das estrelas (103)
    """)

def exibir_carrinho(carrinho):
    soma = sum(carrinho)
    print(f"Total à pagar: {soma:.2f}")

os.system("cls || clear")
biblioteca()
carrinho = []
while True:
    opcao = input("\nDigite o que deseja: ")
    match(opcao):
        case '1':
            cadastro()

        case '2':
            compras_de_livros(carrinho)
            pass

        case '3':
            alugar_um_livro()
            pass

        case '4':
            devolucao_de_um_livro()
            pass

        case '5':
            estoque_de_livro()
            pass
        case '6':
            exibir_carrinho(carrinho)

        case _:
            print("Saindo do sistema")
            break
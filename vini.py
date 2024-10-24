import os
os.system("cls || clear")
def biblioteca():
    print("""=== Bem vindo à nossa biblioteca ===
    1 - Criar cadastro
    2 - Comprar
    3 - Alugar
    4 - Devolução
    5 - Estoque
    0 - Sair do sistema
    """)
def cadastro():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    cpf = input("Digite seu cpf: ")
    data_de_nascimento = input("Digite sua data de nascimento: ")

def compras_de_livros():
    pass
biblioteca()
while True:
    opcao = input("\nDigite o que deseja: ")
    match(opcao):
        case '1':
            cadastro()

        #case '2':
            

        #case '3':
            

        #case '4':
            

        #case '5':
            

        case _:
            print("Saindo do sistema")
            break
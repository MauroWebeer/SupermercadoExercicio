# Exercicio de POO

from Funcionario import Funcionario
from Caixa import Caixa
from Usuario import Usuario
from Produto import Produto

#Dados pré-determinados dos Funcionarios

gerente = Funcionario(123,"Anthon You", "01-01-1985", "G")
funcionario_1 = Funcionario(134, "Steve Jefferson", "14-03-1991", "F")
funcionario_2 = Funcionario(145, "Calson Smith", "25-07-1987", "F")
funcionario_3 = Funcionario(156, "William White", "15-06-1998", "F")
funcionario_4 = Funcionario(167, "Hanna Pinkman", "09-11-1995", "F")
funcionario_5 = Funcionario(178, "Kim Elen", "31-01-1999", "F")

#Configuração das Caixas

caixa_1 = Caixa(84254)
caixa_2 = Caixa(86524)
caixa_3 = Caixa(85426)

#Usuarios e senha para acessar o caixa



usuario_0 = Usuario(123, gerente.nome, "anthon", "G123")

usuario_1 = Usuario(134, funcionario_1.nome, "steve", "F134")

usuario_2 = Usuario(145, funcionario_2.nome, "calson", "F145")

usuario_3 = Usuario(156, funcionario_3.nome, "william", "F156")

usuario_4 = Usuario(167, funcionario_4.nome, "hanna", "F167")

usuario_5 = Usuario(178, funcionario_5.nome, "kim", "F178")

# PROUTOS

prod_1 = Produto(984576, "Maça", "fruta", True)
prod_2 = Produto(785429, "Coca-Cola", "bebida", False)
prod_3 = Produto(687476, "Filé Mignon", "frios", True)
prod_4 = Produto(347152, "Papel Higiênio", "limpeza", False)
prod_5 = Produto(984576, "Arroz", "alimeto", False)


# Guardar usuarios
lista_de_usuarios = []
lista_de_usuarios.append(usuario_0)
lista_de_usuarios.append(usuario_1)
lista_de_usuarios.append(usuario_2)
lista_de_usuarios.append(usuario_3)
lista_de_usuarios.append(usuario_4)
lista_de_usuarios.append(usuario_5)

#Demonstração Código

#ABRIR O CAIXA


Login = input("Digite seu login: ")
Senha = input("Digite sua senha: ")

aux = False
for usuario in lista_de_usuarios:
    if usuario.login == Login or usuario.senha == Senha:
        aux=True
        usuario_logado = usuario

if aux == False:
    print(f'Login ou Senha inválidos')
    exit()

    print("O usuario", usuario_logado.nome, "está logado")

#OPÇÕES DENTRO DA CAIXA
escolha = 0

while escolha != int(4):



    print(''' Escolha uma das opções abaixo:
[1] Iniciar Caixa
[2] Trocar de Usuario
[3] Gerenciar Estoque
[4] Sair''')

    escolha = int(input())

# OPÇÃO INVÁLIDA
    while int(0) <= escolha >= int(5):
        print("Opção escolhida não disponível")
        escolha = int(input("Escolha uma opção:"))

# OPÇÃO INICIAR CAIXA

    if escolha == int(1):


# OPÇÃO TROCAR DE USUARIO

    elif escolha == int(2):
        Login = input("Digite seu login: ")
        Senha = input("Digite sua senha: ")

        aux = False
        for usuario in lista_de_usuarios:
            if usuario.login == Login or usuario.senha == Senha:
                aux = True
                usuario_logado = usuario

        if aux == False:
            print(f'Login ou Senha inválidos')
            exit()

        print("O usuario", usuario_logado.nome, "está logado")

# OPÇÃO GERENCIAR ESTOQUE

    if escolha == int(3):
        opcao_estoque = 0

        while  opcao_estoque != 4:

            print(''' Escolha uma das opções abaixo:
            [1] Consultar Estoque
            [2] Adicionar Ítem ao Estoque
            [3] Remover ítem do Estoque
            [4] Sair''')

            opcao_estoque = int(input())

            while 0 <= opcao_estoque >= 5:
                opcao_estoque = int(input("Opção inválida. Tente novamente:"))
                pass

            if opcao_estoque == 1:
                print("ENTREI 1")

            if opcao_estoque == 2:
                print("ENTREI 2")

            if opcao_estoque == 3:
                print("ENTREI 3")
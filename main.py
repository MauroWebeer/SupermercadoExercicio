# Exercicio de POO

import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="knust1000", database="supermarket")
mycursor = mydb.cursor()


from Funcionario import Funcionario
from Caixa import Caixa
from Usuario import Usuario
from Produto import Produto

#Demonstração Código

#INICIAR MAQUINA

access = False
while access == False:

    Login = input("Digite seu login: ")
    Senha = input("Digite sua senha: ")

    user = Usuario(Login, Senha)
    logando = user.login_usuario(Login, Senha)

    if logando == False:
        pass
    elif logando == True:
        access = True


#OPÇÕES DENTRO DA CAIXA
escolha = 0

while escolha != int(4):

    print('''Escolha uma das opções abaixo:
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
        print("Caixa iniciado!")
        fex = True
        caixa = True
        cx = Caixa()
        while fex == True:
            total = float(0)

            while caixa != False:

                print("ENTREI")
                codg = input("Insira o código do produto")
                preco = cx.passar_produto(codg)

                total += preco
                print("Total=", total)

                aux = input("aperte 0 para fechar compra ou 1 para continuar")
                caixa = cx.fechar_caixa(int(aux))
                print(caixa)

            print("TOTAL =", total)
            caixa = True

            aux2 = input("aperte 1 para nova compra ou 0 para fechar o caixa")
            fex = cx.fechar_caixa(aux2)

# OPÇÃO TROCAR DE USUARIO

    elif escolha == int(2):
        access = False
        while access == False:

            Login = input("Digite seu login: ")
            Senha = input("Digite sua senha: ")

            user = Usuario(Login, Senha)
            logando = user.login_usuario(Login, Senha)

            if logando == False:
                pass
            elif logando == True:
                access = True

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

            prod = Produto()

            if opcao_estoque == 1:
# CONSULTAR ESTOQUE

                estoque = prod.total_estoque()


            if opcao_estoque == 2:
#ADICIONAR ITEM AO ESTOQUE

                prod.adicionar_estoque()

            if opcao_estoque == 3:
#REMOVER ITEM DO ESTOQUE
                prod.remover_estoque()
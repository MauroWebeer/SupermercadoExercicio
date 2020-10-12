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
[3] Gerenciar Estoque e Vendas
[4] Sair''')

    escolha = int(input())

# OPÇÃO INVÁLIDA
    while int(0) <= escolha >= int(5):
        print("Opção escolhida não disponível")
        escolha = int(input("Escolha uma opção:"))

# OPÇÃO INICIAR CAIXA

    if escolha == int(1):
        cx = Caixa()
        escolha_caixa = cx.escaixa()

        print("Caixa",escolha_caixa," iniciado!")


        entrar_caixa = True
        while entrar_caixa == True:

            preco = cx.passar_produto(escolha_caixa, Login)
            print("TOTAL DA COMPRA =", preco)

            pagamento = cx.pagamento(preco)

            entrar_caixa_1 = input("Deseja continuar (C) ou sair (S)")

            while (True):
                if entrar_caixa_1 != "C" and entrar_caixa_1 != "S":
                    entrar_caixa_1 = input("Codigo invalido, tente novamente...")
                else:
                    break

            if entrar_caixa_1 == str("C") or entrar_caixa_1 == str("c"):
                print("Compra iniciada...")
                entrar_caixa = True

            elif entrar_caixa_1 == str("S") or entrar_caixa_1 == str("s"):
                entrar_caixa = False
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

# OPÇÃO GERENCIAR ESTOQUE E VENDAS

    if escolha == int(3):
        opcao_estoque = 0

        while  opcao_estoque != 5:

            print(''' Escolha uma das opções abaixo:
            [1] Consultar Estoque
            [2] Adicionar Ítem ao Estoque
            [3] Remover ítem do Estoque
            [4] Relatório de Venda 
            [5] Relatório de Estoque
            [6] Sair''')

            opcao_estoque = int(input())

            while 0 <= opcao_estoque >= 7:
                opcao_estoque = int(input("Opção inválida. Tente novamente:"))
                pass

            prod = Produto()

            if opcao_estoque == 1:
# CONSULTAR ESTOQUE

                estoque = prod.total_estoque()


            if opcao_estoque == 2:
#ADICIONAR ITEM AO ESTOQUE

                prod.adicionar_estoque(Login)

            if opcao_estoque == 3:
#REMOVER ITEM DO ESTOQUE
                prod.remover_estoque(Login)

#EMITIR RELATORIOS DE VENDAS
            if opcao_estoque == 4:
                prod.relatorio()

#EMITIR RElATORIO DE ESTOQUE

            if opcao_estoque == 5:
                prod.relatorio_estoque()


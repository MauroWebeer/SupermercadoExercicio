import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="knust1000", database="supermarket")
mycursor = mydb.cursor(buffered=True)

class Caixa:

    def fechar_caixa(self):
        resposta = input("Deseja finalizar a compra?")
        if fechar != 0:
            return True
        else:
            return False

    def passar_produto(self, caixa, login):
        prod = input("Insira o codigo do produto")
        mycursor.execute("SELECT nome FROM funcionarios WHERE login = '%s'" % (login))
        results = mycursor.fetchall()
        resultado = list(sub[0] for sub in results)
        vendedor_reg = str(resultado[0])
        caixa_reg = caixa
        total = float(0)

        while (True):
            entrada = False
            if str(prod) == "F":
                sql = "INSERT INTO vendas(caixa, vendedor, total) VALUES (%s, %s, %s)"
                val = (caixa_reg, vendedor_reg, total)
                mycursor.execute(sql, val)
                mydb.commit()

                return (total)

                break

            mycursor.execute("SELECT codigo FROM produtos")
            results = mycursor.fetchall()
            lista_resultado = list(sub[0] for sub in results)
            for x in lista_resultado:
                if str(x) == str(prod):
                    entrada = True


            if entrada == True:
                mycursor.execute("SELECT valor FROM produtos WHERE codigo = '%s'" %(prod))
                results = mycursor.fetchall()
                resultado = list(sub[0] for sub in results)
                preco = float(resultado[0])
                total += preco

                #REMOVENDO DO ESTOQUE

                mycursor.execute("SELECT qntd FROM produtos WHERE codigo = '%s'" % (prod))
                results_2 = mycursor.fetchall()
                resultado_q = list(sub[0] for sub in results_2)
                qntd_anterior = int(resultado_q[0])-int(1)

                sql = "UPDATE produtos SET qntd = %s WHERE codigo = %s"
                val = (qntd_anterior, prod)
                mycursor.execute(sql, val)
                mydb.commit()

                prod = input("insira o codigo do produto")


            if entrada == False:
                prod = input("Código inválido, tente novamente:")


    def pagamento(self, total):
        forma = input("Qual é a forma de pagamento? Cartão (C) ou Dinheiro (D)")

        #sql = "UPDATE vendas SET formapagamento = %s WHERE venda = %s"
        #val = (forma, venda)
        #mycursor.execute(sql, val)
        #mydb.commit()

        while forma != "C" and forma != "D" and forma != "c" and forma != "d":
            forma = input("Insira uma opção válida")

        if forma == "C" or forma == "c":
            print("TROCO = R$00,00", "Compra FINALIZADA")
        elif forma == "D" or forma == "d":
            receb = input("Qual o valor recebido?")
            troco = float(receb) - float(total)
            print("TROCO =R$",troco)

    def escaixa(self):
        while (True):
            escolha = input('''Escolha um dos caixas abaixo:
            (1) Caixa M2654
            (2) Caixa R3648
            (3) Caixa T4863
            (4) SAIR''')

            if escolha == "1":
                return("M2654")

            elif escolha == "2":
                return("R3648")

            elif escolha == "3":
                return("T4863")

            elif escolha == "4":
                return()
            else:
                escolha = input("Escolha inválida, tente de novo:")





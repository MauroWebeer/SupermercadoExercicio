import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="knust1000", database="supermarket")
mycursor = mydb.cursor(buffered=True)

from Produto import Produto

class Caixa:

    def fechar_caixa(self):
        resposta = input("Deseja finalizar a compra?")
        if fechar != 0:
            return True
        else:
            return False

    def passar_produto(self, caixa, login):
        prod = input("Insira o codigo do produto")
        lista_produtos = []
        mycursor.execute("SELECT nome FROM funcionarios WHERE login = '%s'" % (login))
        results = mycursor.fetchall()
        resultado = list(sub[0] for sub in results)
        vendedor_reg = str(resultado[0])
        caixa_reg = caixa

        total = float(0)
        stq = Produto()


        while (True):
            lista_produtos.append(prod)
            entrada = False
            if str(prod) == "F":
                sql = "INSERT INTO vendas(caixa, vendedor, total, formapagamento) VALUES (%s, %s, %s, %s)"
                val = (caixa_reg, vendedor_reg, total, "AA")
                mycursor.execute(sql, val)
                mydb.commit()

                #for produto in lista_produtos[:-1]:


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

                stq.estoque_status(prod)

                stq.atualizar_estoque()

                mycursor.execute("SELECT qntd FROM produtos WHERE codigo = '%s'" % (prod))
                results_2 = mycursor.fetchall()
                resultado_q = list(sub[0] for sub in results_2)
                qntd_anterior = int(resultado_q[0])-int(1)



                sql = "UPDATE produtos SET qntd = %s WHERE codigo = %s"
                val = (qntd_anterior, prod)
                mycursor.execute(sql, val)
                mydb.commit()
                #prod_ant = prod
                prod = input("insira o codigo do produto")


            if entrada == False:
                prod = input("Código inválido, tente novamente:")


    def pagamento(self, total):
        forma = input("Qual é a forma de pagamento? Cartão (C) ou Dinheiro (D)")


        while forma != "C" and forma != "D" and forma != "c" and forma != "d":
            forma = input("Insira uma opção válida")

        if forma == "C" or forma == "c":
            print("TROCO = R$00,00", "Compra FINALIZADA")
            mycursor.execute("SELECT venda FROM vendas where formapagamento = 'AA'")
            results = mycursor.fetchall()
            lista_resultado = list(sub[0] for sub in results)
            venda_pag = lista_resultado[0]
            sql = "UPDATE vendas SET formapagamento = %s WHERE venda = %s"
            val = ("C", venda_pag)
            mycursor.execute(sql, val)
            mydb.commit()
        elif forma == "D" or forma == "d":
            receb = input("Qual o valor recebido?")
            troco = float(receb) - float(total)
            print("TROCO =R$",troco)
            mycursor.execute("SELECT venda FROM vendas where formapagamento = 'AA'")
            results = mycursor.fetchall()
            lista_resultado = list(sub[0] for sub in results)
            venda_pag = lista_resultado[0]
            sql = "UPDATE vendas SET formapagamento = %s WHERE venda = %s"
            val = ("D", venda_pag)
            mycursor.execute(sql, val)
            mydb.commit()
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





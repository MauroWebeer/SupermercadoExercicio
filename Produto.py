import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="knust1000", database="supermarket")
mycursor = mydb.cursor(buffered=True)

from datetime import datetime
from datetime import date
import time

class Produto:


# CONSULTANDO ESTOQUE
    def total_estoque(self):
        mydb.commit()
        mycursor.execute("SELECT nome, qntd FROM produtos")
        results = mycursor.fetchall()
        for x in results:
            print(str(x[0]),"--",x[1])

    def adicionar_estoque(self, codigin):
        while (True):

            mycursor.execute("SELECT cargo FROM funcionarios WHERE login = '%s'" % (codigin))
            results = mycursor.fetchall()
            lista_resultado_3 = list(sub[0] for sub in results)

            if lista_resultado_3[0] == "F":
                print("Você não está autorizado a fazer alteração no estoque.")
                return ()
                break


            resposta_1 = str(input("Quer adicionar um item ja cadastrado (C) ou um item novo (N)?"))


            if resposta_1 == 'C' or resposta_1 == 'c':
                resposta_2 = int(input("Digite o codigo do produto"))

                mycursor.execute("SELECT codigo FROM produtos")
                results = mycursor.fetchall()
                lista_resultado = list(sub[0] for sub in results)

                for x in lista_resultado:
                    if str(x) == str(resposta_2):
                        resposta_3 = int(input("Quantos produtos estão sendo adicionados?"))
                        mycursor.execute("SELECT qntd FROM produtos WHERE codigo = '%s'" % (resposta_2))
                        resultado_1 = mycursor.fetchall()
                        lista_resultado_1 = list(sub[0] for sub in resultado_1)
                        resultado_aux = int(lista_resultado_1[0])
                        quant_atualizada = resultado_aux + resposta_3
                        sql = "UPDATE produtos SET qntd = %s WHERE codigo = %s"
                        val = (quant_atualizada, resposta_2)
                        mycursor.execute(sql, val)
                        mydb.commit()


            elif resposta_1 == 'N' or resposta_1 =='n':
                while (True):
                    codg = input("Insira o codigo do produto a ser adicionado")
                    nome = input("Insira o nome do produto a ser adicionado")
                    valor = input("Insira o valor do produto a ser adicionado")
                    quant = input("Insira a quantida de produtos a serem adicionado")
                    mycursor.execute("SELECT codigo FROM produtos")
                    results = mycursor.fetchall()
                    lista_resultado = list(sub[0] for sub in results)
                    aux = False
                    for x in lista_resultado:
                        if str(x) == str(codg):
                            aux = True

                    if aux == False:
                        sql = "INSERT INTO produtos(codigo, nome, valor, qntd) VALUES (%s,%s,%s,%s)"
                        val = (codg, nome, valor, quant)
                        mycursor.execute(sql, val)
                        mydb.commit()
                        guardar_estoque()
                        return()


                    aux_3 = int(input("Conflito de dados,aperte enter para tentar novamente ou precisone 0 para sair"))
                    if aux_3 == 0:
                        break

            else:
                resposta_4 = int(input("Resposta inválida tente novamente com enter ou aperte 0 para sair"))
                if resposta_4 == 0:
                    break
                elif resposta_4 != 0:
                    pass

    def remover_estoque(self, codigin):

        mycursor.execute("SELECT cargo FROM funcionarios WHERE login = '%s'" % (codigin))
        results = mycursor.fetchall()
        lista_resultado_3 = list(sub[0] for sub in results)

        if lista_resultado_3[0] == "F":
            print("Você não está autorizado a fazer alteração no estoque.")
            return ()


        entrada = False
        resposta_6 = int(input("Digite o codigo do produto que deseja remover"))
        while (True):



             mycursor.execute("SELECT codigo FROM produtos")
             results = mycursor.fetchall()
             lista_resultado = list(sub[0] for sub in results)
             for x in lista_resultado:
                if str(x) == str(resposta_6):
                     entrada = True

             if entrada == True:
                resposta_7 = int(input("Digite a quantidade de produtos a serem removidos"))
                mycursor.execute("SELECT qntd FROM produtos WHERE codigo = '%s'" % (resposta_6))
                resultado_1 = mycursor.fetchall()
                lista_resultado_1 = list(sub[0] for sub in resultado_1)
                resultado_aux = int(lista_resultado_1[0])
                quant_atualizada = resultado_aux - resposta_7
                sql = "UPDATE produtos SET qntd = %s WHERE codigo = %s"
                val = (quant_atualizada, resposta_6)
                mycursor.execute(sql, val)
                mydb.commit()

                #Guardando estoque
                #mycursor.execute("SELECT nome, qntd FROM produtos")
                #result = mycursor.fetchall()
                #lista_produtos = []
                #for t in result:
                #    for x in t:
                #        lista_produtos.append(x)
                #print(lista_produtos)

                #lista_aux = str(lista_produtos)
                #mycursor.execute("INSERT INTO estoque_status (estoque) VALUES '%s'" % (lista_aux))
                #mydb.commit()


                entrada = False

                resposta_8 = int(input("Para remover outro produto digite 1. Para sair 0"))
                if resposta_8 == 1:
                    pass
                elif resposta_8 == 0:
                    break
             else:
                 resposta_6 = input("Digite um codigo válido")

    def relatorio(self):
        resposta = int(input('''Escolha uma das opções
        [1] RELATORIO DE VENDAS
        [2] RELATORIO DE ESTOQUE
        [3] SAIR
        '''))

        if resposta == 1:
            #CRIAR TABELA PARA RELATORIO
            sql = "CREATE TABLE relatorio (ident integer NOT NULL AUTO_INCREMENT, caixa varchar(10), vendedor varchar(20), total float(20), PRIMARY KEY(ident))"
            mycursor.execute(sql)
            mydb.commit()

            #CRIAR RELATORIO

            #DIA DO RELATORIO
            date_entry = input('Digite a data (YYYY-MM-DD)')
            year, month, day = map(int, date_entry.split('-'))
            date1 = datetime.date(year, month, day)

            caixx = ["M2654","T4863","R3648"]

            for caixxs in caixx:
                sql = "SELECT nome FROM funcionarios WHERE cargo = 'F'"
                mycursor.execute(sql)
                results = mycursor.fetchall()
                lista_resultado = list(sub[0] for sub in results)

                for nome in  lista_resultado:
                    sql = "SELECT total FROM vendas WHERE vendedor = %s AND caixa = %s AND date(hora_venda) = %s"
                    val = (nome, caixxs, date1)
                    mycursor.execute(sql, val)
                    results_2 = mycursor.fetchall()
                    lista_resultado_2 = list(sub[0] for sub in results_2)

                    #somando os valores de venda e guardando-os
                    if len(lista_resultado_2) != int(0):
                        valor_total = 0
                        for valor in lista_resultado_2:
                            valor_total += valor

                        sql = "INSERT INTO relatorio(caixa, vendedor, total) VALUES (%s, %s, %s)"
                        val = (caixxs, nome, valor_total)
                        mycursor.execute(sql, val)
                        mydb.commit()

            mycursor.execute("SELECT caixa, vendedor, total FROM relatorio")
            results_3 = mycursor.fetchall()
            for t in results_3:
                result = []
                for x in t:
                    result.append(x)
                print('''-------------------------------------------
''', result)
            print('''-------------------------------------------''')
            #DELETAR TABELA DE RELATORIO
            sql = "DROP TABLE relatorio"
            mycursor.execute(sql)
            mydb.commit()
            return()

        if resposta == 3:
            return()


    def estoque_status(self, codigo):
        codigo_prodt = int(codigo)

        data_est = date.today()
        #print(data_est)



        #sql = "SELECT nome FROM produtos WHERE codigo = '%s'"
        #val = (codigo_prodt)
        mycursor.execute("SELECT nome FROM produtos WHERE codigo = '%s'" % (codigo_prodt))
        results_2 = mycursor.fetchall()
        #print(results_2)
        nome_produto = list(sub[0] for sub in results_2)

        #print(nome_produto)


        mycursor.execute("SELECT qntd FROM produtos WHERE codigo = '%s'" % (codigo_prodt))
        results_3 = mycursor.fetchall()
        #print(results_3)
        qntd_atual = list(sub[0] for sub in results_3)

        #print(qntd_atual)

        mycursor.execute("SELECT qntd FROM estoque_status WHERE  DATE(data_estoque) = '%s' AND produto = '%s'" % (data_est, nome_produto[0]))
        results_4 = mycursor.fetchall()


        #VERIFICANDO EXISTENCIA DE DADOS
        if not len(results_4):
            #print("ENTREI")
            sql = "INSERT INTO estoque_status (produto, qntd) VALUES (%s, %s)"
            val = (nome_produto[0], qntd_atual[0])
            mycursor.execute(sql, val)
            mydb.commit()

            time.sleep(1)
            mycursor.execute("SELECT qntd FROM estoque_status WHERE  DATE(data_estoque) = '2020-10-12' AND produto = '%s'" % (nome_produto[0]))
            results_4 = mycursor.fetchall()

        #print(results_4)
        qntd_status = list(sub[0] for sub in results_4)

        #print(qntd_status)

        sql = "INSERT INTO estoque_status (produto, qntd) VALUES (%s, %s)"
        val = (nome_produto[0], int(qntd_atual[0])-1)
        mycursor.execute(sql, val)
        mydb.commit()

    def atualizar_estoque(self):
        nomes = []
        #horas = []

        mycursor.execute("SELECT produto FROM estoque_status")
        results = mycursor.fetchall()
        for t in results:
            for i in t:
                if i not in nomes:
                    nomes.append(i)
                    print(nomes)

        for nome in nomes:
            mycursor.execute("SELECT MIN(data_estoque) FROM estoque_status WHERE produto = '%s'" %(nome))
            results_2 = mycursor.fetchall()
            for s in results_2:
                for j in s:
                    data_min = j

                    mycursor.execute("SELECT MAX(data_estoque) FROM estoque_status WHERE produto = '%s'" % (nome))
                    results_3 = mycursor.fetchall()
                    for x in results_3:
                        for k in x:
                            data_max = k

                            sql = "DELETE FROM estoque_status WHERE produto = %s AND data_estoque != %s AND data_estoque != %s"
                            val = (nome, data_min, data_max)
                            mycursor.execute(sql, val)
                            mydb.commit()

    def relatorio_estoque(self):
        mycursor.execute("SELECT produto, qntd FROM estoque_status")
        result = mycursor.fetchall()
        for x in result:
            print('''-------------------
            ''', x)

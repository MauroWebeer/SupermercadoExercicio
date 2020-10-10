import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="knust1000", database="supermarket")
mycursor = mydb.cursor(buffered=True)

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
                entrada = False

                resposta_8 = int(input("Para remover outro produto digite 1. Para sair 0"))
                if resposta_8 == 1:
                    pass
                elif resposta_8 == 0:
                    break
             else:
                 resposta_6 = input("Digite um codigo válido")






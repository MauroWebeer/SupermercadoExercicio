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

    def passar_produto(self):
        prod = input("Insira o codigo do produto")


        total = float(0)

        while (True):
            entrada = False
            if str(prod) == "F":
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
                prod = input("insira o codigo do produto")


            if entrada == False:
                prod = input("Código inválido, tente novamente:")


    def pagamento(self, total):
        forma = input("Qual é a forma de pagamento? Cartão (C) ou Dinheiro (D)")

        while forma != "C" and forma != "D" and forma != "c" and forma != "d":
            forma = input("Insira uma opção válida")

        if forma == "C" or forma == "c":
            print("TROCO = R$00,00", "Compra FINALIZADA")
        elif forma == "D" or forma == "d":
            receb = input("Qual o valor recebido?")
            troco = float(receb) - float(total)
            print("TROCO =R$",troco)



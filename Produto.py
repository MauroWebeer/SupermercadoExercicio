import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="knust1000", database="supermarket")
mycursor = mydb.cursor(buffered=True)

class Produto:

# CONSULTANDO ESTOQUE
    def total_estoque(self):
        mycursor.execute("SELECT nome, qntd FROM produtos")
        results = mycursor.fetchall()
        for x in results:
            print(str(x[0]),"--",x[1])

    def adicionar_estoque(self):
        aux_2 = False
        while aux_2 == False:
            codg = input("Insira o codigo do produto a ser adicionado")
            nome = input("Insira o nome do produto a ser adicionado")
            valor = input("Insira o valor do produto a ser adicionado")
            quant = input("Insira a quantida de produtos a serem adicionado")
            mycursor.execute("SELECT codigo FROM produtos")
            results = mycursor.fetchall()
            aux = False
            for x in range(len(results)):
                codigo_int = results[x]
                print(results[0])
                print(codigo_int,codg)
                if codigo_int == codg:
                    print("YES")
                    aux = True

            if aux == False:
                sql = "INSERT INTO produtos(codigo, nome, valor, qntd) VALUES (%s,%s,%s,%s)"
                val = (codg, nome, valor, quant)
                mycursor.execute(sql, val)
                mydb.commit()
                return()
            else:
                print("Conflito de dados, tente novamente")



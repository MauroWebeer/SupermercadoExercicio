import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="knust1000", database="supermarket")
mycursor = mydb.cursor(buffered=True)

class Caixa:

    def fechar_caixa(self, fechar):
        if fechar != 0:
            return True
        else:
            return False

    def passar_produto(self, codigo):
        mycursor.execute("SELECT valor FROM produtos WHERE codigo = '%s'" %(codigo))
        result = mycursor.fetchone()
        for x in result:
            return float(x)



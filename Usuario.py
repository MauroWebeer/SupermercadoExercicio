import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="knust1000", database="supermarket")
mycursor = mydb.cursor(buffered=True)

class Usuario :

    def __init__(self, login, senha):
        self.log = login
        self.pwd = senha

    def __str__(self):
        return "Usuario:{}".format(self.id)

# LOGANDO USUARIO

    def login_usuario(self, l, s):
        mycursor.execute("SELECT senha FROM funcionarios WHERE login = '%s'" %(l))
        myresult_1 = mycursor.fetchone()
        if myresult_1 != None:
            for x in myresult_1:
                x = str(x)
                if s == x:
                    mycursor.execute("SELECT nome FROM funcionarios WHERE login = '%s'" % (l))
                    myresult_2 = mycursor.fetchone()
                    for y in myresult_2:
                        print("Usuário", str(y), "logado com sucesso")
                    return True
                else:
                    print("Login ou Senha inválidos, tente mais uma vez")
                    return False
        else:
            print("Login ou Senha inválidos, tente mais uma vez")
            return False


from Conexao import Connection
from MapUsuario import Usuario

connection = Connection.create_session()

new_user = Usuario()
new_user.login = "vrau"
new_user.nome = "eu"
new_user.senha = "vrau"
connection.add(new_user)
connection.commit()
from Conexao import Connection
from MapUsuario import Usuario

connection = Connection.create_session()

usuario = Usuario('Joao', 'vrau', 'vrau')
connection.add(usuario)
connection.commit()

user = connection.query(Usuario).all()
print(user)


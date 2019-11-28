from Conexao import Connection
from MapUsuario import Usuario

connection = Connection.create_session()

#insert
if False:
    usuario = Usuario('Joao', 'vrau', 'vrau')
    connection.add(usuario)
    connection.commit()

#select all
if False:
    user = connection.query(Usuario).all()

    for i in user:
        print(i)

#select pelo id

if False:
    user = connection.query(Usuario).filter_by(id=1).first()
    print(user)

#alterar 
if False:
    user = connection.query(Usuario).filter_by(id=1).first()
    user.nome = 'Teste'
    connection.commit()
    print(user)

if False:
    user = connection.query(Usuario).filter_by(id=1).first()
    connection.delete(user)
    connection.commit()


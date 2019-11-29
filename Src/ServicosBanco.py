from Conexao import Connection
from MapUsuario import Usuario

class service:

    connection = Connection.create_session()

    #insert
    def inserir(nome ,usuario, senha):
        usuario = Usuario('Joao', 'vrau', 'vrau')
        connection.add(usuario)
        connection.commit()

    def select_all():
        user = connection.query(Usuario).all()
        return user

    #select pelo id

    def select_por_id(id : int):
        user = connection.query(Usuario).filter_by(id=id).first()
        return user

    def select_por_nome(nome):
        user = connection.query(Usuario).filter_by(nome=nome).first()
        return user

    #alterar 
    def alterar_nome(nome_primario, nome_alterado)
        user = connection.query(Usuario).filter_by(nome=nome_primario).first()
        user.nome = nome
        connection.commit()

    def excluir_nome(nome)
        user = connection.query(Usuario).filter_by(nome=nome).first()
        connection.delete(user)
        connection.commit()


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'users'

#so funciona com id auto increment

    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    usuario = Column(String(80))
    senha = Column(String(80))

    def __init__(self, nome, login, password):
        self.nome = nome
        self.usuario = login
        self.senha = password

    def __str__(self):
        return f'Nome: {self.nome} Usuario: {self.usuario} Senha: {self.senha}\n'
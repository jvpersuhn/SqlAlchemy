from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    usuario = Column(String(80))
    senha = Column(String(80))

    # def __init__(self, nome, login, password):
    #     self.nome = nome
    #     self.login = login
    #     self.senha = senha

    def __repr__(self):
        return '<users(%s,%s,%s)' % (self.nome, self.usuario, self.senha)
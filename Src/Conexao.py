from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Connection:
    
    def create_session():
        connection_string = 'mysql+pymysql://%s:%s@%s:%s/%s' % (
        "root", #usuario
        ""    , #senha
        "localhost", #host
        "3306", #porta
        "Usuario" #nome do banco
        )

        #echo true para debugar

        engine = create_engine(connection_string, echo = False)
        Session = sessionmaker(bind = engine)
        session = Session()

        return session
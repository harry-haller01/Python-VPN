from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

class DbInit():
    def __init__(self):
        engine = create_engine('sqlite:///database_context.db', echo=True)
        declarative_base().metadata.create_all(engine)
        session = sessionmaker(bind=engine)
        self.session = session()

class User(declarative_base()):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    virtual_ip = Column(String)

'''for i in range(20):
    new_user = User(name=str(random()), password='Dariel.01')
    session.add(new_user)

session.commit()

registros = session.query(User).all()
for registro in registros:
    print(registro.name, registro.password)'''
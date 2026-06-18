# Mapowanie obiektowo-relacyjne (ang. Object-Relational Mapping – ORM) –
# sposób odwzorowania obiektowej architektury systemu informatycznego na bazę danych (lub inny element systemu)
# o relacyjnym charakterze.

# orm w pythonie -> peewe, sqlalchemy
# pip install sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# echo=True - włączenie logów bazy
engine = create_engine('sqlite:///moja_baza.db', echo=True)
Base = declarative_base()


# model, encja - klasa odwzorowująca tabele w bazie danych
class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)

    def __repr__(self):
        return f"{self.name}"


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person(name="Radek", age="23")
session.add(person)
session.commit()
# INSERT INTO person (name, age) VALUES (?, ?) ('Radek', '23')

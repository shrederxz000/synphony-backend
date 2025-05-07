from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///mydatabase.db")


Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    email = Column(String(100), unique=True)

# Создание таблиц в БД
Base.metadata.create_all(engine)


# Добавление записи
new_user = User(name="Anya", email="anyadura@example.com")
session.add(new_user)
session.commit()

# Запрос данных
user = session.query(User).filter_by(name="Alice").first
print(user.id, user.name)

session.close()  # важно закрывать сессию!

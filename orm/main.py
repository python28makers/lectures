""" 
ORM - Object Relational Mapping - технология, которая позволяет управлять БД через код.

SQLAlchemy
Peewee
TortoiseORM
SQLModel
"""
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select

# ссылка на БД
db_url = '{engine}://{user}:{password}@{host}:{port}/{db_name}'.format(
    engine='postgresql',
    user='tima',
    password='1',
    host='localhost',
    port=5432,
    db_name='sqlmodel_db'
)

# соединение с БД
engine = create_engine(db_url)


def get_session():
    return Session(engine)


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(max_length=255)
    email: str = Field(unique=True)


SQLModel.metadata.create_all(engine)


def create_user(username, email):
    with get_session() as session:
        user = User(username=username, email=email)
        session.add(user)
        session.commit()


# create_user('Michael', 'michael.jackson@gmail.com')
# create_user('Saul', 'saul.goodman@gmail.com')
# create_user('Till', 'till.lindemann@gmail.com')

def get_users():
    with get_session() as session:
        statement = select(User)
        result = session.exec(statement)
        return list(result)


# users = get_users()

def get_one_user(id):
    with get_session() as session:
        return session.exec(select(User).where(User.id == id)).first()


print(get_one_user(3))


# def update_user(id, username):
#     with get_session() as session:
#         user = session.exec(select(User).where(User.id == id)).one()
#         user.username = username
#         session.add(user)
#         session.commit()
#         session.refresh(user)
#         return user


# print(update_user(2, 'Kirill'))


def delete_user(id):
    with get_session() as session:
        user = session.exec(select(User).where(User.id == id)).one()
        session.delete(user)
        session.commit()


# delete_user(2)

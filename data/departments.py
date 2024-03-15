import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Departments(SqlAlchemyBase):
    __tablename__ = 'departments'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    chief = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    members = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    user = orm.relationship("User")


db = input()
global_init(db)
sess = create_session()
for user in sess.query(User).filter(Department.id == 1):
    print(user.name)
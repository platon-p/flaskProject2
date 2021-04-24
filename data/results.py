import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Result(SqlAlchemyBase, UserMixin):
    __tablename__ = 'results'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.ForeignKey("users.id"))
    lesson_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    percent = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user = orm.relation('User')
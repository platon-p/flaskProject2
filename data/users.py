import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    email = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    school_class = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True)
    admin = sqlalchemy.Column(sqlalchemy.Boolean, nullable=True)
    results = orm.relation("Lessons",
                           secondary="results",
                           backref="users")

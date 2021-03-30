import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Test(SqlAlchemyBase):
    __tablename__ = 'tests'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    category_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("categories.id"))
    path_to_html = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    results = orm.relation("User",
                           secondary="results",
                           backref="tests")

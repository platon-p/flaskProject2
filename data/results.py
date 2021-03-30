import sqlalchemy
from .db_session import SqlAlchemyBase


association_table = sqlalchemy.Table(
    'results',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('user_id', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('users.id')),
    sqlalchemy.Column('test_id', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('tests.id')),
    sqlalchemy.Column('result', sqlalchemy.Integer)
)
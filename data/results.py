import sqlalchemy

from .db_session import SqlAlchemyBase

association_table = sqlalchemy.Table(
    'results',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('user_id', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('users.id')),
    sqlalchemy.Column('lessons_name', sqlalchemy.String),
    sqlalchemy.Column('percent', sqlalchemy.String)
)

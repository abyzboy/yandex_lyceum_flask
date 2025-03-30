import sqlalchemy
from database.db_session import SqlAlchemyBase

users_to_jobs = sqlalchemy.Table(
    'users_to_jobs',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('jobs', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('jobs.id')),
    sqlalchemy.Column('users', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('users.id'))
)
users_to_departments = sqlalchemy.Table(
    'users_to_department',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('departments', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('departments.id')),
    sqlalchemy.Column('users', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('users.id'))
)

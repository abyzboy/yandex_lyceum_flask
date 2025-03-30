import datetime
import sqlalchemy
from sqlalchemy import orm
from database.db_session import SqlAlchemyBase


class Department(SqlAlchemyBase):
    __tablename__ = 'departments'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    chief = orm.relationship('User')
    title = sqlalchemy.Column(sqlalchemy.String)
    chief_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    members = orm.relationship("User",
                               secondary="users_to_department",
                               back_populates="departments")
    email = sqlalchemy.Column(sqlalchemy.String)

    def get_members_by_id_to_string(self):
        return ', '.join([str(x.id) for x in self.members])

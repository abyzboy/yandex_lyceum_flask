import datetime
import sqlalchemy
from sqlalchemy import orm
from database.db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    team_leader = orm.relationship('User')
    team_leader_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    job = sqlalchemy.Column(sqlalchemy.String)
    work_size = sqlalchemy.Column(sqlalchemy.Integer)
    collaborators = orm.relationship("User",
                                     secondary="users_to_jobs",
                                     back_populates="collaborators_jobs")
    start_date = sqlalchemy.Column(sqlalchemy.DateTime)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean)

    def get_collabarators_by_id_to_string(self):
        return ', '.join([str(x.id) for x in self.collaborators])

    def get_is_finsihed_to_string(self):
        if self.is_finished:
            return 'Is finished'
        return 'Is not finished'

import datetime
import sqlalchemy
from sqlalchemy import orm
from database.db_session import SqlAlchemyBase, create_session
from flask_login import UserMixin
from extensions import login_manager


@login_manager.user_loader
def load_user(user_id):
    return create_session().query(User).filter(User.id == user_id).first()


class User(UserMixin, SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    surname = sqlalchemy.Column(sqlalchemy.String)
    age = sqlalchemy.Column(sqlalchemy.Integer)
    position = sqlalchemy.Column(sqlalchemy.String)
    speciality = sqlalchemy.Column(sqlalchemy.String)
    address = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime)
    collaborators_jobs = orm.relationship("Jobs",
                                          secondary="users_to_jobs",
                                          back_populates="collaborators")
    created_jobs = orm.relationship('Jobs', back_populates='team_leader')
    departments = orm.relationship("Department",
                                   secondary="users_to_department",
                                   back_populates="members")

    def __repr__(self):
        return f'<Colonist> {self.id} {self.surname} {self.name}'

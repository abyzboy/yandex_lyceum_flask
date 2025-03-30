from database import db_session
from sqlalchemy.orm import Session
from models.all_models import *


def add_collaborator(db_ses: Session, job: Jobs, collaborator_id):
    collaborator = db_ses.query(User).filter(
        User.id == collaborator_id).first()
    if collaborator:
        job.collaborators.append(collaborator)


def add_members(db_ses: Session, department: Department, member_id):
    member = db_ses.query(User).filter(
        User.id == member_id).first()
    if member:
        department.members.append(member)


def add_user(db_ses: Session, surname, name, age, position, speciality, address, email, hashed_password):
    user = User(surname=surname, name=name, age=age, position=position,
                speciality=speciality, address=address, email=email, hashed_password=hashed_password)
    # Проверка существует ли пользователь с такой же почтой
    if not db_ses.query(User).filter(User.email == email).first():
        db_ses.add(user)
        db_ses.commit()
    return user


def add_job(db_ses: Session, team_leader_id, job, work_size, collaborators, start_date, is_finished):
    user = db_ses.query(User).filter(User.id == team_leader_id).first()
    db_ses.close()
    job = Jobs(team_leader=user, job=job, work_size=work_size, start_date=start_date,
               is_finished=is_finished)
    db_ses.add(job)
    for collaborator in collaborators:
        add_collaborator(db_ses, job, collaborator)
    db_ses.commit()
    db_ses.close()

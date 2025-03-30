from database.db_session import create_session, global_init
from models.all_models import *
import sqlalchemy

s = input()
global_init('app\\mars_explorer.sqlite')
db_ses = create_session()
department = db_ses.query(Department).filter(Department.id == 1).first()
for mem_id in department.members:
    user = db_ses.query(User).filter(User.id == mem_id).first()
    hrs = 0
    jobs = db_ses.query(Jobs).all()
    for job in jobs:
        n = job.collaborators.replace(',', ' ')
        n = n.split()
        if str(mem_id) in n and job.is_finished:
            hrs += job.work_size
    if hrs > 25:
        print(user.surname + ' ' + user.name)

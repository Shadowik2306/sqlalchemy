from flask import Flask
from data import db_session
from data.users import User
from data.job import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def new_users():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    user = User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.age = 21
    user.position = 'capitan'
    user.speciality = 'speciality research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    db_sess.add(user)
    db_sess.commit()
    user = User()
    user.surname = 'Scott1'
    user.name = 'Ridley1'
    user.age = 21
    user.position = 'capitan'
    user.speciality = 'speciality research engineer'
    user.address = 'module_1'
    user.email = 'scott1_chief@mars.org'
    db_sess.add(user)
    db_sess.commit()
    user = User()
    user.surname = 'Scott2'
    user.name = 'Ridley2'
    user.age = 21
    user.position = 'capitan'
    user.speciality = 'speciality research engineer'
    user.address = 'module_1'
    user.email = 'scott2_chief@mars.org'
    db_sess.add(user)
    db_sess.commit()

def new_job():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.is_finished = False
    db_sess.add(job)
    db_sess.commit()

def main():
    new_job()


if __name__ == '__main__':
    main()
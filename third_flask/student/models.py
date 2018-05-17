from datetime import datetime

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Grade(db.Model):

    g_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    g_name = db.Column(db.String(10), unique=True)
    g_desc = db.Column(db.String(100), nullable=True)
    g_time = db.Column(db.Date, default=datetime.now)
    students = db.relationship('Student', backref='stu', lazy=True)

    __tablename__ = 'grade'

    def __init__(self, name, desc):
        self.g_name = name
        self.g_desc = desc


class Student(db.Model):

    s_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_name = db.Column(db.String(20), unique=True)
    s_age = db.Column(db.Integer, default=18)
    s_g = db.Column(db.Integer, db.ForeignKey('grade.g_id'), nullable=True)

    __tablename__ = 'student'

    def __init__(self, name, age):

        self.s_name = name
        self.s_age = age

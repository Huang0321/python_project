from flask import Blueprint, render_template

from student.models import db, Grade

grade = Blueprint('grade', __name__)


@grade.route('/')
def get_grade():

    return '班级'


@grade.route('/createdb/')
def create_db():
    db.create_all()

    return '创建成功'


@grade.route('/creategrade/')
def create_grade():
    names = {
        'python': 'Life is too short, I use Python',
        'H5': '这里妹子多',
        'Java': '假的吧',
        'PHP': '又是前端！'
    }
    grades_list = []
    for key, value in names.items():
        grade = Grade(key, value)
        grades_list.append(grade)
    db.session.add_all(grades_list)
    db.session.commit()

    return '创建班级成功'


@grade.route('/selstubygrade/<int:id>/')
def select_stu_by_grade(id):

    grade = Grade.query.get(id)
    stus = grade.students

    return render_template('grade_student.html', stus=stus, grade=grade)

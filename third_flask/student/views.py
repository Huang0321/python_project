
from flask import Blueprint, request, render_template
from sqlalchemy import and_, or_, not_

from student.models import db, Student

stu = Blueprint('stu', __name__)


@stu.route('/')
def index():

    return 'hello'


@stu.route('/createdb/')
def create_db():
    db.create_all()
    return '创建成功'


@stu.route('/dropdb/')
def drop_db():
    db.drop_all()
    return '删除数据表成功'


@stu.route('/createstu/', methods=['GET', 'POST'])
def create_stu():

    if request.method == 'GET':

        return render_template('create.html')

    if request.method == 'POST':
        s_name = request.form.get('s_name')
        s_age = request.form['s_age']
        stus = Student(s_name, s_age)

        db.session.add(stus)
        db.session.commit()

        return '添加成功'


@stu.route('/createstudents/', methods=['GET', 'POST'])
def create_students():

    if request.method == 'GET':
        return render_template('create_students.html')

    if request.method == 'POST':

        # 不可以这样
        s1name = request.form.get('s1name')
        s2name = request.form.get('s2name')
        s1age = request.form.get('s1age')
        s2age = request.form.get('s2age')

        stus_list = [Student(s1name, s1age), Student(s2name, s2age)]

        db.session.add_all(stus_list)
        db.session.commit()

        return '创建成功'


@stu.route('/selectstu/')
def sel_stu():

    # 年龄小于16岁的学生
    # 第一种写法
    # stus = Student.query.filter(Student.s_age < 16)

    #第二种写法
    # lt 小于, le 小于等于 同理（gt, ge)
    stus = Student.query.filter(Student.s_age.__lt__(16))

    # 年龄在某个列表值的学生
    stus = Student.query.filter(Student.s_age.in_([12, 17, 18, 13, 9, 6]))
    # 年龄在某个范围的学生
    stus = Student.query.filter(Student.s_age.between(12, 18))

    # 原生sql排序 倒序
    sql = 'select * from student order by (-s_age)'
    stus = db.session.execute(sql)

    #排序 .all() 不可以接后面的order_by，因为order_by就相当于.all()后再order_by；  但是.filter可以接，也可以先order_by,再filter
    # offset() 等
    stus = Student.query.filter(Student.s_age.between(12, 18)).order_by('-s_age')
    stus = Student.query.order_by('-s_age').filter(Student.s_age.between(12, 18)).limit(3)

    # 获取id=24的学生
    stus = Student.query.filter(Student.s_id==24)
    # flask的get方法默认找到主键,并且get到的值可以为空，不报错
    stus = Student.query.get(24)

    # 多条件查询
    stus = Student.query.filter(Student.s_age.__le__(18), Student.s_name=='娃哈哈')

    # and
    stus = Student.query.filter(and_(Student.s_age==18, Student.s_name=='娃哈哈'))
    # or
    stus = Student.query.filter(or_(Student.s_age==18, Student.s_name=='娃哈哈'))
    #not
    stus = Student.query.filter(not_(and_(Student.s_age==18, Student.s_name=='娃哈哈')))
    return render_template('students_list.html', stus=stus)


@stu.route('/stupage/')
def stu_page():

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    paginate = Student.query.order_by('-s_id').paginate(page, per_page, error_out=False)

    stus = paginate.items

    return render_template('stu_page.html', paginate=paginate, stus=stus)


@stu.route('/selgradebystu/<int:id>/')
def sel_grade_by_stu(id):

    stu = Student.query.get(id)
    grade = stu.stu

    return render_template('stu_grade.html', stu=stu, grade=grade)
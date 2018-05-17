import random

from flask import Blueprint, render_template, redirect, url_for
from student.models import db, Student

stu = Blueprint('stu', __name__)


@stu.route('/')
def index():

    return render_template('index.html')


@stu.route('/scores/')
def scores():

    scores_list = [21, 34, 32, 67, 89, 43, 22, 13]
    content_h2 = ' <p> you are a sb </p> '

    return render_template('scores.html', scores=scores_list, content_h2=content_h2)


@stu.route('/createdb/')
def create_db():

    # 创建表格
    db.create_all()

    # 删除表格
    # db.drop_all()

    return '创建成功'


@stu.route('/createstu/')
def create_stu():
    my_names = '我去年买了个表明刚新小大王锤红天飞翔的呵哇丁靠酷'
    name = ''

    for index in range(20):
        stu = Student()
        for _ in range(3):
            name += random.choice(my_names)
        stu.s_name = name
        stu.s_age = '%d' % random.randrange(20)

        db.session.add(stu)
        db.session.commit()
        name = ''

    return '创建成功'


@stu.route('/stulist/')
def stu_all():

    # 第一种方法 可以写原生的sql语句
    sql = 'select * from student'
    stus = db.session.execute(sql)

    # 第二种方法
    # stus = Student.query.all()

    return render_template('stulist.html', stus=stus)


@stu.route('/studentall/')
def stu_detail():

    # 第一种方法使用原生sql
    # sql = 'select * from student where s_name="丁飞哇"'
    # stus = db.session.execute(sql)

    # 第二种方法使用 filter
        # 第一种写法
        # 后面加 .all 就直接获取了具体对象
    # stus = Student.query.filter(Student.s_name=='丁飞哇')

    # 第三种写法 使用filter_by
       # 后面加 all() 或不加, 效果一样
    stus = Student.query.filter_by(s_id=22).all()

    return render_template('stulist.html', stus=stus)


@stu.route('/updatestu/')
def update_stu():

    # 第一种方式
    # stu = Student.query.filter_by(s_name='丁飞哇')  # 后面加 .first() 就等于stu[0]
    # stu[0].s_name = '丁牛哇'  # 等于 stu.first().s_name
    # db.session.commit()

    # 第二种方式
    Student.query.filter_by(s_id=26).update({'s_name': '丁狗哇'})

    # 第三种方式
    # Student.query.filter(Student.s_id==26).update({'s_name': '丁丁哇'})
    # 必须commit一下, 不然改不了数据库
    db.session.commit()

    return redirect(url_for('stu.stu_detail'))


@stu.route('/delstu/')
def del_stu():

    stu = Student.query.filter(Student.s_id==21)
    db.session.delete(stu[0])

    # 不commit只更改缓存, 但是改不了数据库
    db.session.commit()

    return redirect(url_for('stu.stu_detail'))
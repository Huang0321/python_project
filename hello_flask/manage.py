
from flask_script import Manager

from app import create_app
from Users import create_user_app

app1 = create_app()
app2 = create_user_app()
manager = Manager(app=app1)
manage = Manager(app=app2)


if __name__ == '__main__':

    # manager.run()
    manage.run()



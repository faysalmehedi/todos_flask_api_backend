from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server, Command, Option 

from core.flask_app import app 
from models.user import db 

migrate = Migrate(app, db)
manager = Manager(app) 
manager.add_command('db', MigrateCommand)

manager.add_command('db', MigrateCommand)

@manager.command
def create_db():
    db.create_all()

@manager.command
def drop_db():
    db.drop_all()


if __name__ == '__main__':
    manager.run()

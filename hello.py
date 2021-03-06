import os
from flask import Flask
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin(app)
manager = Manager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['DEBUG'] = True
try: from localconfig import *
except ImportError: pass

manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()

@app.route('/')
def hello():
	return 'Hello World!'
	
class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Unicode(120))
	text = db.Column(db.UnicodeText, nullable=False)

admin.add_view(ModelView(Post, db.session))

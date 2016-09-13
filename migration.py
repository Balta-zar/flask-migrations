from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand, init, migrate, upgrade

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'

db = SQLAlchemy(app)
migrates = Migrate(app, db)
migrates.init_app(app, db) # nije neophodna linija

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    
    # Add next line in project for second migration
    first_name = db.Column(db.String(128))
    
with app.app_context():
    try:
        init()
    except:
        print 'initialized'
    migrate()
    upgrade()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from application.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# If a user who is not logged in tries to view a protected page,
# Flask-Login will automatically redirect the user to the login
# form, and only redirect back to the page the user wanted to
# view after the login process is complete
login = LoginManager(app)
login.login_view = 'login'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from application import routes, models

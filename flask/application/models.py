from flask_login import UserMixin
from datetime import datetime
from application import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5


class User(UserMixin, db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    username      = db.Column(db.String(64), index=True, unique=True)
    email         = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # use class name; not an actual field, but a high-level view of relationship between users and posts
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        res = check_password_hash(self.password_hash, password)
        print(f'res={res}')
        return res

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{digest}?d=monsterid&s={size}'

    def __repr__(self):
        return f'Id={self.id},User={self.username},Email={self.email}'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # use table name

    def __repr__(self):
        return f'Id={self.id},UserId={self.user_id},Body={self.body}'


@login.user_loader
def load_user(id): # id will be a string
    return User.query.get(int(id))

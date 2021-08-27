"""
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
SQL-Alchemy: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
"""

from application import app, db
from application.models import User, Post


def test():
    for u in User.query.all():
        db.session.delete(u)
    for p in Post.query.all():
        db.session.delete(p)
    db.session.commit()


# when the flask shell command runs, it will invoke this function
# and register the items returned by it in the shell session
@app.shell_context_processor
def make_shell_context():
    # they keys represent future variable names in the shell interpreter
    return {'db': db, 'User': User, 'Post': Post}


if __name__ == '__main__':
    app.run(debug=True)
    # test()

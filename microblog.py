from microblog.flaskApp import app, db
from microblog.flaskApp.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

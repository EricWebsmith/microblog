from app import myapp, db, cli
from app.models import User, Post

@myapp.shell_context_processor
def make_content_processor():
    return {'db': db, 'User': User, 'Post': Post}


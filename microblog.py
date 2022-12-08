from app import cli, create_app, db
from app.models import *

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_content_processor():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
            'Notification': Notification}


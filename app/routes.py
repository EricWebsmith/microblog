from flask import render_template

from app import myapp

posts = [
    {
        'author': {'username': 'John'},
        'body': 'Beautiful day in Portland!'
    },
    {
        'author': {'username': 'Susan'},
        'body': 'The Avengers movie was so cool!'
    }
]


@myapp.route('/')
@myapp.route('/index')
def index():
    return render_template('index.html', title='Home', user={'username': 'Eric'}, posts=posts)


@myapp.route('/1')
def index1():
    return render_template('index.html', user={'username': 'Eric'})

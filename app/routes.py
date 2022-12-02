from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

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

@myapp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html',title='Sign In', form=form)
from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user
from app.forms import LoginForm

from app import myapp
from app.models import User


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
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember_me=form.remember_me)
        return redirect(url_for('index'))
    return render_template('login.html',title='Sign In', form=form)
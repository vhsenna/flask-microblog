from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Victor'}
    posts = [
        {
            'author': {'username': 'Maria'},
            'body': 'Beautiful day in Recife!'
        },
        {
            'author': {'username': 'João'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

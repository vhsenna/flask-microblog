from flask import render_template
from app import app

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

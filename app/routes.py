from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Tiago'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Sao Paulo!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'SPFC always makes me sad!'
        }
    ]
    return render_template('index.html', title='Sweet Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
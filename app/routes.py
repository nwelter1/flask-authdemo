from app import app, db
from flask import render_template, request, url_for, redirect
from app.models import User
from flask_login import login_required, login_user, current_user, logout_user

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        res = request.form
        name = res['name']
        email = res['email']
        password = res['password']
        print(name, email, password)
        u = User(name=name, email=email, password=password)
        db.session.add(u)
        db.session.commit()
        print(u)

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =='POST':
        res = request.form
        email = res['email']
        password = res['password']
        logged_user = User.query.filter(User.email == email).first()
        print(email, password)
        if logged_user and logged_user.password == password:
            login_user(logged_user)
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))
    
    return render_template('login.html')

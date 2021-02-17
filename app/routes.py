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
        #grabbing name, email, pw data from form on register page
        name = res['name']
        email = res['email']
        password = res['password']
        #double checking that the data came through
        print(name, email, password)
        #instantiating a new User Class
        u = User(name=name, email=email, password=password)
        #adding and committing my new user to the user table in the db
        db.session.add(u)
        db.session.commit()

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method =='POST':
        res = request.form
        email = res['email']
        password = res['password']
        #querying my all of my Users by email to see if the person loggin in matches someone in my db
        logged_user = User.query.filter(User.email == email).first()
        print(email, password)
        #if that person is in my db, and the password they entered matches the records for that email address
        #log them in and bring them to index.html
        if logged_user and logged_user.password == password:
            login_user(logged_user)
            return redirect(url_for('index'))
        #if not bring them right back to the login page
        else:
            return redirect(url_for('login'))
    
    return render_template('login.html')

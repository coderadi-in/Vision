'''coderadi &bull; Authentication routing file for the Project.'''

# ? IMPORTING LIBRARIES
from flask import Blueprint, render_template, redirect, url_for, flash, request
from plugins import *
from plugins.models import *

# ! BUILDING AUTH ROUTER
auth_router = Blueprint('auth_router', __name__, url_prefix='/auth')

# & SIGNUP ROUTE
@auth_router.route('/signup/', methods=['POST'])
def handle_signup():
    email = request.form.get('email')
    password = request.form.get('password')

    if (User.query.filter_by(email=email).first()):
        return render_template('auth/login.html', data={
            'email': email,
            'password': password
        })

    return render_template('auth/signup.html', data={
        'email': email,
        'password': password
    })

# & CREATE-ACCOUNT ROUTE
@auth_router.route('/create-account/', methods=['GET', 'POST'])
def handle_acc_creation():
    if (request.method == 'GET'): return render_template('auth/signup.html')

    else:
        name = request.form.get('full-name')
        username = request.form.get('handle')
        email = request.form.get('email')
        password = request.form.get('password')

        if (User.query.filter_by(email=email).first()):
            flash("This email already exists! Try logging in instead.", "error")
            return redirect(url_for('auth_router.handle_login'))
        
        new_user = User(
            name=name,
            username=username,
            email=email,
            password=bcrypt.generate_password_hash(password)
        )

        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash("You're logged in.", "success")
        flash("Welcome to Vision.", "success")
        return redirect(url_for('base_router.open_dashboard'))

# & LOGIN ROUTE
@auth_router.route('/login/', methods=['GET', 'POST'])
def handle_login():
    if (request.method == 'GET'): return render_template('auth/login.html')

    else:
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if (not user):
            flash("This email doesn't exist, try signing in instead.", "warning")
            print("This email doesn't exist, try signing in instead.")
            return redirect(url_for('auth_router.handle_login'))
        
        if (not bcrypt.check_password_hash(user.password, password)):
            flash("Incorrect password!", "error")
            print("Incorrect password!")
            return redirect(url_for('auth_router.handle_login'))
        
        login_user(user)
        flash("You're logged in.", "success")
        flash("Welcome back!", "success")
        return redirect(url_for('base_router.open_dashboard'))
    
# & LOGOUT ROUTE
@auth_router.route('/logout/')
def handle_logout():
    logout_user()
    flash("You're logged out.", "success")
    return redirect(url_for('base_router.base_index'))
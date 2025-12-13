'''coderadi &bull; Authentication routing file for the Project.'''

# ? IMPORTING LIBRARIES
from flask import Blueprint, render_template, redirect, url_for, flash, request
from plugins import *

# ! BUILDING AUTH ROUTER
auth_router = Blueprint('auth_router', __name__, url_prefix='/auth')

# & SIGNUP ROUTE
@auth_router.route('/signup/', methods=['POST'])
def handle_login():
    email = request.form.get('email')
    password = request.form.get('password')

    return render_template('auth/signup.html', data={
        'email': email,
        'password': password
    })
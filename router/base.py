'''coderadi &bull; Base routing file for the Project.'''

# ? IMPORTING LIBRARIES
from flask import Blueprint, render_template, redirect, url_for, flash, request
from plugins import *
from plugins.models import *

# ! BUILDING BASE ROUTER
base_router = Blueprint('base_router', __name__)

# * FUNCTION TO CHECK IF USER IS LOGGED IN
def authenticate():
    '''Checks if the user is logged in.'''

    if (not current_user.is_authenticated):
        flash("You need to log in before using the app.", "warning")
        return redirect('auth_router.login')

# & BASE ROUTE
@base_router.route('/')
def base_index():
    if (current_user.is_authenticated):
        return redirect(url_for('base_route.dashboard'))
    return render_template('pages/index.html')

# & DASHBOARD ROUTE
@base_router.route('/dashboard')
def open_dashboard():
    authenticate()
    return render_template('pages/dashboard.html')
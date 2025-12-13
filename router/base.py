'''coderadi &bull; Base routing file for the Project.'''

# ? IMPORTING LIBRARIES
from flask import Blueprint, render_template, redirect, url_for, flash, request
from plugins import *

# ! BUILDING BASE ROUTER
base_router = Blueprint('base_route', __name__)

# & BASE ROUTE
@base_router.route('/')
def base_index():
    if (current_user.is_authenticated):
        return redirect(url_for('base_route.dashboard'))
    return render_template('pages/index.html')

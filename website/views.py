from flask import Blueprint, render_template # bp means bunch of routes defined
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/') #decorator + route
@login_required
def home(): # will run for root page
    return render_template("home.html", user=current_user)
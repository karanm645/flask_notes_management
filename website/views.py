# where users can go to
# anything unrelated to authentication
from flask import Blueprint # bp means bunch of routes defined
views = Blueprint('views', __name__)

@views.route('/') #decorator + route
def home(): # will run for root page
    return "<h1>Test</h1>"
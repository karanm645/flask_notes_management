from flask import Blueprint, render_template  # bp means bunch of routes defined

auth = Blueprint("auth", __name__)

@auth.route('/login')
def login():
    return render_template("login.html", text="testing", user="Karan")

@auth.route('/logout')
def logout():
    return render_template("login.html", text="testing", user="Karan")

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html", boolean=True)

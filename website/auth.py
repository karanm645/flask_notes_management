from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint("auth", __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", text="testing", user="Karan")

@auth.route('/logout')
def logout():
    return render_template("login.html", text="testing", user="Karan")


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == 'POST': 
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4: 
            flash("Email must be greater than three characters", category="error")
        elif len(first_name) < 2: 
            flash("First name must be greater than one character", category="error")
        elif len(password1) < 7:
            flash("Password must be greater than seven characters", category="error")
        elif password1 != password2:
            flash("Passwords don\'t match", category="error")
        else:
            new_user = User(
                email=email,
                first_name=first_name,
                password=generate_password_hash(password1, method="scrypt")
            )
            db.session.add(new_user)
            db.session.commit()
            flash("Account created!", category="success")
            return redirect(url_for('views.home'))
            # add user to database

    return render_template("sign_up.html", boolean=True)

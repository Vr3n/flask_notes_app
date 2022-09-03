
from flask import Blueprint, render_template

# Think of this as Urls.
auth_views = Blueprint('auth_views', __name__)


@auth_views.route("login/")
def login():
    return render_template("login.html")


@auth_views.route("logout/")
def logout():
    return "<p>logout</p>"


@auth_views.route("sign-up/")
def sign_up():
    return render_template("sign_up.html")

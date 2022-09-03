from flask import Blueprint, render_template, request, flash

# Think of this as Urls.
auth_views = Blueprint('auth_views', __name__)


@auth_views.route("login/", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@auth_views.route("sign-up/", methods=["GET", "POST"])
def sign_up():
    data = None
    if request.method == "POST":
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash("Email must be greater than 4 characters.", category="error")
        elif len(first_name) < 2:
            flash("First Name must be greater than 2 characters.", category="error")
        elif password1 != password2:
            flash("Your passwords don't match.", category="error")
        elif len(password1) < 7:
            flash("Your is too short! should be atleast 8 characters.",
                  category="error")
        else:
            flash("Account Created Successfully!", category="success")

    return render_template("sign_up.html")


@auth_views.route("logout/")
def logout():
    return "<p>logout</p>"

from flask import Blueprint, render_template

# Think of this as Urls.
views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")

from flask import Blueprint

# Think of this as Urls.
views = Blueprint('views', __name__)


@views.route('/')
def home():
    return "<h1>Hello, Flask!</h1>"

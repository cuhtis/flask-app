from flask import Blueprint, redirect, session, url_for, render_template

blueprint = Blueprint('index', __name__, template_folder='templates')

@blueprint.route('/')
def index():
    context = {
        "title": "Hello World!"
        }
    return render_template('index.html', context=context)

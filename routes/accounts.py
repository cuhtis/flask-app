from flask import Blueprint, redirect, session, url_for

blueprint = Blueprint('accounts', __name__, template_folder='templates')

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    session['logged_in'] = True
    return redirect(url_for('index'))

@blueprint.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))

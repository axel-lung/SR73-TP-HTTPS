# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""


from flask import Blueprint, render_template, flash, Flask
from flask_login import login_required, current_user
from __init__ import create_app, db
# définir le message secret
SECRET_MESSAGE = "Message secret de Axel" # A modifier
# app = Flask(__name__)

main = Blueprint('main', __name__)

@main.route('/') # home page that return 'index'
def index():
    return render_template('index.html')

@main.route('/profile') # profile page that return 'profile'
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

# @app.route("/")
# def get_secret_message():
#     return SECRET_MESSAGE
app = create_app()
if __name__ == "__main__":
    # HTTP version
    # app.run(debug=True, host="0.0.0.0", port=8081, ssl_context='adhoc')
    # HTTPS version
    # A compléter  : nécessité de déplacer les bons fichiers vers ce répertoire
    db.create_all(app=create_app())
    context = ('./resources/server-public-key.pem','./resources/server-private-key.pem')
    app.run(debug=True, host="0.0.0.0", port=8081, ssl_context=context)


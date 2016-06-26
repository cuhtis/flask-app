from flask import Flask
from db import *
from build.setup import setup

from routes.accounts import blueprint as accounts
from routes.index import blueprint as index

app = Flask(__name__)

setup(app);

app.register_blueprint(index)
app.register_blueprint(accounts)

if __name__ == "__main__":
    app.run()

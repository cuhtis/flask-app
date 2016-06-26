import os

def setup(app):
    app.config.from_object(__name__)

    app.config.update(dict(
        DATABASE=os.path.join(app.root_path, 'main.db'),
        SECRET_KEY='secret key',
        USERNAME='admin',
        PASSWORD='password'
    ))

    app.config.from_envvar('FS_SETTINGS', silent=True)

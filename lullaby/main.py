from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from lullaby.settings import PORT, DB_URI
from lullaby.api_urls import init_resources

from lullaby.database.migrations import upgrade


def make_app() -> Flask:
    flask = Flask(__name__)
    flask.url_map.strict_slashes = False
    flask.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    flask.config['SQLALCHEMY_ECHO'] = True
    flask.config['SQLALCHEMY_BINDS'] = {'default': DB_URI}

    flask.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy()
    db.init_app(flask)
    upgrade()

    return flask


app = make_app()
init_resources(app)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)

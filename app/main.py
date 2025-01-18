import os
from pathlib import Path

from flask import Flask

from app.base.views import base_bp
from app.extensions import ba, db, ma, migrate
from app.products.views import products_bp

APP_ROOT = Path(__file__).parent.absolute()


def create_app() -> Flask:
    from app.utils import inject_environment

    app = Flask(__name__, instance_path=str(APP_ROOT))
    app.config["SECRET_KEY"] = os.urandom(32)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

    app.register_blueprint(base_bp)
    app.register_blueprint(products_bp)

    db.init_app(app)
    migrate.init_app(app, db, directory="app/migrations")

    ma.init_app(app)

    ba.init_app(app, locale_selector=lambda: os.environ.get("LANG", "en"))

    app.context_processor(inject_environment)

    return app

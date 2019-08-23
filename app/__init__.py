from flask import Flask


def create_app():
    app = Flask(__name__, static_folder="../dist/static", template_folder="../dist")
    # blueprint
    from .client import client_bp
    app.register_blueprint(client_bp)

    # load settings
    app.config.from_object("app.config.GlobalConfig")
    
    return app
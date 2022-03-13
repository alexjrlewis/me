"""Module to initiate a flask application."""

import sys
from flask import Flask
# from flask_lnnode import LNNode
from flask_mail import Mail
from flask_qrcode import QRcode
from app.config.config import Config

# lnnode = LNNode()
mail = Mail()
qrcode = QRcode()

def create_app() -> Flask:
    """Initialize the core application and returns it.

    Returns:
        The initiated flask application.
    """

    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object(Config)

    # lnnode.init_app(app)  # initialize global variables
    mail.init_app(app)
    qrcode.init_app(app)

    with app.app_context():

        from app.views.about_bp import about_bp
        from app.views.contact_bp import contact_bp
        from app.views.index_bp import index_bp
        from app.views.pay_bp import pay_bp
        # from app.views.webhooks_bp import webhooks_bp

        app.register_blueprint(about_bp, url_prefix="/about")
        app.register_blueprint(contact_bp, url_prefix="/contact")
        app.register_blueprint(index_bp, url_prefix="/")
        app.register_blueprint(pay_bp, url_prefix="/pay")
        # app.register_blueprint(webhooks_bp, url_prefix="/webhooks")

        return app

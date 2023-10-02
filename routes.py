from flask import Blueprint
import views

routes_blueprint = Blueprint("routes", __name__)

routes_blueprint.route("/", methods=["GET", "POST"])(views.index)
routes_blueprint.route("/planets", methods=["GET", "POST"])(views.index)
routes_blueprint.route("/register", methods=["GET", "POST"])(views.register)
routes_blueprint.route("/logout", methods=["GET", "POST"])(views.logout)
routes_blueprint.route("/login", methods=["GET", "POST"])(views.login)


from flask import Blueprint

from app.controllers.auth_controller import AuthController


auth_bp = Blueprint(
    "auth",
    __name__
)

controller = AuthController()


@auth_bp.route("/", methods=["GET", "POST"])
def login():

    return controller.login()


@auth_bp.route("/logout")
def logout():

    return controller.logout()
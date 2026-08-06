from flask import Blueprint

from app.controllers.usuario_controller import UsuarioController

usuario_bp = Blueprint(
    "usuarios",
    __name__
)

controller = UsuarioController()


@usuario_bp.route("/usuarios")
def listar():

    return controller.listar()
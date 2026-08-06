from flask import Blueprint

from app.controllers.usuario_controller import UsuarioController
from app.utils.auth import admin_required

usuario_bp = Blueprint(
    "usuarios",
    __name__
)

controller = UsuarioController()

@usuario_bp.route("/usuarios")
@admin_required
def listar():

    return controller.listar()
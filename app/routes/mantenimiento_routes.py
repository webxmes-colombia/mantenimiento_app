from flask import Blueprint

from app.controllers.mantenimiento_controller import MantenimientoController

from app.utils.auth import login_required


mantenimiento_bp = Blueprint(
    "mantenimientos",
    __name__
)

controller = MantenimientoController()


@mantenimiento_bp.route("/mantenimientos")
@login_required
def listar():

    return controller.listar()


@mantenimiento_bp.route("/mantenimientos/nuevo")
@login_required
def nuevo():

    return controller.nuevo()


@mantenimiento_bp.route("/mantenimientos/guardar", methods=["POST"])
@login_required
def guardar():

    return controller.guardar()
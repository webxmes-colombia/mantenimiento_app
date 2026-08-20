from flask import Blueprint

from app.controllers.evidencia_controller import EvidenciaController

from app.utils.auth import login_required


evidencia_bp = Blueprint(
    "evidencias",
    __name__
)

controller = EvidenciaController()


@evidencia_bp.route("/evidencias/<int:mantenimiento_id>")
@login_required
def listar(mantenimiento_id):

    return controller.listar(mantenimiento_id)


@evidencia_bp.route(
    "/evidencias/subir/<int:mantenimiento_id>",
    methods=["POST"]
)
@login_required
def subir(mantenimiento_id):

    return controller.subir(mantenimiento_id)


@evidencia_bp.route(
    "/evidencias/eliminar/<int:id>"
)
@login_required
def eliminar(id):

    return controller.eliminar(id)
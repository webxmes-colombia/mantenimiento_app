from flask import Blueprint

from app.controllers.equipo_controller import EquipoController

from app.utils.auth import login_required


equipo_bp = Blueprint(
    "equipos",
    __name__
)

controller = EquipoController()


@equipo_bp.route("/equipos")
@login_required
def listar():

    return controller.listar()


@equipo_bp.route("/equipos/nuevo")
@login_required
def nuevo():

    return controller.nuevo()


@equipo_bp.route("/equipos/guardar", methods=["POST"])
@login_required
def guardar():

    return controller.guardar()


@equipo_bp.route("/equipos/editar/<int:id>")
@login_required
def editar(id):

    return controller.editar(id)


@equipo_bp.route("/equipos/actualizar/<int:id>", methods=["POST"])
@login_required
def actualizar(id):

    return controller.actualizar(id)


@equipo_bp.route("/equipos/eliminar/<int:id>")
@login_required
def eliminar(id):

    return controller.eliminar(id)
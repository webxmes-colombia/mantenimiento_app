from flask import Blueprint

from app.controllers.cliente_controller import ClienteController

from app.utils.auth import login_required


cliente_bp = Blueprint(
    "clientes",
    __name__
)

controller = ClienteController()


@cliente_bp.route("/clientes")
@login_required
def listar():

    return controller.listar()


@cliente_bp.route("/clientes/nuevo")
@login_required
def nuevo():

    return controller.nuevo()


@cliente_bp.route("/clientes/guardar", methods=["POST"])
@login_required
def guardar():

    return controller.guardar()


@cliente_bp.route("/clientes/editar/<int:id>")
@login_required
def editar(id):

    return controller.editar(id)


@cliente_bp.route("/clientes/actualizar/<int:id>", methods=["POST"])
@login_required
def actualizar(id):

    return controller.actualizar(id)

@cliente_bp.route("/clientes/eliminar/<int:id>")
@login_required
def eliminar(id):

    return controller.eliminar(id)
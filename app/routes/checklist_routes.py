from flask import Blueprint

from app.controllers.checklist_controller import ChecklistController

from app.utils.auth import login_required


checklist_bp = Blueprint(
    "checklist",
    __name__
)

controller = ChecklistController()


@checklist_bp.route("/checklist")
@login_required
def nuevo():

    return controller.nuevo()


@checklist_bp.route("/checklist/equipo/<int:id>")
@login_required
def equipo(id):

    return controller.seleccionar(id)
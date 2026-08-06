from flask import Blueprint

from app.controllers.dashboard_controller import DashboardController
from app.utils.auth import login_required

dashboard_bp = Blueprint(

    "dashboard",

    __name__

)

controller = DashboardController()

@dashboard_bp.route("/dashboard")
@login_required
def dashboard():

    return controller.index()
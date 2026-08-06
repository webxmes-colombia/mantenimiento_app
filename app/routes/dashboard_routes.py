from flask import Blueprint

from app.controllers.dashboard_controller import DashboardController

dashboard_bp = Blueprint(

    "dashboard",

    __name__

)

controller = DashboardController()


@dashboard_bp.route("/dashboard")
def dashboard():

    return controller.index()
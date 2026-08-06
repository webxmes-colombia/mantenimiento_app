# ============================================
# CONTROLADOR DASHBOARD
# ============================================

from flask import render_template

from app.models.cliente import Cliente
from app.models.equipo import Equipo
from app.models.mantenimiento import Mantenimiento
from app.models.usuario import Usuario


class DashboardController:
    """
    Controlador del Dashboard.
    Obtiene toda la información necesaria para la pantalla principal.
    """

    def __init__(self):

        self.cliente = Cliente()
        self.equipo = Equipo()
        self.mantenimiento = Mantenimiento()
        self.usuario = Usuario()

    def index(self):
        """
        Carga la información del Dashboard.
        """

        datos = {

            "total_clientes": self.cliente.contar(),

            "total_equipos": self.equipo.contar(),

            "total_mantenimientos": self.mantenimiento.contar(),

            "total_tecnicos": self.usuario.contar_tecnicos(),

            "ultimos_clientes": self.cliente.ultimos(),

            "ultimos_equipos": self.equipo.ultimos()

        }

        return render_template(
            "dashboard/index.html",
            datos=datos
        )
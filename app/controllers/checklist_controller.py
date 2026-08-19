from flask import render_template

from app.models.equipo import Equipo


class ChecklistController:

    def __init__(self):

        self.modelo = Equipo()


    def nuevo(self):

        equipos = self.modelo.listar()

        return render_template(
            "checklist/formulario.html",
            equipos=equipos,
            equipo=None
        )


    def seleccionar(self, id):

        equipo = self.modelo.obtener(id)

        equipos = self.modelo.listar()

        return render_template(
            "checklist/formulario.html",
            equipos=equipos,
            equipo=equipo
        )
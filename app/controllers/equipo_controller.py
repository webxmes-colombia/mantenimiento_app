from flask import render_template
from flask import request
from flask import redirect

from app.models.equipo import Equipo
from app.models.cliente import Cliente


class EquipoController:

    def __init__(self):

        self.modelo = Equipo()

        self.cliente = Cliente()


    def listar(self):

        equipos = self.modelo.listar()

        return render_template(
            "equipos/listar.html",
            equipos=equipos
        )


    def nuevo(self):

        clientes = self.cliente.listar()

        return render_template(
            "equipos/formulario.html",
            equipo=None,
            clientes=clientes
        )


    def guardar(self):

        self.modelo.crear(request.form)

        return redirect("/equipos")


    def editar(self, id):

        equipo = self.modelo.obtener(id)

        clientes = self.cliente.listar()

        return render_template(
            "equipos/formulario.html",
            equipo=equipo,
            clientes=clientes
        )


    def actualizar(self, id):

        self.modelo.actualizar(id, request.form)

        return redirect("/equipos")


    def eliminar(self, id):

        self.modelo.eliminar(id)

        return redirect("/equipos")
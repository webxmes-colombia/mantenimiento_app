from flask import render_template
from flask import request
from flask import redirect

from app.models.cliente import Cliente


class ClienteController:

    def __init__(self):

        self.modelo = Cliente()


    def listar(self):

        clientes = self.modelo.listar()

        return render_template(
            "clientes/listar.html",
            clientes=clientes
        )


    def nuevo(self):

        return render_template(
            "clientes/formulario.html",
            cliente=None
        )


    def guardar(self):

        self.modelo.crear(request.form)

        return redirect("/clientes")
    
    def editar(self, id):

        cliente = self.modelo.obtener(id)

        return render_template(

            "clientes/formulario.html",

            cliente=cliente

        )


    def actualizar(self, id):

        self.modelo.actualizar(id, request.form)

        return redirect("/clientes")
    
    def eliminar(self, id):

        self.modelo.eliminar(id)

        return redirect("/clientes")
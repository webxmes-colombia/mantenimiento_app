from flask import render_template, request, redirect
from app.models.mantenimiento import Mantenimiento
from app.models.equipo import Equipo
from app.models.usuario import Usuario


class MantenimientoController:
    def __init__(self):
        self.modelo = Mantenimiento()
        self.equipo = Equipo()
        self.usuario = Usuario()

    def listar(self):
        return render_template("mantenimientos/listar.html", mantenimientos=self.modelo.listar())

    def nuevo(self):
        return render_template("mantenimientos/formulario.html", equipos=self.equipo.listar(), tecnicos=self.usuario.listar_tecnicos())

    def guardar(self):
        datos = dict(request.form)
        for campo in ("limpieza_realizada", "pasta_termica_aplicada", "antivirus_actualizado", "sistema_actualizado", "respaldo_verificado", "pruebas_funcionamiento"):
            datos[campo] = 1 if campo in request.form else 0
        datos["costo"] = datos.get("costo") or 0
        self.modelo.crear(datos)
        return redirect("/mantenimientos")

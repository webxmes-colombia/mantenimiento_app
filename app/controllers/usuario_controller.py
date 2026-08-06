# ============================================
# CONTROLADOR USUARIOS
# ============================================

from flask import render_template
from app.models.usuario import Usuario


class UsuarioController:

    def __init__(self):
        self.modelo = Usuario()

    def listar(self):

        usuarios = self.modelo.listar()

        return render_template(
            "usuarios/listar.html",
            usuarios=usuarios
        )
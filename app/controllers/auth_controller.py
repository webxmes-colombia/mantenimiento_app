# ============================================
# CONTROLADOR DE AUTENTICACIÓN
# ============================================

from flask import render_template
from flask import request
from flask import redirect
from flask import session
from flask import flash

from werkzeug.security import check_password_hash

from app.models.usuario import Usuario


class AuthController:

    def __init__(self):

        self.usuario = Usuario()

    def login(self):
        """
        Iniciar sesión.
        """

        if request.method == "POST":

            correo = request.form["email"]
            

            password = request.form["password"]

            usuario = self.usuario.login(correo)

            if usuario:

                if check_password_hash(
                        usuario["password_hash"],
                        password):

                    session["id"] = usuario["id"]

                    session["usuario"] = usuario["nombre"]

                    session["rol"] = usuario["rol"]

                    return redirect("/dashboard")

            flash(
                "Correo o contraseña incorrectos.",
                "danger"
            )

        return render_template("auth/login.html")

    def logout(self):

        session.clear()

        return redirect("/")

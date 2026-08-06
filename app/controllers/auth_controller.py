from flask import render_template
from flask import request
from flask import redirect
from flask import session

from app.models.usuario import Usuario

usuario_model = Usuario()


def login():

    if request.method == "POST":

        email = request.form["email"]

        password = request.form["password"]

        usuario = usuario_model.login(email, password)

        if usuario:

            session["usuario"] = usuario["nombre"]
            session["rol"] = usuario["rol"]

            return redirect("/dashboard")

        return render_template(
            "auth/login.html",
            error="Usuario o contraseña incorrectos"
        )

    return render_template("auth/login.html")
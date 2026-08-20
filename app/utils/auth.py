# ============================================
# DECORADORES DE AUTENTICACIÓN
# ============================================

from functools import wraps

from flask import session
from flask import redirect
from flask import flash


def login_required(func):
    """
    Permite acceder únicamente a usuarios autenticados.
    """

    @wraps(func)
    def decorated_function(*args, **kwargs):

        if "id" not in session:

            flash(
                "Debe iniciar sesión.",
                "warning"
            )

            return redirect("/")

        return func(*args, **kwargs)

    return decorated_function


def admin_required(func):
    """
    Permite acceder únicamente a administradores.
    """

    @wraps(func)
    def decorated_function(*args, **kwargs):

        if "id" not in session:

            flash(
                "Debe iniciar sesión.",
                "warning"
            )

            return redirect("/")

        if session.get("rol") != "admin":

            flash(
                "No tiene permisos para acceder.",
                "danger"
            )

            return redirect("/dashboard")

        return func(*args, **kwargs)

    return decorated_function

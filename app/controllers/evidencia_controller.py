import os

from flask import render_template
from flask import request
from flask import redirect
from flask import current_app
from werkzeug.utils import secure_filename

from app.models.evidencia import Evidencia


class EvidenciaController:

    def __init__(self):

        self.modelo = Evidencia()


    def listar(self, mantenimiento_id):

        evidencias = self.modelo.listar(mantenimiento_id)

        return render_template(
            "evidencias/listar.html",
            evidencias=evidencias,
            mantenimiento_id=mantenimiento_id
        )


    def subir(self, mantenimiento_id):

        archivo = request.files.get("archivo")

        tipo_evidencia = request.form.get("tipo_evidencia")

        descripcion = request.form.get("descripcion", "")

        if not archivo or archivo.filename == "":
            return redirect(
                f"/evidencias/{mantenimiento_id}"
            )

        nombre = secure_filename(archivo.filename)

        carpeta = os.path.join(
            current_app.config["UPLOAD_FOLDER"],
            "evidencias"
        )

        os.makedirs(carpeta, exist_ok=True)

        ruta = os.path.join(carpeta, nombre)

        archivo.save(ruta)

        ruta_bd = f"uploads/evidencias/{nombre}"

        self.modelo.crear(
            mantenimiento_id,
            tipo_evidencia,
            nombre,
            ruta_bd,
            archivo.content_type,
            descripcion
        )

        return redirect(
            f"/evidencias/{mantenimiento_id}"
        )


    def eliminar(self, id):

        self.modelo.eliminar(id)

        return redirect(request.referrer or "/")
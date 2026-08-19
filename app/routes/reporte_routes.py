from flask import Blueprint, render_template, request, send_file, abort

from app.models.reporte import Reporte
from app.utils.auth import login_required
from app.utils.pdf_reportes import generar_reporte_equipo


reporte_bp = Blueprint("reportes", __name__)

modelo_reporte = Reporte()


@reporte_bp.route("/reportes/equipos")
@login_required
def reporte_por_equipo():

    equipos = modelo_reporte.equipos()

    equipo_id = request.args.get("equipo_id", type=int)

    mantenimientos = []

    if equipo_id:
        mantenimientos = modelo_reporte.por_equipo(equipo_id)

    return render_template(
        "reportes/equipos.html",
        equipos=equipos,
        equipo_id=equipo_id,
        mantenimientos=mantenimientos
    )


@reporte_bp.route("/reportes/equipos/pdf")
@login_required
def descargar_reporte_equipo():

    equipo_id = request.args.get("equipo_id", type=int)

    if not equipo_id:
        abort(400)

    equipo = modelo_reporte.datos_equipo(equipo_id)

    if not equipo:
        abort(404)

    mantenimientos = modelo_reporte.por_equipo(equipo_id)

    archivo_pdf = generar_reporte_equipo(
        equipo,
        mantenimientos
    )

    return send_file(
        archivo_pdf,
        as_attachment=True,
        download_name=f"reporte_equipo_{equipo_id}.pdf",
        mimetype="application/pdf"
    )
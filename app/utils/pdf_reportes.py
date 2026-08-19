from io import BytesIO
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
   )


def texto(valor):
    if valor is None or valor == "":
        return "-"

    return escape(str(valor))


def celda(valor, estilo):
    return Paragraph(texto(valor), estilo)


def generar_reporte_equipo(equipo, mantenimientos):

    archivo = BytesIO()

    documento = SimpleDocTemplate(
        archivo,
        pagesize=landscape(letter),
        rightMargin=18,
        leftMargin=18,
        topMargin=18,
        bottomMargin=18
    )

    estilos = getSampleStyleSheet()

    titulo = estilos["Title"]
    subtitulo = estilos["Heading2"]
    normal = estilos["BodyText"]
    normal.fontSize = 7
    normal.leading = 8

    contenido = []

    contenido.append(
        Paragraph(
            "Reporte de mantenimiento de equipo",
            titulo
        )
    )

    contenido.append(Spacer(1, 12))

    contenido.append(
        Paragraph("Información del cliente", subtitulo)
    )

    datos_cliente = [
        [
            celda("Cliente", normal),
            celda(equipo["cliente"], normal),
            celda("NIT", normal),
            celda(equipo["nit"], normal)
        ],
        [
            celda("Contacto", normal),
            celda(equipo["contacto"], normal),
            celda("Teléfono", normal),
            celda(equipo["telefono"], normal)
        ],
        [
            celda("Correo", normal),
            celda(equipo["correo"], normal),
            celda("Ciudad", normal),
            celda(equipo["ciudad"], normal)
        ],
        [
            celda("Dirección", normal),
            celda(equipo["direccion"], normal),
            "",
            ""
        ]
    ]

    tabla_cliente = Table(
        datos_cliente,
        colWidths=[0.9 * inch, 2.55 * inch, 0.9 * inch, 2.55 * inch]
    )

    tabla_cliente.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#e9ecef")),
        ("BACKGROUND", (2, 0), (2, -1), colors.HexColor("#e9ecef")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("PADDING", (0, 0), (-1, -1), 3)
    ]))

    contenido.append(tabla_cliente)
    contenido.append(Spacer(1, 16))

    contenido.append(
        Paragraph("Ficha técnica del equipo", subtitulo)
    )

    datos_equipo = [
        [
            celda("Nombre", normal),
            celda(equipo["nombre_equipo"], normal),
            celda("Tipo", normal),
            celda(equipo["tipo"], normal)
        ],
        [
            celda("Marca / modelo", normal),
            celda(f'{equipo["marca"]} {equipo["modelo"]}', normal),
            celda("Serial", normal),
            celda(equipo["serial"], normal)
        ],
        [
            celda("Activo fijo", normal),
            celda(equipo["activo_fijo"], normal),
            celda("Ubicación", normal),
            celda(equipo["ubicacion"], normal)
        ],
        [
            celda("Dirección IP", normal),
            celda(equipo["direccion_ip"], normal),
            celda("Procesador", normal),
            celda(equipo["procesador"], normal)
        ],
        [
            celda("RAM", normal),
            celda(equipo["ram"], normal),
            celda("Tipo RAM", normal),
            celda(equipo["tipo_ram"], normal)
        ],
        [
            celda("Disco", normal),
            celda(equipo["disco"], normal),
            celda("Tipo disco", normal),
            celda(equipo["tipo_disco"], normal)
        ],
        [
            celda("Sistema operativo", normal),
            celda(equipo["sistema_operativo"], normal),
            celda("Antivirus", normal),
            celda(equipo["antivirus"], normal)
        ],
        [
            celda("Estado", normal),
            celda(equipo["estado"], normal),
            celda("Activo", normal),
            celda(equipo["activo"], normal)
        ],
        [
            celda("Fecha de ingreso", normal),
            celda(equipo["fecha_ingreso"], normal),
            "",
            ""
        ],
        [
            celda("Accesorios", normal),
            celda(equipo["accesorios"], normal),
            "",
            ""
        ],
        [
            celda("Observaciones", normal),
            celda(equipo["observaciones"], normal),
            "",
            ""
        ]
    ]

    tabla_equipo = Table(
        datos_equipo,
        colWidths=[1.15 * inch, 2.3 * inch, 1.15 * inch, 2.3 * inch]
    )

    tabla_equipo.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#e9ecef")),
        ("BACKGROUND", (2, 0), (2, -1), colors.HexColor("#e9ecef")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("PADDING", (0, 0), (-1, -1), 3),
        ("SPAN", (1, 8), (3, 8)),
        ("SPAN", (1, 9), (3, 9)),
        ("SPAN", (1, 10), (3, 10))
    ]))

    contenido.append(tabla_equipo)
    contenido.append(Spacer(1, 8))

    contenido.append(
        Paragraph("Historial de mantenimientos", subtitulo)
    )

    datos_mantenimientos = [[
        celda("Fecha", normal),
        celda("Técnico responsable", normal),
        celda("Tipo", normal),
        celda("Estado", normal),
        celda("Costo", normal),
        celda("Diagnóstico", normal)
    ]]

    for mantenimiento in mantenimientos:

        datos_mantenimientos.append([
            celda(mantenimiento["fecha_mantenimiento"], normal),
            celda(mantenimiento["tecnico"], normal),
            celda(mantenimiento["tipo_mantenimiento"], normal),
            celda(mantenimiento["estado"], normal),
            celda(f'${mantenimiento["costo"]}', normal),
            celda(mantenimiento["diagnostico"], normal)
        ])

    if not mantenimientos:

        datos_mantenimientos.append([
            celda("No hay mantenimientos registrados.", normal),
            "",
            "",
            "",
            "",
            ""
        ])

    tabla_mantenimientos = Table(
        datos_mantenimientos,
        repeatRows=1,
        colWidths=[
            1.0 * inch,
            1.35 * inch,
            1.0 * inch,
            1.0 * inch,
            0.8 * inch,
            3.0 * inch
        ]
    )

    tabla_mantenimientos.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0d6efd")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("PADDING", (0, 0), (-1, -1), 5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [
            colors.white,
            colors.HexColor("#f2f2f2")
        ])
    ]))

    contenido.append(tabla_mantenimientos)

    documento.build(contenido)

    archivo.seek(0)

    return archivo
# ============================================
# MODELO MANTENIMIENTO
# ============================================

from app.database import conectar


class Mantenimiento:
    """
    Modelo encargado de administrar la tabla mantenimientos.
    """

    def contar(self):

        conexion = conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""

            SELECT COUNT(*) AS total

            FROM mantenimientos

        """)

        resultado = cursor.fetchone()

        cursor.close()

        conexion.close()

        return resultado["total"]
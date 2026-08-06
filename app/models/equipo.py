# ============================================
# MODELO EQUIPO
# ============================================

from app.database import conectar


class Equipo:
    """
    Modelo encargado de administrar la tabla equipos.
    """

    def contar(self):
        """
        Retorna la cantidad de equipos registrados.
        """

        conexion = conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""
            SELECT COUNT(*) AS total
            FROM equipos
        """)

        resultado = cursor.fetchone()

        cursor.close()

        conexion.close()

        return resultado["total"]


    def ultimos(self):
        """
        Retorna los últimos cinco equipos registrados.
        """

        conexion = conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                e.id,
                c.nombre AS cliente,
                e.marca,
                e.modelo,
                e.estado
            FROM equipos e
            INNER JOIN clientes c
                ON e.cliente_id = c.id
            ORDER BY e.id DESC
            LIMIT 5
        """)

        equipos = cursor.fetchall()

        cursor.close()

        conexion.close()

        return equipos
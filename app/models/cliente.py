# ============================================
# MODELO CLIENTE
# ============================================

from app.database import conectar


class Cliente:
    """
    Modelo encargado de administrar la tabla clientes.
    """

    def contar(self):
        """
        Retorna la cantidad de clientes registrados.
        """

        conexion = conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""
            SELECT COUNT(*) AS total
            FROM clientes
        """)

        resultado = cursor.fetchone()

        cursor.close()

        conexion.close()

        return resultado["total"]


    def ultimos(self):
        """
        Retorna los últimos cinco clientes registrados.
        """

        conexion = conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                id,
                nombre,
                empresa,
                telefono,
                email
            FROM clientes
            ORDER BY id DESC
            LIMIT 5
        """)

        clientes = cursor.fetchall()

        cursor.close()

        conexion.close()

        return clientes
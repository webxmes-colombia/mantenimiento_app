# ============================================
# MODELO USUARIO
# ============================================

from app.database import conectar


class Usuario:
    """
    Modelo encargado de administrar la tabla usuarios.
    """

    def listar(self):
        """
        Obtiene todos los usuarios registrados.
        """

        conexion = conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                id,
                nombre,
                email,
                rol,
                creado_en
            FROM usuarios
            ORDER BY id;
        """)

        usuarios = cursor.fetchall()

        cursor.close()

        conexion.close()

        return usuarios
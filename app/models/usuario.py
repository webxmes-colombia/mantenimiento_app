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
    
    def contar_tecnicos(self):
        """
        Retorna la cantidad de técnicos registrados.
        """

        conexion = conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""

            SELECT COUNT(*) AS total

            FROM usuarios

            WHERE rol='tecnico'

        """)

        resultado = cursor.fetchone()

        cursor.close()

        conexion.close()

        return resultado["total"]
    
    
    
    
    
    
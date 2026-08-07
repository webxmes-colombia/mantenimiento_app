from app.database import conectar


class Usuario:
    def listar(self):
        conexion = conectar(); cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT id, nombre, correo, rol, activo, fecha_creacion FROM usuarios ORDER BY nombre")
        datos = cursor.fetchall()
        cursor.close(); conexion.close()
        return datos

    def contar_tecnicos(self):
        conexion = conectar(); cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT COUNT(*) AS total FROM usuarios WHERE rol='Tecnico' AND activo=1")
        total = cursor.fetchone()["total"]
        cursor.close(); conexion.close()
        return total

    def login(self, correo):
        conexion = conectar(); cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE correo=%s AND activo=1", (correo,))
        usuario = cursor.fetchone()
        cursor.close(); conexion.close()
        return usuario

    def listar_tecnicos(self):
        conexion = conectar(); cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT id, nombre FROM usuarios WHERE rol='Tecnico' AND activo=1 ORDER BY nombre")
        datos = cursor.fetchall()
        cursor.close(); conexion.close()
        return datos

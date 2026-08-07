from app.database import conectar


class Cliente:
    def listar(self):
        conexion = conectar()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clientes WHERE activo=1 ORDER BY nombre")
        datos = cursor.fetchall()
        cursor.close(); conexion.close()
        return datos

    def obtener(self, cliente_id):
        conexion = conectar()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clientes WHERE id=%s", (cliente_id,))
        dato = cursor.fetchone()
        cursor.close(); conexion.close()
        return dato

    def crear(self, datos):
        conexion = conectar(); cursor = conexion.cursor()
        cursor.execute("""INSERT INTO clientes (nombre, nit, contacto, telefono, correo, direccion, ciudad)
                          VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                       (datos["nombre"], datos["nit"], datos["contacto"], datos.get("telefono"),
                        datos.get("correo"), datos.get("direccion"), datos.get("ciudad")))
        conexion.commit(); cursor.close(); conexion.close()

    def actualizar(self, cliente_id, datos):
        conexion = conectar(); cursor = conexion.cursor()
        cursor.execute("""UPDATE clientes SET nombre=%s, nit=%s, contacto=%s, telefono=%s,
                          correo=%s, direccion=%s, ciudad=%s WHERE id=%s""",
                       (datos["nombre"], datos["nit"], datos["contacto"], datos.get("telefono"),
                        datos.get("correo"), datos.get("direccion"), datos.get("ciudad"), cliente_id))
        conexion.commit(); cursor.close(); conexion.close()

    def eliminar(self, cliente_id):
        conexion = conectar(); cursor = conexion.cursor()
        cursor.execute("UPDATE clientes SET activo=0 WHERE id=%s", (cliente_id,))
        conexion.commit(); cursor.close(); conexion.close()

    def contar(self):
        conexion = conectar(); cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT COUNT(*) AS total FROM clientes WHERE activo=1")
        total = cursor.fetchone()["total"]
        cursor.close(); conexion.close()
        return total

    def ultimos(self):
        conexion = conectar(); cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT id, nombre, contacto, ciudad FROM clientes WHERE activo=1 ORDER BY id DESC LIMIT 5")
        datos = cursor.fetchall()
        cursor.close(); conexion.close()
        return datos

from app.database import conectar


class Equipo:
    CAMPOS = ("cliente_id", "tipo", "marca", "modelo", "serial", "activo_fijo", "nombre_equipo", "ubicacion", "direccion_ip", "procesador", "ram", "tipo_ram", "disco", "tipo_disco", "sistema_operativo", "antivirus", "estado", "accesorios", "observaciones", "fecha_ingreso", "activo")

    def listar(self):
        conexion = conectar(); cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT e.*, c.nombre AS cliente FROM equipos e INNER JOIN clientes c ON c.id=e.cliente_id ORDER BY e.id DESC")
        datos = cursor.fetchall()
        cursor.close(); conexion.close()
        return datos

    def obtener(self, equipo_id):
        conexion = conectar(); cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM equipos WHERE id=%s", (equipo_id,))
        dato = cursor.fetchone()
        cursor.close(); conexion.close()
        return dato

    def _valores(self, datos):
        return tuple(datos.get(campo) or None for campo in self.CAMPOS)

    def crear(self, datos):
        conexion = conectar(); cursor = conexion.cursor()
        cursor.execute(f"INSERT INTO equipos ({', '.join(self.CAMPOS)}) VALUES ({', '.join(['%s'] * len(self.CAMPOS))})", self._valores(datos))
        conexion.commit(); cursor.close(); conexion.close()

    def actualizar(self, equipo_id, datos):
        conexion = conectar(); cursor = conexion.cursor()
        cursor.execute(f"UPDATE equipos SET {', '.join(f'{campo}=%s' for campo in self.CAMPOS)} WHERE id=%s", self._valores(datos) + (equipo_id,))
        conexion.commit(); cursor.close(); conexion.close()

    def eliminar(self, equipo_id):
        conexion = conectar(); cursor = conexion.cursor()
        cursor.execute("UPDATE equipos SET activo='NO', estado='Baja' WHERE id=%s", (equipo_id,))
        conexion.commit(); cursor.close(); conexion.close()

    def contar(self):
        conexion = conectar(); cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT COUNT(*) AS total FROM equipos WHERE activo='SI'")
        total = cursor.fetchone()["total"]
        cursor.close(); conexion.close()
        return total

    def ultimos(self):
        conexion = conectar(); cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT e.id, c.nombre AS cliente, e.marca, e.modelo, e.estado FROM equipos e INNER JOIN clientes c ON c.id=e.cliente_id ORDER BY e.id DESC LIMIT 5")
        datos = cursor.fetchall()
        cursor.close(); conexion.close()
        return datos

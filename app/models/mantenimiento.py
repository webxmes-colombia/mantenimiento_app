from app.database import conectar


class Mantenimiento:
    CAMPOS = ("equipo_id", "tecnico_id", "tipo_mantenimiento", "fecha_programada",
              "fecha_mantenimiento", "estado", "diagnostico", "trabajo_realizado",
              "repuestos_utilizados", "limpieza_realizada", "pasta_termica_aplicada",
              "antivirus_actualizado", "sistema_actualizado", "respaldo_verificado",
              "pruebas_funcionamiento", "observaciones", "costo")

    def listar(self):
        conexion = conectar(); cursor = conexion.cursor(dictionary=True)
        cursor.execute("""
            SELECT m.id, c.nombre AS cliente, CONCAT(e.marca, ' ', e.modelo) AS equipo,
                   u.nombre AS tecnico, m.tipo_mantenimiento, m.fecha_mantenimiento, m.estado
            FROM mantenimientos m
            INNER JOIN equipos e ON e.id=m.equipo_id
            INNER JOIN clientes c ON c.id=e.cliente_id
            INNER JOIN usuarios u ON u.id=m.tecnico_id
            ORDER BY m.fecha_mantenimiento DESC, m.id DESC
        """)
        datos = cursor.fetchall()
        cursor.close(); conexion.close()
        return datos

    def crear(self, datos):
        conexion = conectar(); cursor = conexion.cursor()
        columnas = ", ".join(self.CAMPOS)
        marcadores = ", ".join(["%s"] * len(self.CAMPOS))
        valores = tuple(
            (datos.get(campo) or None) if campo == "fecha_programada" else datos.get(campo)
            for campo in self.CAMPOS
        )
        cursor.execute(f"INSERT INTO mantenimientos ({columnas}) VALUES ({marcadores})", valores)
        conexion.commit(); cursor.close(); conexion.close()

    def contar(self):
        conexion = conectar(); cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT COUNT(*) AS total FROM mantenimientos")
        total = cursor.fetchone()["total"]
        cursor.close(); conexion.close()
        return total

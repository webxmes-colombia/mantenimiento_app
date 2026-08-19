from app.database import conectar


class Reporte:

    def equipos(self):
        conexion = conectar()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                id,
                CONCAT(nombre_equipo, ' — ', marca, ' ', modelo) AS nombre
            FROM equipos
            WHERE activo = 'SI'
            ORDER BY nombre_equipo
        """)

        equipos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return equipos

    def por_equipo(self, equipo_id):
        conexion = conectar()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                m.id,
                c.nombre AS cliente,
                e.nombre_equipo,
                CONCAT(e.marca, ' ', e.modelo) AS equipo,
                u.nombre AS tecnico,
                m.tipo_mantenimiento,
                m.fecha_mantenimiento,
                m.estado,
                m.diagnostico,
                m.costo
            FROM mantenimientos m
            INNER JOIN equipos e ON e.id = m.equipo_id
            INNER JOIN clientes c ON c.id = e.cliente_id
            INNER JOIN usuarios u ON u.id = m.tecnico_id
            WHERE m.equipo_id = %s
            ORDER BY m.fecha_mantenimiento DESC
        """, (equipo_id,))

        mantenimientos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return mantenimientos
    
    def datos_equipo(self, equipo_id):

        conexion = conectar()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                e.*,
                c.nombre AS cliente,
                c.nit,
                c.contacto,
                c.telefono,
                c.correo,
                c.direccion,
                c.ciudad
            FROM equipos e
            INNER JOIN clientes c ON c.id = e.cliente_id
            WHERE e.id = %s
        """, (equipo_id,))

        equipo = cursor.fetchone()

        cursor.close()
        conexion.close()

        return equipo
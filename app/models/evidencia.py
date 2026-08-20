from app.database import conectar


class Evidencia:

    def listar(self, mantenimiento_id):

        conexion = conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM evidencias
            WHERE mantenimiento_id=%s
            ORDER BY fecha_carga DESC
        """, (mantenimiento_id,))

        datos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return datos


    def crear(self, mantenimiento_id, tipo_evidencia,
              nombre_archivo, ruta_archivo,
              tipo_archivo, descripcion):

        conexion = conectar()

        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO evidencias
            (
                mantenimiento_id,
                tipo_evidencia,
                nombre_archivo,
                ruta_archivo,
                tipo_archivo,
                descripcion
            )
            VALUES (%s,%s,%s,%s,%s,%s)
        """, (
            mantenimiento_id,
            tipo_evidencia,
            nombre_archivo,
            ruta_archivo,
            tipo_archivo,
            descripcion
        ))

        conexion.commit()

        cursor.close()
        conexion.close()


    def eliminar(self, id):

        conexion = conectar()

        cursor = conexion.cursor()

        cursor.execute("""
            DELETE FROM evidencias
            WHERE id=%s
        """, (id,))

        conexion.commit()

        cursor.close()
        conexion.close()
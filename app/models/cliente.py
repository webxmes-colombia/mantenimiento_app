from app.database import conectar


class Cliente:

    def listar(self):

        conexion = conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""
            SELECT *
            FROM clientes
            ORDER BY id
        """)

        datos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return datos


    def obtener(self, id):

        conexion = conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""

            SELECT *

            FROM clientes

            WHERE id=%s

        """,(id,))

        dato = cursor.fetchone()

        cursor.close()
        conexion.close()

        return dato


    def crear(self,datos):

        conexion = conectar()

        cursor = conexion.cursor()

        cursor.execute("""

            INSERT INTO clientes
            (
                nombre,
                empresa,
                direccion,
                telefono,
                email
            )

            VALUES
            (%s,%s,%s,%s,%s)

        """,(

            datos["nombre"],
            datos["empresa"],
            datos["direccion"],
            datos["telefono"],
            datos["email"]

        ))

        conexion.commit()

        cursor.close()
        conexion.close()


    def editar(self,id,datos):

        conexion = conectar()

        cursor = conexion.cursor()

        cursor.execute("""

            UPDATE clientes

            SET

                nombre=%s,

                empresa=%s,

                direccion=%s,

                telefono=%s,

                email=%s

            WHERE id=%s

        """,(

            datos["nombre"],
            datos["empresa"],
            datos["direccion"],
            datos["telefono"],
            datos["email"],
            id

        ))

        conexion.commit()

        cursor.close()
        conexion.close()


    def eliminar(self,id):

        conexion = conectar()

        cursor = conexion.cursor()

        cursor.execute("""

            DELETE

            FROM clientes

            WHERE id=%s

        """,(id,))

        conexion.commit()

        cursor.close()
        conexion.close()
        
    def contar(self):
        """
        Retorna el total de clientes.
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
        Retorna los últimos cinco clientes.
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

        datos = cursor.fetchall()

        cursor.close()
        conexion.close()

        return datos
    
    def actualizar(self, id, datos):

        conexion = conectar()

        cursor = conexion.cursor()

        cursor.execute("""

            UPDATE clientes

            SET

                nombre=%s,

                empresa=%s,

                direccion=%s,

                telefono=%s,

                email=%s

            WHERE id=%s

        """, (

            datos["nombre"],
            datos["empresa"],
            datos["direccion"],
            datos["telefono"],
            datos["email"],
            id

        ))

        conexion.commit()

        cursor.close()

        conexion.close()
def eliminar(self, id):

    conexion = conectar()

    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM clientes
        WHERE id=%s
    """, (id,))

    conexion.commit()

    cursor.close()

    conexion.close()
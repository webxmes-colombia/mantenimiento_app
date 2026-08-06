"""
==========================================
SEED DE USUARIOS
Actualiza las contraseñas utilizando HASH
==========================================
"""

from werkzeug.security import generate_password_hash

from app.database import conectar


conexion = conectar()

cursor = conexion.cursor()


usuarios = [

    ("Admin123", "admin@empresa.com"),

    ("Tecnico123", "ana@empresa.com"),

    ("Tecnico123", "luis@empresa.com"),

    ("Tecnico123", "sofia@empresa.com"),

    ("Admin123", "jorge@empresa.com")

]


for password, email in usuarios:

    password_hash = generate_password_hash(password)

    cursor.execute("""

        UPDATE usuarios

        SET password=%s

        WHERE email=%s

    """, (password_hash, email))


conexion.commit()

cursor.close()

conexion.close()


print("Usuarios actualizados correctamente.")
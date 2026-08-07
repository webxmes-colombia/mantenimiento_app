from werkzeug.security import generate_password_hash

print(generate_password_hash("Admin123"))
print(generate_password_hash("Tecnico123"))
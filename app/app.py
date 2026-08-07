from flask import Flask
from dateutil.relativedelta import relativedelta
from app.routes.usuario_routes import usuario_bp
from app.routes.dashboard_routes import dashboard_bp
from app.routes.auth_routes import auth_bp
from app.routes.cliente_routes import cliente_bp
from app.routes.equipo_routes import equipo_bp
from app.routes.mantenimiento_routes import mantenimiento_bp

# app = Flask(__name__)
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

app.secret_key = "123456"

app.register_blueprint(usuario_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(cliente_bp)
app.register_blueprint(equipo_bp)
app.register_blueprint(mantenimiento_bp)

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
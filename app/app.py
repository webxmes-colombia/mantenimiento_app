from flask import Flask

from app.routes.usuario_routes import usuario_bp
from app.routes.dashboard_routes import dashboard_bp

# app = Flask(__name__)
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

app.secret_key = "123456"

app.register_blueprint(usuario_bp)
app.register_blueprint(dashboard_bp)

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
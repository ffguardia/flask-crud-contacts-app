from flask import Flask
from main import register_blueprints
from db import init_app

# Crear la instancia de la aplicación
app = Flask(__name__)

# Configuración de la clave secreta
app.secret_key = "mysecretkey"

# Inicializar la base de datos
init_app(app)

# Registrar blueprints
register_blueprints(app)

# Iniciar la aplicación
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

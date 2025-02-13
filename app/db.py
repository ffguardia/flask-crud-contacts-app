from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

# Crear una instancia de MySQL sin configurarla aún
mysql = MySQL()

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Función para inicializar la configuración de la base de datos
def init_app(app):
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'rootpassword'
    app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST') or '127.0.0.1'  # localhost
    app.config['MYSQL_DB'] = os.getenv('MYSQL_DB') or 'contacts_db'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    
    # Inicializar la conexión MySQL con la app
    mysql.init_app(app)

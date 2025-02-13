from contacts import contacts

# Función para registrar los blueprints
def register_blueprints(app):
    app.register_blueprint(contacts)

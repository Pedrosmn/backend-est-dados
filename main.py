import os
from flask import Flask
from flask_cors import CORS
from app.routes import routes

app = Flask(__name__)
CORS(app)  # Habilita CORS para evitar bloqueios

app.register_blueprint(routes)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Usa a porta fornecida pelo Render
    app.run(host="0.0.0.0", port=port, debug=True)  # Escuta em todas as interfaces

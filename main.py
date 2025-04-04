from flask import Flask
from flask_cors import CORS
from app.routes import routes

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "https://frontend-est-dados.vercel.app"}})

# Defina um prefixo "/api" para as rotas
app.register_blueprint(routes, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)

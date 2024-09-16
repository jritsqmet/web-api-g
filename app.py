from flask import Flask, jsonify
import json

app = Flask(__name__)

# Cargar los datos desde el archivo JSON
with open('videojuegos.json') as f:
    videojuegos = json.load(f)

# Ruta para obtener todos los videojuegos
@app.route('/videojuegos', methods=['GET'])
def get_videojuegos():
    return jsonify(videojuegos)

# Ruta para obtener un videojuego por ID
@app.route('/videojuegos/<int:id>', methods=['GET'])
def get_videojuego(id):
    videojuego = next((item for item in videojuegos if item["id"] == id), None)
    if videojuego:
        return jsonify(videojuego)
    else:
        return jsonify({"error": "Videojuego no encontrado"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

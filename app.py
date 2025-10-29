# Autor: isaak
# Fecha: 29

from flask import Flask, request, jsonify

app = Flask(__name__)

# Diccionario principal de dispositivos
dispositivos = {}
#hola
# GET: mostrar todos los dispositivos
# POST: agregar un nuevo dispositivo
# PUT: modificar un dispositivo existente
@app.route('/dispositivos', methods=['GET', 'POST', 'PUT'])
def manejar_dispositivos():
    # Mostrar todos (GET)
    if request.method == 'GET':
        return jsonify(list(dispositivos.values()))

    # Agregar (POST)
    if request.method == 'POST':
        data = request.get_json()
        if not data or "id" not in data:
            return jsonify({"error": "Faltan datos o el campo 'id'"}), 400
        dispositivos[data["id"]] = data
        return jsonify({"mensaje": "Dispositivo agregado correctamente"}), 201

    # Modificar (PUT)
    if request.method == 'PUT':
        data = request.get_json()
        if not data or "id" not in data:
            return jsonify({"error": "Falta el campo 'id'"}), 400
        id = data["id"]
        if id not in dispositivos:
            return jsonify({"error": "Dispositivo no encontrado"}), 404
        dispositivos[id].update(data)
        return jsonify({"mensaje": "Dispositivo actualizado correctamente"}), 200

# Ruta para mostrar todos los dispositivos en HTML
@app.route('/dispositivos_html', methods=['GET'])
def mostrar_html():
    html = "<html><body><h1>Lista de Dispositivos</h1>"
    for d in dispositivos.values():
        html += f"""
        <div style='border:1px solid #ccc; padding:10px; margin:10px;'>
            <b>ID:</b> {d.get('id','')}<br>
            <b>Nombre:</b> {d.get('nombre','')}<br>
            <b>Descripción:</b> {d.get('descripcion','')}<br>
            <b>IP:</b> {d.get('ip','')}<br>
            <b>MAC:</b> {d.get('mac','')}<br>
            <b>Ubicación:</b> {d.get('ubicacion','')}<br>
            <b>Tipo:</b> {d.get('tipo','')}
        </div>
        """
    html += "</body></html>"
    return html

# Ruta base
@app.route('/')
def inicio():
    return "API de dispositivos funcionando correctamente. Usa /dispositivos y /dispositivos_html"

if __name__ == '__main__':
    app.run(debug=True)

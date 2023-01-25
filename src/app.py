from flask import Flask, jsonify, request
import json
app = Flask(__name__)

# Diccionario
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

# Endpoint (route) - Metodo: Get
@app.route('/todos', methods=['GET'])
def hello_world():
     # Retorna la lista completa
    return jsonify(todos)

# Endpoint (route) - Metodo: Post
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request.get_json(force=True)
    request_body = request.data
    # Json.loads sirve para decodificar el request.data
    decoded_object = json.loads(request_body)
    # Insertar un elemento al final de la lista
    todos.append(decoded_object)
    # Jsonify: Cast de JSON
    json_text = jsonify(todos)
    # Retorna la lista completa
    return json_text

# Endpoint (route) - Metodo: Delete
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    # Elimina item de esa posición
    del todos[position]
     # Retorna la lista completa
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
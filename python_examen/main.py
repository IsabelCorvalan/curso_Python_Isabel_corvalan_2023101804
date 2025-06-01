from flask import Flask, request, jsonify
from cliente import buscar_cliente

app = Flask(__name__)

@app.route('/cliente', methods=['POST'])
def cliente():
    data = request.get_json()
    ci = data.get('ci')

    if not ci:
        return jsonify({
            "accion": "Falta cédula de cliente",
            "codRes": "ERROR",
            "menRes": "Datos incompletos",
            "ci": None
        }), 400

    existe = buscar_cliente(ci)

    if existe:
        return jsonify({
            "accion": "Success",
            "codRes": "SIN_ERROR",
            "menRes": "OK",
            "ci": ci
        })
    else:
        return jsonify({
            "accion": "Cliente no está en el sistema",
            "codRes": "ERROR",
            "menRes": "Error cliente",
            "ci": ci
        })

if __name__ == '__main__':
    app.run(port=5003, debug=True)
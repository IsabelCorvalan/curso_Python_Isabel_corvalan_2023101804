from flask import Blueprint, request, jsonify

cliente = Blueprint('cliente', __name__)

@cliente.route('/cliente', methods=['POST'])
def verificar_cliente():
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
            "accion": "La cédula del cliente existe",
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


clientes = [
    "6748467"
]

def buscar_cliente(ci):
    return ci in clientes
clientes = {
    "6748467": {
        "ci": "6748467",
        "accion": "Success",
        "codRes": "SIN_ERROR",
        "menRes": "OK"
    }
}

def buscar_cliente(ci):
    if ci in clientes:
        return clientes[ci]
    else:
        return {
            "ci": ci,
            "accion": "Cliente no está en el sistema",
            "codRes": "ERROR",
            "menRes": "Error cliente"
        }

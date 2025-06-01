from flask import Flask
from cliente import cliente

app = Flask( __name__)

app.register_blueprint(cliente)

@app.route('/', methods=['GET'])
def hello():
    return 'Hola Unida soy Isabel Corvalan'

if __name__ == "_main_":
    app.run(host='0.0.0.0', port=5001, debug=True)
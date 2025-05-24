# main.py

from cliente import buscar_cliente

def main():
    ci = input("Ingrese la cédula de identidad del cliente: ")
    resultado = buscar_cliente(ci)
    print("\nResultado de la búsqueda:")
    for clave, valor in resultado.items():
        print(f"{clave}: {valor}")

if __name__ == "__main__":
    main()

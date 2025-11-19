from zeep import Client

WSDL_URL = "http://localhost:8000/?wsdl"

client = Client(WSDL_URL)

def crear_dispositivo(tipo_dispositivo, marca, num_serie, user_id):
    result = client.service.crear(tipo_dispositivo, marca, num_serie, user_id)
    print(f"Dispositivo creado con ID: {result}")
    return result

def leer_dispositivo(dispositivo_id):
    result = client.service.leer(dispositivo_id)
    print(f"Leer dispositivo: {result}")
    return result

def actualizar_dispositivo(dispositivo_id, tipo_dispositivo, marca, num_serie, user_id):
    result = client.service.actualizar(dispositivo_id, tipo_dispositivo, marca, num_serie, user_id)
    print(f"Actualizar dispositivo: {result}")
    return result

def eliminar_dispositivo(dispositivo_id):
    result = client.service.eliminar(dispositivo_id)
    print(f"Eliminar dispositivo: {result}")
    return result

def listar_todos():
    result = client.service.listar_todos()
    print("Lista de dispositivos:")
    for item in result:
        print("-", item)


if __name__ == "__main__":
   # Ejemplo de uso:

    print("=== Crear dispositivo ===")
    nuevo_id = crear_dispositivo(
        tipo_dispositivo="AirTag",
        marca="Apple",
        num_serie="APL12345",
        user_id=1
    )

    print("\n=== Leer dispositivo ===")
    leer_dispositivo(nuevo_id)

    print("\n=== Actualizar dispositivo ===")
    actualizar_dispositivo(
        nuevo_id,
        tipo_dispositivo="Mi Band 6 Pro",
        marca="Xiaomi",
        num_serie="XIAOXD76",
        user_id=2
    )

    print("\n=== Leer dispositivo actualizado ===")
    leer_dispositivo(nuevo_id)

    print("\n=== Eliminar dispositivo ===")
    eliminar_dispositivo(6)

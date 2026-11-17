class Producto:

    def __init__(self, codigo: str, nombre: str, precio: float, existencia: int):
        # Atributos del producto solicitados en la practica
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencia = existencia

    # Metodo que muestra la informacion del producto en pantalla.
    def mostrar_informacion(self) -> None:
        print("-" * 35)
        print(" DATOS DEL PRODUCTO")
        print("-" * 35)
        print(f"Codigo:     {self.codigo}")
        print(f"Nombre:     {self.nombre}")
        print(f"Precio:     ${self.precio:.2f}")
        print(f"Existencia: {self.existencia} unidades")
        print("-" * 35)


# Funcionalidad correspondiente al reto (feature/busqueda-productos)
def buscar_producto(lista_productos: list, criterio: str) -> list:

    criterio_busqueda = criterio.lower()
    coincidencias = []
    
    for prod in lista_productos:
        if criterio_busqueda in prod.codigo.lower() or criterio_busqueda in prod.nombre.lower():
            coincidencias.append(prod)         
    return coincidencias


# Bloque de prueba local para verificar su funcionamiento
if __name__ == "__main__":
    # 1. Creacion de producto (feature/registro-productos)
    producto_demo = Producto(
        codigo="PROD-001",
        nombre="Teclado Mecanico RGB",
        precio=75.50,
        existencia=20
    )

    # 2. Mostrar la informacion en pantalla
    producto_demo.mostrar_informacion()

    # 3. Demostracion de busqueda (reto: feature/busqueda-productos)
    inventario = [
        producto_demo,
        Producto("PROD-002", "Mouse Inalambrico", 25.00, 15),
        Producto("PROD-003", "Monitor 24 pulgadas", 180.00, 8)
    ]

    print("\n>>> Ejecutando prueba de busqueda por termino 'Mouse'...")
    resultados = buscar_producto(inventario, "Mouse")
    
    for prod_encontrado in resultados:
        prod_encontrado.mostrar_informacion()
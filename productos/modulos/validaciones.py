'''
existe_producto(productos, id_)
validar_precio(precio) (precio > 0)
validar_stock(stock) (stock >= 0)
validar_nombre(nombre) (no vacío y largo mínimo)
validar_id_formato(id_) (ej: empieza con “P” y números)
puede_descontar_stock(producto, cantidad) (no dejar stock negativo)
'''
'''
Este módulo contiene funciones para validar productos, 
precios, stock, IDs y ventas, trabajando 
directamente con el diccionario global PRODUCTOS.
'''

from modulos.datos_basicos import PRODUCTOS
import modulos.funciones_utiles as funhelp


def producto_existencia(largo=int):
    """
    Solicita el nombre de un producto y valida que:
    - No sea None (cancelación)
    - Cumpla un largo mínimo
    - No exista previamente en PRODUCTOS

    Args:
        largo (int): largo mínimo permitido para el nombre.

    Returns:
        str | None: nombre del producto en minúsculas si es válido,
                    None si el usuario cancela.
    """
    while True:
        nombre = funhelp.prueba_letras("\nIngrese el nombre del producto: ", largo)
        
        if nombre is None:
            return None
        
        nombre = nombre.strip().lower()

        existe = False
        for producto in PRODUCTOS.values():
            if producto["nombre"].lower() == nombre:
                existe = True
                break

        if existe:
            print("\n❌ El producto ya existe, intente con otro nombre.")
        else:
            print("\n✅ Producto aceptado, ingrese los siguientes datos...")
            return nombre


def validar_precio():
    """
    Solicita y valida el precio de un producto.

    Reglas:
    - Debe ser un número mayor a 0
    - 0 se considera cancelación
    - No se permiten valores negativos

    Returns:
        int | None: precio válido o None si se cancela.
    """
    while True:
        precio = funhelp.prueba_numeros("\nPrecio del producto: ")
        
        if precio == 0:
            return None

        if precio is None:
            continue

        if precio < 0:
            print("\n❌ Ingrese un precio valido...")
            continue
    
        print(f"\n✅ Buen precio: ${precio}")
        return precio


def validar_stock(nombre): #* se pasa el nombre del producto 
    """
    Solicita y valida el stock inicial de un producto.

    Reglas:
    - No puede ser negativo
    - 0 se considera cancelación

    Args:
        nombre (str): nombre del producto (solo para mensajes).

    Returns:
        int | None: stock válido o None si se cancela.
    """
    while True:
        stock = funhelp.prueba_numeros("\nCantidad del producto: ")

        if stock == 0:
            return None

        if stock is None:
            continue

        if stock < 0:
            print("\n❌El stock no es suficiente.")
            continue
        
        print(f"\n✅ {nombre} tiene la cantidad de {stock} unidades.")
        return stock


def validar_id():
    """
    Permite buscar un producto por ID o por nombre.

    Reglas:
    - '0' cancela la búsqueda
    - Coincide tanto por ID como por nombre

    Returns:
        tupla:
            (id_producto, producto) si se encuentra
            (None, None) si se cancela
    """
    while True:
        buscar = input("\nIngrese ID o nombre del producto que busca (0 para cancelar): ").strip().lower()

        if buscar == "0":
            return None, None
        
        if not buscar:
            print("\n❌ Ingrese un ID o nombre valido")
            continue
        
        for id_prod, producto in PRODUCTOS.items():
            if id_prod.lower() == buscar or producto["nombre"].lower() == buscar:
                return id_prod, producto
        
        print("\n❌ Producto no encontrado...")


def descontar_stock():
    """
    Muestra la información de un producto antes de descontar stock.

    Flujo:
    - Busca producto por ID o nombre
    - Muestra el producto en tabla
    - Retorna el producto para operar sobre él

    Returns:
        dict | None: producto encontrado o None si se cancela.
    """
    id_producto, producto = validar_id()

    if producto is None:
        print("\nBusqueda cancelada")
        return None
    
    mostrar_producto = {
        id_producto: {
            "nombre": producto["nombre"],
            "descripcion": producto["descripcion"],
            "precio": producto["precio"],
            "stock": producto["stock"]
        }
    }
    funhelp.imprimir_tabla(mostrar_producto, None, "double_grid")
    return producto


def validar_cantidad(producto):
    """
    Valida la cantidad de unidades a vender y descuenta el stock.

    Reglas:
    - Cantidad > 0
    - No puede superar el stock disponible
    - 0 o None cancelan la operación

    Args:
        producto (dict): producto sobre el cual se realizará la venta.

    Returns:
        None
    """
    while True:
        cantidad = funhelp.prueba_numeros("\nIngrese cuantas unidades quiere: ")

        if cantidad is None or cantidad == 0:
            return funhelp.cancelaciones()

        if cantidad < 0:
            print("\n❌ Cantidad invalida, debe ser mayor a 0")
            continue

        elif producto["stock"] < cantidad:
            print("\n❌ No hay suficiente stock")
            continue

        producto["stock"] -= cantidad
        print(f"\n✅ Venta exitosa con {cantidad} unidades vendidas")
        print(f"\n\tNuevo stock de {producto["nombre"]}: {producto["stock"]}")
        break

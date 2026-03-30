'''
Funciones del CRUD:

-agregar_producto(...)
-listar_productos(...)
-buscar_producto(...)
-editar_producto(...)
-eliminar_producto(...)

Aquí vive “lo importante” del sistema, lógica del negocio
'''

"""
Módulo de gestión de productos.

Contiene funciones para:
- Listar productos
- Agregar productos
- Buscar productos
- Vender productos
- Eliminar productos
- Editar productos y sus campos

Depende de:
- modulos.datos_basicos (PRODUCTOS)
- modulos.funciones_utiles
- modulos.validaciones
"""

from modulos.datos_basicos import PRODUCTOS
import modulos.funciones_utiles as funhelp
import modulos.validaciones as valido

def listar_productos(productos):
    """
    Muestra una tabla con la lista de productos.

    :param productos: Diccionario de productos a mostrar
    :type productos: dict
    """
    headers = ["ID", "Nombre", "Descripcion", "Precio", "Stock"]
    funhelp.imprimir_tabla(productos, headers=headers, formato="double_grid")


def listar_productos_editar(productos):
    """
    Muestra los cambios realizados a un producto durante la edición.

    :param productos: Diccionario con los datos actualizados del producto
    :type productos: dict
    """
    headers = ["Parametro", "Cambio"]
    funhelp.imprimir_tabla(productos, headers=headers, formato="double_grid")


def agregar_producto(producto):
    """
    Agrega un nuevo producto al diccionario global PRODUCTOS.

    Permite cancelar la operación en cualquier paso ingresando '0'.

    :param producto: Diccionario donde se almacenan los productos
    :type producto: dict
    """
    id_producto = funhelp.generar_id(PRODUCTOS, "P", 3)
    nombre = valido.producto_existencia(3)
    if nombre is None:
        return funhelp.cancelaciones()
    descripcion = input("\nDescripcion del producto: ")
    if descripcion == "0":
        return funhelp.cancelaciones()
    precio = valido.validar_precio()
    if precio is None:
        return funhelp.cancelaciones()
    stock = valido.validar_stock(nombre)
    if stock is None:
        return funhelp.cancelaciones()

    #*INGRESO---------------------------
    producto[id_producto] = {"nombre": nombre, "descripcion": descripcion, "precio": precio, "stock": stock}
    print(f"\n✅ El producto '{nombre}' ha sido agregado correctamente con el precio de '{precio}' y '{stock}' unidades...\n")

def buscar_producto_por_id():
    """
    Busca un producto por ID o nombre y lo muestra en pantalla.

    :return: ID del producto si se encuentra, None si se cancela
    :rtype: str | None
    """
    id_producto, producto = valido.validar_id()
    if producto is None:
        print("\nBusqueda cancelada")
        return None
    print("\nProducto encontrado: ")
    mostrar_producto = {
        id_producto: {
            "nombre": producto["nombre"],
            "descripcion": producto["descripcion"],
            "precio": producto["precio"],
            "stock": producto["stock"]
        }
    }
    listar_productos(mostrar_producto)
    return id_producto


def vender_producto():
    """
    Realiza la venta de un producto descontando stock.
    """
    producto = valido.descontar_stock()
    if producto != None:
        valido.validar_cantidad(producto)

def eliminar_producto():
    """
    Elimina un producto del diccionario PRODUCTOS previa confirmación.
    """
    producto = valido.descontar_stock()
    if producto is None:
        return

    eliminar = funhelp.prueba_letras(f"\nDesea eliminar el producto '{producto["nombre"]}' para siempre?: (s/n)", 1)

    if eliminar is None or eliminar.lower() != "s":
        return funhelp.cancelaciones()
        
    for clave, datos in list(PRODUCTOS.items()):
        if datos["nombre"].lower() == producto["nombre"].lower():
            PRODUCTOS.pop(clave)
            print(f"\nEl producto {producto['nombre']} fue eliminado correctamente")
            funhelp.pausa()
            listar_productos(PRODUCTOS)
            print("==== LISTA ACTUALIZADA ====")



#=========== MENU EDITAR ============ (deje unos cambios redundantes comentados pero los refactorice mas abajo...)
def editar_producto():
    """
    Permite editar los campos de un producto existente.

    Campos editables:
    - nombre
    - descripcion
    - precio
    - stock

    Incluye menú interactivo y cancelación global.
    """
    id_producto = buscar_producto_por_id()
    if id_producto is None:
        return
    producto = PRODUCTOS[id_producto]

    while True:
        print("\n","=" * 5 ," EDITAR: ", producto["nombre"].upper(),"=" * 5)
        print("1) Cambiar nombre")
        print("2) Cambiar descripcion")
        print("3) Cambiar precio")
        print("4) Cambiar cantidad")
        print("0) ---.Terminar Acccion.---\n")

        opcion = funhelp.leer_int("Elige una opcion: ", minimo=0, maximo=4)
        print("")

        match opcion:
            case 1:
                editar_campo(producto, "nombre", "Nuevo nombre: ")

                #!Dejo esto comentado para mostrar la redundancia de los casos y porque lo refactorice al final...
                # print(f"Opcion {opcion}")
                # nuevo_nombre = funhelp.prueba_letras("\nIngrese el nuevo nombre: ", 3)
                # cambiar = funhelp.prueba_letras(f"\nEl nuevo nombre '{nuevo_nombre}' esta correcto? (s/n): ", 1)

                # if cambiar == None or cambiar.lower() != "s":
                #     funhelp.cancelaciones()
                #     continue
                
                # producto["nombre"] = nuevo_nombre
                # print(f"\nEl nombre ha sido actualizado correctamente a: {producto['nombre']}\n")
                # funhelp.pausa()

            case 2:
                editar_campo(producto, "descripcion", "Nueva descripcion: ")
                # print(f"Opcion {opcion}")
                # nuevo_nombre = funhelp.prueba_letras("\nIngrese la nueva descripcion: ", 3)
                # cambiar = funhelp.prueba_letras(f"\nLa descripcion: '{nuevo_nombre}' esta correcta? (s/n): ", 1)

                # if cambiar == None or cambiar.lower() != "s":
                #     funhelp.cancelaciones()
                #     continue
                
                # producto["descripcion"] = nuevo_nombre
                # print(f"\nLa descripcion ha sido actualizada correctamente a: {producto['descripcion']}\n")
                # funhelp.pausa()

            case 3:
                editar_campo(producto, "precio", "Nuevo precio: ", tipo="numero")
                # print(f"Opcion {opcion}")
                # precio = funhelp.prueba_numeros("\nIngrese el nuevo precio: ")
                # cambiar = funhelp.prueba_letras(f"\nEl precio: '{precio}' esta correcta? (s/n): ", 1)

                # if cambiar == None or cambiar.lower() != "s":
                #     funhelp.cancelaciones()
                #     continue
                
                # producto["precio"] = precio
                # print(f"\nEl precio ha sido actualizada correctamente a: {producto['precio']}\n")
                # funhelp.pausa()
            
            case 4:
                editar_campo(producto, "precio", "Nueva cantidad: ", tipo="numero")
                print(f"Opcion {opcion}")
                # stock = funhelp.prueba_numeros("\nIngrese la nueva cantidad: ")
                # cambiar = funhelp.prueba_letras(f"\nLa cantidad: '{stock}' esta correcta? (s/n): ", 1)

                # if cambiar == None or cambiar.lower() != "s":
                #     funhelp.cancelaciones()
                #     continue
                
                # producto["stock"] = stock
                # print(f"\nLa cantidad ha sido actualizada correctamente a: {producto['stock']}\n")
                # funhelp.pausa()

            case 0:
                print("\nNueva informacion del producto: ")
                listar_productos_editar(producto)
                print("REGRESANDO...\n")
                break

def editar_campo(producto, campo, mensaje, tipo="texto"):
    """
    Edita un campo específico de un producto con confirmación previa.

    :param producto: Diccionario del producto a editar
    :param campo: Campo a modificar (nombre, descripcion, precio, stock)
    :param mensaje: Mensaje a mostrar al pedir el nuevo valor
    :param tipo: Tipo de dato esperado ('texto' o 'numero')
    """
    if tipo == "texto":
        valor = funhelp.prueba_letras(mensaje, 3)
    else:
        valor = funhelp.prueba_numeros(mensaje)

    if valor is None:
        return funhelp.cancelaciones()
    
    confirmar = funhelp.prueba_letras(f"\nEl nuevo valor: '{valor}' esta correcto? (s/n): ", 1)

    if confirmar is None or confirmar.lower() != "s":
        return funhelp.cancelaciones()

    producto[campo] = valor

    print(f"\n{campo.capitalize()} ha sido actualizado a: {valor}")
    funhelp.pausa()
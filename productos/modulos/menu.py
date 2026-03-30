'''
Funciones para:

-mostrar el menú
-pedir una opción
-imprimir mensajes bonitos

No debería tener lógica de negocio (no calcular totales, modificar productos).
'''
# --- Librería estándar ---


# --- Librerías externas / de terceros ---


# --- Módulos y paquetes propios del proyecto ---

from modulos.datos_basicos import PRODUCTOS
import modulos.gestion_datos as ges_datos
import modulos.funciones_utiles as funhelp

def mostrar_menu(): #Funcion que imprime el menu
    print("\n" + "=" * 40)
    print("     GESTION DE PRODUCTOS")
    print("=" * 40)
    print("1) Listar productos")
    print("2) Agregar productos")
    print("3) Buscar productos por ID o nombre")
    print("4) Vender productos")
    print("5) Editar productos")
    print("6) Eliminar productos")
    print("0) Salir")
    print("=" * 40)

def ejecutar_menu(): #Ejecuta el caso con la eleccion del usuario
    while True:
        mostrar_menu()  #Muestra el menu
        opcion = funhelp.leer_int("Elige una opcion: ", minimo=0, maximo=6) #Aqui se guarda la opcion del usuario
        print("\n")

        match opcion:
            case 1: 
                print("===== LISTA DE PRODUCTOS =====")
                ges_datos.listar_productos(PRODUCTOS)
                funhelp.pausa()
                funhelp.limpiar_consola()

            case 2:
                print("===== AGREGAR PRODUCTO ===== (0 = cancelar)")
                ges_datos.agregar_producto(PRODUCTOS)
                funhelp.pausa()
                funhelp.limpiar_consola()

            case 3:
                print("===== BUSCAR PRODUCTO =====")
                ges_datos.buscar_producto_por_id()
                funhelp.pausa()
                funhelp.limpiar_consola()

            case 4:
                print("===== GENERAR VENTA =====")
                ges_datos.vender_producto()
                funhelp.pausa()
                funhelp.limpiar_consola()

            case 5:
                print("===== EDITAR PRODUCTO =====")
                ges_datos.editar_producto()
                funhelp.pausa()
                funhelp.limpiar_consola()

            case 6:
                print("===== ELIMINAR PRODUCTO =====")
                ges_datos.listar_productos(PRODUCTOS)
                ges_datos.eliminar_producto()
                funhelp.pausa()
                funhelp.limpiar_consola()
            
            case 0:
                print("SALIENDO DEL SISTEMA...\n")
                break
            

ejecutar_menu() #Comienza la ejecucion del sistema



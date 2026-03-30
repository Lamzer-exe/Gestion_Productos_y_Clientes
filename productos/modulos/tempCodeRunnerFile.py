from datos_basicos import PRODUCTOS
import gestion_datos as ges_datos
import funciones_utiles as funhelp

def mostrar_menu():
    print("\n" + "=" * 40)
    print("     GESTION DE PRODUCTOS")
    print("=" * 40)
    print("1) Listar productos")
    print("2) Agregar productos")
    print("3) Buscar productos por ID o nombre")
    print("4) Vender productos")
    print("5) Eliminar productos")
    print("0) Salir")
    print("=" * 40)

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = funhelp.leer_int("Elige una opcion: ", minimo=0, maximo=5)
        print("\n")

        match opcion:
            case 1:
                print("===== LISTA DE PRODUCTOS =====")

                ges_datos.listar_productos(PRODUCTOS)
                funhelp.pausa()
                funhelp.limpiar_consola()

            case 2:
                print("===== AGREGAR PRODUCTO =====")

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
                print("Opcion 5 Eliminar productos")
                ges_datos.listar_productos(PRODUCTOS)
                ges_datos.eliminar_producto()
                funhelp.pausa()
                ges_datos.listar_productos(PRODUCTOS)
                funhelp.pausa()
                funhelp.limpiar_consola()


            
            # case 6: GENERAR VENTA
            case 0:
                print("SALIENDO DEL SISTEMA...\n")
                break
            

ejecutar_menu()
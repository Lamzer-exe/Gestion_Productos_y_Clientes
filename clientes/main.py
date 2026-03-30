import sys
import os

# Agregar el directorio padre al path para importaciones
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from modulos.cliente_regular import ClienteRegular
from modulos.cliente_premium import ClientePremium
from modulos.cliente_corporativo import ClienteCorporativo
from modulos.gestor_clientes import GestorClientes
from modulos.archivos import exportar_a_csv, importar_desde_csv, generar_reporte_txt, registrar_log
from modulos.excepciones import (
    EmailInvalidoError,
    TelefonoInvalidoError,
    ClienteExistenteError,
    ClienteNoEncontradoError
)


def mostrar_menu() -> None:
    """Muestra el menú principal del sistema."""
    print("\n" + "=" * 50)
    print("   SISTEMA DE GESTIÓN INTEGRAL DE CLIENTES (GIC)")
    print("=" * 50)
    print("1. Agregar cliente")
    print("2. Listar clientes")
    print("3. Buscar cliente por email")
    print("4. Eliminar cliente")
    print("5. Exportar a CSV")
    print("6. Importar desde CSV")
    print("7. Generar reporte TXT")
    print("8. Salir")
    print("-" * 50)


def seleccionar_tipo_cliente() -> int:
    """
    Muestra las opciones de tipo de cliente y retorna la selección.
    
    Returns:
        El número de opción seleccionada (1-3).
    """
    print("\nSeleccione el tipo de cliente:")
    print("1. Cliente Regular")
    print("2. Cliente Premium")
    print("3. Cliente Corporativo")
    
    while True:
        try:
            opcion = int(input("Opción: "))
            if 1 <= opcion <= 3:
                return opcion
            print("Por favor, seleccione una opción válida (1-3).")
        except ValueError:
            print("Por favor, ingrese un número válido.")


def agregar_cliente(gestor: GestorClientes) -> None:
    """
    Agrega un nuevo cliente al sistema.
    
    Args:
        gestor: El gestor de clientes.
    """
    print("\n--- AGREGAR NUEVO CLIENTE ---")
    
    tipo = seleccionar_tipo_cliente()
    
    try:
        nombre = input("Nombre: ").strip()
        if not nombre:
            print("Error: El nombre no puede estar vacío.")
            return
            
        email = input("Email: ").strip()
        telefono = input("Teléfono: ").strip()
        
        if tipo == 1:
            cliente = ClienteRegular(nombre, email, telefono)
        elif tipo == 2:
            cliente = ClientePremium(nombre, email, telefono)
        else:
            empresa = input("Empresa: ").strip()
            if not empresa:
                print("Error: La empresa no puede estar vacía para clientes corporativos.")
                return
            cliente = ClienteCorporativo(nombre, email, telefono, empresa)
        
        gestor.agregar_cliente(cliente)
        registrar_log(f"Cliente agregado: {email}")
        print(f"\nCliente '{nombre}' agregado exitosamente.")
        
    except EmailInvalidoError as e:
        print(f"\nError: {e.mensaje}")
    except TelefonoInvalidoError as e:
        print(f"\nError: {e.mensaje}")
    except ClienteExistenteError as e:
        print(f"\nError: {e.mensaje}")


def listar_clientes(gestor: GestorClientes) -> None:
    """
    Lista todos los clientes registrados.
    
    Args:
        gestor: El gestor de clientes.
    """
    print("\n--- LISTA DE CLIENTES ---")
    
    clientes = gestor.listar_clientes()
    
    if not clientes:
        print("No hay clientes registrados.")
        return
    
    print(f"Total de clientes: {len(clientes)}\n")
    
    for i, cliente in enumerate(clientes, 1):
        print(f"--- Cliente #{i} ---")
        print(cliente.mostrar_info())
        print()


def buscar_cliente(gestor: GestorClientes) -> None:
    """
    Busca un cliente por su email.
    
    Args:
        gestor: El gestor de clientes.
    """
    print("\n--- BUSCAR CLIENTE ---")
    
    email = input("Ingrese el email del cliente: ").strip()
    
    try:
        cliente = gestor.buscar_cliente(email)
        print("\nCliente encontrado:")
        print(cliente.mostrar_info())
        registrar_log(f"Búsqueda exitosa: {email}")
        
    except ClienteNoEncontradoError as e:
        print(f"\n{e.mensaje}")


def eliminar_cliente(gestor: GestorClientes) -> None:
    """
    Elimina un cliente por su email.
    
    Args:
        gestor: El gestor de clientes.
    """
    print("\n--- ELIMINAR CLIENTE ---")
    
    email = input("Ingrese el email del cliente a eliminar: ").strip()
    
    try:
        cliente = gestor.eliminar_cliente(email)
        registrar_log(f"Cliente eliminado: {email}")
        print(f"\nCliente '{cliente.nombre}' eliminado exitosamente.")
        
    except ClienteNoEncontradoError as e:
        print(f"\n{e.mensaje}")


def exportar_clientes(gestor: GestorClientes) -> None:
    """
    Exporta los clientes a un archivo CSV.
    
    Args:
        gestor: El gestor de clientes.
    """
    print("\n--- EXPORTAR A CSV ---")
    
    if gestor.obtener_cantidad_total() == 0:
        print("No hay clientes para exportar.")
        return
    
    try:
        exportar_a_csv(gestor)
        print("\nClientes exportados exitosamente a 'datos/clientes.csv'.")
    except Exception as e:
        print(f"\nError al exportar: {str(e)}")


def importar_clientes(gestor: GestorClientes) -> None:
    """
    Importa clientes desde un archivo CSV.
    
    Args:
        gestor: El gestor de clientes.
    """
    print("\n--- IMPORTAR DESDE CSV ---")
    
    try:
        cantidad = importar_desde_csv(gestor)
        print(f"\nSe importaron {cantidad} cliente(s) exitosamente.")
    except FileNotFoundError as e:
        print(f"\n{str(e)}")
    except Exception as e:
        print(f"\nError al importar: {str(e)}")


def generar_reporte(gestor: GestorClientes) -> None:
    """
    Genera un reporte en formato TXT.
    
    Args:
        gestor: El gestor de clientes.
    """
    print("\n--- GENERAR REPORTE ---")
    
    try:
        generar_reporte_txt(gestor)
        print("\nReporte generado exitosamente en 'reportes/resumen.txt'.")
    except Exception as e:
        print(f"\nError al generar reporte: {str(e)}")


def main() -> None:
    """Función principal que ejecuta el menú del sistema."""
    gestor = GestorClientes()
    registrar_log("Sistema GIC iniciado")
    
    print("\n¡Bienvenido al Sistema de Gestión Integral de Clientes!")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Seleccione una opción: ").strip()
            
            if opcion == '1':
                agregar_cliente(gestor)
            elif opcion == '2':
                listar_clientes(gestor)
            elif opcion == '3':
                buscar_cliente(gestor)
            elif opcion == '4':
                eliminar_cliente(gestor)
            elif opcion == '5':
                exportar_clientes(gestor)
            elif opcion == '6':
                importar_clientes(gestor)
            elif opcion == '7':
                generar_reporte(gestor)
            elif opcion == '8':
                registrar_log("Sistema GIC finalizado")
                print("\n¡Gracias por usar el Sistema GIC! Hasta pronto.")
                break
            else:
                print("\nOpción no válida. Por favor, seleccione una opción del 1 al 8.")
                
        except KeyboardInterrupt:
            registrar_log("Sistema GIC interrumpido por el usuario")
            print("\n\nSistema interrumpido. ¡Hasta pronto!")
            break
        except Exception as e:
            registrar_log(f"Error inesperado: {str(e)}", 'ERROR')
            print(f"\nError inesperado: {str(e)}")


if __name__ == "__main__":
    main()

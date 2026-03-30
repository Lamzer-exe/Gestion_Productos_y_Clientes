# --- Librería estándar de Python (viene con Python) ---
import os

# --- Librerías externas / de terceros (pip install ...) ---
from tabulate import tabulate

# --- Módulos y paquetes propios del proyecto ---


def leer_int(mensaje: str, minimo=None, maximo=None):
    """
    Solicita al usuario un número entero válido desde consola.

    Reglas:
    - Solo acepta números enteros positivos
    - Puede validar un valor mínimo y/o máximo

    Args:
        mensaje (str): mensaje mostrado al usuario.
        minimo (int | None): valor mínimo permitido.
        maximo (int | None): valor máximo permitido.

    Returns:
        int: número entero validado.
    """
    while True:
        dato = input(mensaje).strip()
        if not dato.isdigit():
            print("Debes ingresar un numero entero")
            continue

        num = int(dato)

        if minimo is not None and num < minimo:
            print(f"Debe ingresar una opcion valida mayor o igual a {minimo}")
            continue

        if maximo and num > maximo:
            print(f"Debe ingresar una opcion valida menor o igual a {maximo}")
            continue

        return num
    
def generar_id(diccionario, prefijo="P", largo=3):
    """
    Genera un ID incremental basado en las claves de un diccionario.

    Ejemplo:
        P001, P002, P003...

    Args:
        diccionario (dict): diccionario donde se almacenan los datos.
        prefijo (str): letra o texto inicial del ID.
        largo (int): cantidad de dígitos numéricos.

    Returns:
        str: nuevo ID generado.
    """
    max_num = 0

    for key in diccionario.keys():
        key = str(key)
        if key.startswith(prefijo):
            parte_num = key[len(prefijo):]  # lo que viene después del prefijo
            if parte_num.isdigit():
                num = int(parte_num)
                if num > max_num:
                    max_num = num

    nuevo = max_num + 1
    return f"{prefijo}{nuevo:0{largo}d}"
    


def imprimir_tabla(datos: dict, headers: list[str] | None = None, formato: str = "grid"):
    """
    Imprime un diccionario como tabla en consola usando la librería tabulate.

    La función recibe un diccionario simple o un diccionario de diccionarios y
    lo transforma en una tabla legible para mostrar en consola.

    Parámetros
    ----------
    datos : dict
        Diccionario a mostrar. Ejemplos válidos:
        - {"Ana": 6.5, "Juan": 5.8}
        - {"Ana": {"nota": 6.5, "asistencia": 95}}
    headers : list[str] | None, opcional
        Encabezados de la tabla. Si es None, se generan automáticamente.
    formato : str, opcional
        Estilo de la tabla (por defecto "grid").
        Ejemplos: "grid", "simple", "github", "fancy_grid".

    Retorna
    -------
    None
        La función solo imprime la tabla, no retorna valores.

    Requiere
    --------
    tabulate (librería externa)
    Instalar con: python -m pip install tabulate
    """

    if not datos:
        print("No hay datos para mostrar.")
        return

    filas = []

    # Caso 1: diccionario simple
    if not isinstance(next(iter(datos.values())), dict):
        if headers is None:
            headers = ["Clave", "Valor"]

        for clave, valor in datos.items():
            filas.append([clave, valor])

    # Caso 2: diccionario de diccionarios
    else:
        columnas = list(next(iter(datos.values())).keys())

        if headers is None:
            headers = ["Clave"] + columnas

        for clave, subdic in datos.items():
            filas.append([clave] + list(subdic.values()))

    print(tabulate(filas, headers=headers, tablefmt=formato))


def prueba_numeros(mensaje):
    """
    Solicita un número entero al usuario.

    Reglas:
    - Repite hasta que el valor ingresado sea un entero válido

    Args:
        mensaje (str): mensaje mostrado al usuario.

    Returns:
        int: número ingresado.
    """
    while True:
        valor = input(mensaje).strip()
        
        try:
            valor = int(valor)
            return valor
        except ValueError:
            print("❌ Debe ingresar un numero")


def prueba_letras(mensaje, largo):
    """
    Solicita texto al usuario y valida su contenido.

    Reglas:
    - '0' cancela la operación
    - Largo mínimo obligatorio
    - No se permiten solo números

    Args:
        mensaje (str): mensaje mostrado al usuario.
        largo (int): largo mínimo requerido.

    Returns:
        str | None: texto válido o None si se cancela.
    """
    while True:
        respuesta = input(mensaje)
        if respuesta == "0":
            return None

        if respuesta == "" or len(respuesta) < largo:
            print(f"\n❌ Ingrese un nombre valido porfavor y mayor o igual a {largo} caracteres")
            continue

        if respuesta.isdigit():
            print("\n❌ Debe ingresar palabra o frase, no se admite numeros.")
            continue
        
        return respuesta


def pausa():
    """
    Pausa la ejecución del programa hasta que el usuario presione ENTER.

    Returns:
        None
    """
    input("\nPresiona ENTER para continuar...\n")


def limpiar_consola():
    """
    Limpia la consola (compatible con Windows).

    Returns:
        None
    """
    os.system('cls')


def cancelaciones():
    """
    Muestra un mensaje estándar de cancelación de acción.

    Returns:
        None
    """
    print("❌ Accion cancelada...")


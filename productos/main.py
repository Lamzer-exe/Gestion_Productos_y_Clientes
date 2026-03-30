'''
Arranca el programa.
Mantiene el “ciclo principal” (while) que muestra el menú y ejecuta opciones.
Importa funciones desde otros módulos.
'''

#* Desde aqui se inicia el sistema de gestiones

from modulos.menu import ejecutar_menu  #Importar el modulo desde otro sitio

def main():
    """
    Función principal del programa.

    Su responsabilidad es iniciar la ejecución del sistema
    llamando al menú principal.
    """
    ejecutar_menu() #Nos lleva al menu

if __name__ == "__main__": #Al coincidir el nombre del archivo ejecuta su linea que da inicio al sistema
    """
    Punto de entrada del programa.

    Esta condición permite que el archivo se ejecute directamente
    y evita que el código se ejecute automáticamente si el módulo
    es importado desde otro archivo.
    """
    main()

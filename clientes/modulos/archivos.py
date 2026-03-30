"""
Módulo para manejo de archivos CSV, TXT y logs.
"""

import csv
import os
import logging
from datetime import datetime
from typing import List

from .cliente import Cliente
from .cliente_regular import ClienteRegular
from .cliente_premium import ClientePremium
from .cliente_corporativo import ClienteCorporativo
from .gestor_clientes import GestorClientes


# Configurar rutas base
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATOS_DIR = os.path.join(BASE_DIR, 'datos')
REPORTES_DIR = os.path.join(BASE_DIR, 'reportes')
LOGS_DIR = os.path.join(BASE_DIR, 'logs')

# Crear directorios si no existen
os.makedirs(DATOS_DIR, exist_ok=True)
os.makedirs(REPORTES_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)

# Configurar logging
logging.basicConfig(
    filename=os.path.join(LOGS_DIR, 'app.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def registrar_log(mensaje: str, nivel: str = 'INFO') -> None:
    """
    Registra un mensaje en el archivo de log.
    
    Args:
        mensaje: El mensaje a registrar.
        nivel: El nivel del log (INFO, WARNING, ERROR).
    """
    if nivel == 'INFO':
        logging.info(mensaje)
    elif nivel == 'WARNING':
        logging.warning(mensaje)
    elif nivel == 'ERROR':
        logging.error(mensaje)


def exportar_a_csv(gestor: GestorClientes, archivo: str = 'clientes.csv') -> bool:
    """
    Exporta los clientes a un archivo CSV.
    
    Args:
        gestor: El gestor de clientes con los datos.
        archivo: Nombre del archivo CSV de salida.
        
    Returns:
        True si la exportación fue exitosa.
    """
    ruta_archivo = os.path.join(DATOS_DIR, archivo)
    
    try:
        clientes = gestor.listar_clientes()
        
        with open(ruta_archivo, 'w', newline='', encoding='utf-8') as f:
            # Determinar los campos (incluir empresa para corporativos)
            campos = ['tipo', 'nombre', 'email', 'telefono', 'empresa']
            writer = csv.DictWriter(f, fieldnames=campos)
            
            writer.writeheader()
            for cliente in clientes:
                data = cliente.to_dict()
                # Asegurar que empresa tenga un valor aunque sea vacío
                if 'empresa' not in data:
                    data['empresa'] = ''
                writer.writerow(data)
        
        registrar_log(f"Exportación exitosa a {archivo}. Total: {len(clientes)} clientes.")
        return True
        
    except Exception as e:
        registrar_log(f"Error al exportar a CSV: {str(e)}", 'ERROR')
        raise


def importar_desde_csv(gestor: GestorClientes, archivo: str = 'clientes_entrada.csv') -> int:
    """
    Importa clientes desde un archivo CSV.
    
    Args:
        gestor: El gestor de clientes donde agregar los datos.
        archivo: Nombre del archivo CSV de entrada.
        
    Returns:
        Número de clientes importados exitosamente.
        
    Raises:
        FileNotFoundError: Si el archivo no existe.
    """
    ruta_archivo = os.path.join(DATOS_DIR, archivo)
    clientes_importados = 0
    errores = 0
    
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for fila in reader:
                try:
                    tipo = fila.get('tipo', 'ClienteRegular')
                    nombre = fila.get('nombre', '')
                    email = fila.get('email', '')
                    telefono = fila.get('telefono', '')
                    empresa = fila.get('empresa', '')
                    
                    # Crear el cliente según el tipo
                    if tipo == 'ClienteCorporativo':
                        cliente = ClienteCorporativo(nombre, email, telefono, empresa)
                    elif tipo == 'ClientePremium':
                        cliente = ClientePremium(nombre, email, telefono)
                    else:
                        cliente = ClienteRegular(nombre, email, telefono)
                    
                    gestor.agregar_cliente(cliente)
                    clientes_importados += 1
                    
                except Exception as e:
                    errores += 1
                    registrar_log(f"Error al importar cliente: {str(e)}", 'WARNING')
        
        registrar_log(f"Importación completada. Importados: {clientes_importados}, Errores: {errores}")
        return clientes_importados
        
    except FileNotFoundError:
        registrar_log(f"Archivo no encontrado: {archivo}", 'ERROR')
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_archivo}")


def generar_reporte_txt(gestor: GestorClientes, archivo: str = 'resumen.txt') -> bool:
    """
    Genera un reporte en formato TXT con el resumen de clientes.
    
    Args:
        gestor: El gestor de clientes con los datos.
        archivo: Nombre del archivo de reporte.
        
    Returns:
        True si el reporte se generó exitosamente.
    """
    ruta_archivo = os.path.join(REPORTES_DIR, archivo)
    
    try:
        clientes = gestor.listar_clientes()
        cantidad_total = gestor.obtener_cantidad_total()
        cantidad_por_tipo = gestor.obtener_cantidad_por_tipo()
        
        with open(ruta_archivo, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write("        REPORTE DE CLIENTES - SISTEMA GIC\n")
            f.write("=" * 60 + "\n\n")
            
            f.write(f"Fecha de generación: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("-" * 40 + "\n")
            f.write("RESUMEN GENERAL\n")
            f.write("-" * 40 + "\n")
            f.write(f"Total de clientes: {cantidad_total}\n\n")
            
            f.write("Cantidad por tipo:\n")
            for tipo, cantidad in cantidad_por_tipo.items():
                f.write(f"  - {tipo}: {cantidad}\n")
            
            f.write("\n" + "-" * 40 + "\n")
            f.write("DETALLE DE CLIENTES\n")
            f.write("-" * 40 + "\n\n")
            
            for i, cliente in enumerate(clientes, 1):
                f.write(f"Cliente #{i}\n")
                f.write(cliente.mostrar_info() + "\n")
                f.write("\n")
            
            f.write("=" * 60 + "\n")
            f.write("        FIN DEL REPORTE\n")
            f.write("=" * 60 + "\n")
        
        registrar_log(f"Reporte generado exitosamente: {archivo}")
        return True
        
    except Exception as e:
        registrar_log(f"Error al generar reporte: {str(e)}", 'ERROR')
        raise

"""
Módulo de gestión de clientes - Proyecto GIC
"""

from .excepciones import (
    EmailInvalidoError,
    TelefonoInvalidoError,
    ClienteExistenteError,
    ClienteNoEncontradoError
)
from .validaciones import validar_email, validar_telefono
from .cliente import Cliente
from .cliente_regular import ClienteRegular
from .cliente_premium import ClientePremium
from .cliente_corporativo import ClienteCorporativo
from .gestor_clientes import GestorClientes
from .archivos import (
    exportar_a_csv,
    importar_desde_csv,
    generar_reporte_txt,
    registrar_log
)

__all__ = [
    'EmailInvalidoError',
    'TelefonoInvalidoError',
    'ClienteExistenteError',
    'ClienteNoEncontradoError',
    'validar_email',
    'validar_telefono',
    'Cliente',
    'ClienteRegular',
    'ClientePremium',
    'ClienteCorporativo',
    'GestorClientes',
    'exportar_a_csv',
    'importar_desde_csv',
    'generar_reporte_txt',
    'registrar_log'
]

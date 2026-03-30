"""
Módulo de validaciones para email y teléfono usando expresiones regulares.
"""

import re
from .excepciones import EmailInvalidoError, TelefonoInvalidoError


def validar_email(email: str) -> bool:
    """
    Valida el formato de un email usando regex.
    
    Args:
        email: El email a validar.
        
    Returns:
        True si el email es válido.
        
    Raises:
        EmailInvalidoError: Si el formato del email es inválido.
    """
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not email or not re.match(patron, email):
        raise EmailInvalidoError(email)
    
    return True


def validar_telefono(telefono: str) -> bool:
    """
    Valida el formato de un teléfono usando regex.
    Acepta formatos: +52 123 456 7890, 1234567890, 123-456-7890, (123) 456-7890
    
    Args:
        telefono: El teléfono a validar.
        
    Returns:
        True si el teléfono es válido.
        
    Raises:
        TelefonoInvalidoError: Si el formato del teléfono es inválido.
    """
    # Eliminar espacios y caracteres de formato para validación
    telefono_limpio = re.sub(r'[\s\-\(\)\+]', '', telefono)
    
    # Validar que tenga entre 7 y 15 dígitos
    patron = r'^\d{7,15}$'
    
    if not telefono or not re.match(patron, telefono_limpio):
        raise TelefonoInvalidoError(telefono)
    
    return True

"""
Módulo de excepciones personalizadas para el sistema de gestión de clientes.
"""


class EmailInvalidoError(Exception):
    """Excepción lanzada cuando el formato del email es inválido."""
    
    def __init__(self, email: str, mensaje: str = "El formato del email es inválido"):
        self.email = email
        self.mensaje = f"{mensaje}: {email}"
        super().__init__(self.mensaje)


class TelefonoInvalidoError(Exception):
    """Excepción lanzada cuando el formato del teléfono es inválido."""
    
    def __init__(self, telefono: str, mensaje: str = "El formato del teléfono es inválido"):
        self.telefono = telefono
        self.mensaje = f"{mensaje}: {telefono}"
        super().__init__(self.mensaje)


class ClienteExistenteError(Exception):
    """Excepción lanzada cuando se intenta agregar un cliente que ya existe."""
    
    def __init__(self, email: str, mensaje: str = "Ya existe un cliente con este email"):
        self.email = email
        self.mensaje = f"{mensaje}: {email}"
        super().__init__(self.mensaje)


class ClienteNoEncontradoError(Exception):
    """Excepción lanzada cuando no se encuentra un cliente."""
    
    def __init__(self, email: str, mensaje: str = "No se encontró el cliente con email"):
        self.email = email
        self.mensaje = f"{mensaje}: {email}"
        super().__init__(self.mensaje)

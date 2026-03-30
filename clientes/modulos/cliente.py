"""
Módulo que define la clase base Cliente con encapsulación y validaciones.
"""

from .validaciones import validar_email, validar_telefono


class Cliente:
    """
    Clase base que representa un cliente del sistema.
    
    Attributes:
        __nombre (str): Nombre del cliente (privado).
        __email (str): Email del cliente (privado).
        __telefono (str): Teléfono del cliente (privado).
    """
    
    def __init__(self, nombre: str, email: str, telefono: str):
        """
        Inicializa un nuevo cliente con validaciones.
        
        Args:
            nombre: Nombre del cliente.
            email: Email del cliente.
            telefono: Teléfono del cliente.
            
        Raises:
            EmailInvalidoError: Si el email no tiene formato válido.
            TelefonoInvalidoError: Si el teléfono no tiene formato válido.
        """
        self.__nombre = nombre
        
        # Validar email antes de asignar
        validar_email(email)
        self.__email = email
        
        # Validar teléfono antes de asignar
        validar_telefono(telefono)
        self.__telefono = telefono
    
    # Propiedades para acceder a los atributos privados
    @property
    def nombre(self) -> str:
        """Obtiene el nombre del cliente."""
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor: str):
        """Establece el nombre del cliente."""
        self.__nombre = valor
    
    @property
    def email(self) -> str:
        """Obtiene el email del cliente."""
        return self.__email
    
    @email.setter
    def email(self, valor: str):
        """Establece el email del cliente con validación."""
        validar_email(valor)
        self.__email = valor
    
    @property
    def telefono(self) -> str:
        """Obtiene el teléfono del cliente."""
        return self.__telefono
    
    @telefono.setter
    def telefono(self, valor: str):
        """Establece el teléfono del cliente con validación."""
        validar_telefono(valor)
        self.__telefono = valor
    
    def mostrar_info(self) -> str:
        """
        Muestra la información del cliente en formato legible.
        
        Returns:
            String con la información del cliente.
        """
        return (
            f"Tipo: {self.__class__.__name__}\n"
            f"Nombre: {self.__nombre}\n"
            f"Email: {self.__email}\n"
            f"Teléfono: {self.__telefono}"
        )
    
    def to_dict(self) -> dict:
        """
        Convierte el cliente a un diccionario.
        
        Returns:
            Diccionario con los datos del cliente.
        """
        return {
            'tipo': self.__class__.__name__,
            'nombre': self.__nombre,
            'email': self.__email,
            'telefono': self.__telefono
        }
    
    def __str__(self) -> str:
        """Representación en string del cliente."""
        return f"{self.__class__.__name__}: {self.__nombre} ({self.__email})"
    
    def __repr__(self) -> str:
        """Representación oficial del cliente."""
        return f"{self.__class__.__name__}(nombre='{self.__nombre}', email='{self.__email}', telefono='{self.__telefono}')"

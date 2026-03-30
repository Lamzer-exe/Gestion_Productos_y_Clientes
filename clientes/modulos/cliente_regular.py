"""
Módulo que define la clase ClienteRegular.
"""

from .cliente import Cliente


class ClienteRegular(Cliente):
    """
    Clase que representa un cliente regular del sistema.
    Hereda de Cliente sin atributos adicionales.
    """
    
    def __init__(self, nombre: str, email: str, telefono: str):
        """
        Inicializa un cliente regular.
        
        Args:
            nombre: Nombre del cliente.
            email: Email del cliente.
            telefono: Teléfono del cliente.
        """
        super().__init__(nombre, email, telefono)
    
    def mostrar_info(self) -> str:
        """
        Muestra la información del cliente regular.
        
        Returns:
            String con la información del cliente.
        """
        info_base = super().mostrar_info()
        return f"{info_base}\nCategoría: Regular"

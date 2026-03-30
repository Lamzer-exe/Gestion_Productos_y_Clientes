"""
Módulo que define la clase ClientePremium.
"""

from .cliente import Cliente


class ClientePremium(Cliente):
    """
    Clase que representa un cliente premium del sistema.
    Hereda de Cliente sin atributos adicionales pero con beneficios premium.
    """
    
    def __init__(self, nombre: str, email: str, telefono: str):
        """
        Inicializa un cliente premium.
        
        Args:
            nombre: Nombre del cliente.
            email: Email del cliente.
            telefono: Teléfono del cliente.
        """
        super().__init__(nombre, email, telefono)
    
    def mostrar_info(self) -> str:
        """
        Muestra la información del cliente premium.
        
        Returns:
            String con la información del cliente.
        """
        info_base = super().mostrar_info()
        return f"{info_base}\nCategoría: Premium ⭐"

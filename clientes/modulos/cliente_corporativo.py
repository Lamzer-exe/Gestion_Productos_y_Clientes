"""
Módulo que define la clase ClienteCorporativo.
"""

from .cliente import Cliente


class ClienteCorporativo(Cliente):
    """
    Clase que representa un cliente corporativo del sistema.
    Hereda de Cliente con atributo adicional 'empresa'.
    """
    
    def __init__(self, nombre: str, email: str, telefono: str, empresa: str):
        """
        Inicializa un cliente corporativo.
        
        Args:
            nombre: Nombre del cliente.
            email: Email del cliente.
            telefono: Teléfono del cliente.
            empresa: Nombre de la empresa del cliente.
        """
        super().__init__(nombre, email, telefono)
        self.__empresa = empresa
    
    @property
    def empresa(self) -> str:
        """Obtiene el nombre de la empresa."""
        return self.__empresa
    
    @empresa.setter
    def empresa(self, valor: str):
        """Establece el nombre de la empresa."""
        self.__empresa = valor
    
    def mostrar_info(self) -> str:
        """
        Muestra la información del cliente corporativo.
        
        Returns:
            String con la información del cliente incluyendo empresa.
        """
        info_base = super().mostrar_info()
        return f"{info_base}\nEmpresa: {self.__empresa}\nCategoría: Corporativo"
    
    def to_dict(self) -> dict:
        """
        Convierte el cliente corporativo a un diccionario.
        Sobrescribe el método padre para incluir el atributo empresa.
        
        Returns:
            Diccionario con los datos del cliente incluyendo empresa.
        """
        data = super().to_dict()
        data['empresa'] = self.__empresa
        return data

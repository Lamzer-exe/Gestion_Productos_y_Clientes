"""
Módulo que define el gestor de clientes para administrar la lista de clientes.
"""

from typing import List, Optional
from .cliente import Cliente
from .excepciones import ClienteExistenteError, ClienteNoEncontradoError


class GestorClientes:
    """
    Clase para gestionar una lista de clientes.
    Permite agregar, listar, buscar y eliminar clientes.
    """
    
    def __init__(self):
        """Inicializa el gestor con una lista vacía de clientes."""
        self.__clientes: List[Cliente] = []
    
    @property
    def clientes(self) -> List[Cliente]:
        """Obtiene una copia de la lista de clientes."""
        return self.__clientes.copy()
    
    def agregar_cliente(self, cliente: Cliente) -> None:
        """
        Agrega un nuevo cliente a la lista.
        
        Args:
            cliente: El cliente a agregar.
            
        Raises:
            ClienteExistenteError: Si ya existe un cliente con el mismo email.
        """
        # Verificar si ya existe un cliente con el mismo email
        for c in self.__clientes:
            if c.email.lower() == cliente.email.lower():
                raise ClienteExistenteError(cliente.email)
        
        self.__clientes.append(cliente)
    
    def listar_clientes(self) -> List[Cliente]:
        """
        Lista todos los clientes registrados.
        
        Returns:
            Lista de todos los clientes.
        """
        return self.__clientes.copy()
    
    def buscar_cliente(self, email: str) -> Cliente:
        """
        Busca un cliente por su email.
        
        Args:
            email: El email del cliente a buscar.
            
        Returns:
            El cliente encontrado.
            
        Raises:
            ClienteNoEncontradoError: Si no se encuentra el cliente.
        """
        for cliente in self.__clientes:
            if cliente.email.lower() == email.lower():
                return cliente
        
        raise ClienteNoEncontradoError(email)
    
    def eliminar_cliente(self, email: str) -> Cliente:
        """
        Elimina un cliente por su email.
        
        Args:
            email: El email del cliente a eliminar.
            
        Returns:
            El cliente eliminado.
            
        Raises:
            ClienteNoEncontradoError: Si no se encuentra el cliente.
        """
        for i, cliente in enumerate(self.__clientes):
            if cliente.email.lower() == email.lower():
                return self.__clientes.pop(i)
        
        raise ClienteNoEncontradoError(email)
    
    def obtener_cantidad_total(self) -> int:
        """
        Obtiene la cantidad total de clientes.
        
        Returns:
            Número total de clientes.
        """
        return len(self.__clientes)
    
    def obtener_cantidad_por_tipo(self) -> dict:
        """
        Obtiene la cantidad de clientes agrupados por tipo.
        
        Returns:
            Diccionario con el conteo por tipo de cliente.
        """
        conteo = {}
        for cliente in self.__clientes:
            tipo = cliente.__class__.__name__
            conteo[tipo] = conteo.get(tipo, 0) + 1
        return conteo
    
    def limpiar(self) -> None:
        """Elimina todos los clientes de la lista."""
        self.__clientes.clear()

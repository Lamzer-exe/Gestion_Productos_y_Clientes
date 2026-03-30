"""
Módulo de pruebas unitarias para el sistema de gestión de clientes.
"""

import unittest
import sys
import os

# Agregar el directorio padre al path para importaciones
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modulos.cliente import Cliente
from modulos.cliente_regular import ClienteRegular
from modulos.cliente_premium import ClientePremium
from modulos.cliente_corporativo import ClienteCorporativo
from modulos.gestor_clientes import GestorClientes
from modulos.excepciones import (
    EmailInvalidoError,
    TelefonoInvalidoError,
    ClienteExistenteError,
    ClienteNoEncontradoError
)


class TestCliente(unittest.TestCase):
    """Pruebas para la clase Cliente y sus subclases."""
    
    def test_crear_cliente_valido(self):
        """Prueba la creación de un cliente con datos válidos."""
        cliente = ClienteRegular("Juan Pérez", "juan@ejemplo.com", "1234567890")
        
        self.assertEqual(cliente.nombre, "Juan Pérez")
        self.assertEqual(cliente.email, "juan@ejemplo.com")
        self.assertEqual(cliente.telefono, "1234567890")
    
    def test_crear_cliente_premium(self):
        """Prueba la creación de un cliente premium."""
        cliente = ClientePremium("María López", "maria@ejemplo.com", "9876543210")
        
        self.assertEqual(cliente.nombre, "María López")
        self.assertIsInstance(cliente, ClientePremium)
    
    def test_crear_cliente_corporativo(self):
        """Prueba la creación de un cliente corporativo con empresa."""
        cliente = ClienteCorporativo(
            "Carlos Ruiz", 
            "carlos@empresa.com", 
            "5555555555",
            "TechCorp S.A."
        )
        
        self.assertEqual(cliente.empresa, "TechCorp S.A.")
        self.assertIn('empresa', cliente.to_dict())
    
    def test_email_invalido_lanza_excepcion(self):
        """Prueba que un email inválido lanza EmailInvalidoError."""
        with self.assertRaises(EmailInvalidoError):
            ClienteRegular("Test", "email-invalido", "1234567890")
    
    def test_email_sin_arroba_lanza_excepcion(self):
        """Prueba que un email sin @ lanza EmailInvalidoError."""
        with self.assertRaises(EmailInvalidoError):
            ClienteRegular("Test", "emailsinarroba.com", "1234567890")
    
    def test_email_vacio_lanza_excepcion(self):
        """Prueba que un email vacío lanza EmailInvalidoError."""
        with self.assertRaises(EmailInvalidoError):
            ClienteRegular("Test", "", "1234567890")
    
    def test_telefono_invalido_lanza_excepcion(self):
        """Prueba que un teléfono inválido lanza TelefonoInvalidoError."""
        with self.assertRaises(TelefonoInvalidoError):
            ClienteRegular("Test", "test@ejemplo.com", "abc")
    
    def test_telefono_muy_corto_lanza_excepcion(self):
        """Prueba que un teléfono muy corto lanza TelefonoInvalidoError."""
        with self.assertRaises(TelefonoInvalidoError):
            ClienteRegular("Test", "test@ejemplo.com", "123")
    
    def test_telefono_vacio_lanza_excepcion(self):
        """Prueba que un teléfono vacío lanza TelefonoInvalidoError."""
        with self.assertRaises(TelefonoInvalidoError):
            ClienteRegular("Test", "test@ejemplo.com", "")
    
    def test_to_dict_cliente_regular(self):
        """Prueba que to_dict retorna los campos correctos."""
        cliente = ClienteRegular("Ana García", "ana@test.com", "1111111111")
        data = cliente.to_dict()
        
        self.assertEqual(data['nombre'], "Ana García")
        self.assertEqual(data['email'], "ana@test.com")
        self.assertEqual(data['telefono'], "1111111111")
        self.assertEqual(data['tipo'], "ClienteRegular")
    
    def test_mostrar_info(self):
        """Prueba que mostrar_info retorna información formateada."""
        cliente = ClienteRegular("Pedro Sánchez", "pedro@test.com", "2222222222")
        info = cliente.mostrar_info()
        
        self.assertIn("Pedro Sánchez", info)
        self.assertIn("pedro@test.com", info)
        self.assertIn("2222222222", info)


class TestGestorClientes(unittest.TestCase):
    """Pruebas para la clase GestorClientes."""
    
    def setUp(self):
        """Configura el gestor antes de cada prueba."""
        self.gestor = GestorClientes()
    
    def test_agregar_cliente(self):
        """Prueba agregar un cliente al gestor."""
        cliente = ClienteRegular("Test User", "test@example.com", "1234567890")
        self.gestor.agregar_cliente(cliente)
        
        self.assertEqual(self.gestor.obtener_cantidad_total(), 1)
    
    def test_agregar_cliente_duplicado_lanza_excepcion(self):
        """Prueba que agregar un cliente duplicado lanza ClienteExistenteError."""
        cliente1 = ClienteRegular("User 1", "mismo@email.com", "1234567890")
        cliente2 = ClientePremium("User 2", "mismo@email.com", "9876543210")
        
        self.gestor.agregar_cliente(cliente1)
        
        with self.assertRaises(ClienteExistenteError):
            self.gestor.agregar_cliente(cliente2)
    
    def test_buscar_cliente_existente(self):
        """Prueba buscar un cliente que existe."""
        cliente = ClienteRegular("Buscar User", "buscar@test.com", "1234567890")
        self.gestor.agregar_cliente(cliente)
        
        encontrado = self.gestor.buscar_cliente("buscar@test.com")
        
        self.assertEqual(encontrado.nombre, "Buscar User")
    
    def test_buscar_cliente_no_existente_lanza_excepcion(self):
        """Prueba que buscar un cliente inexistente lanza ClienteNoEncontradoError."""
        with self.assertRaises(ClienteNoEncontradoError):
            self.gestor.buscar_cliente("noexiste@test.com")
    
    def test_eliminar_cliente(self):
        """Prueba eliminar un cliente existente."""
        cliente = ClienteRegular("Eliminar User", "eliminar@test.com", "1234567890")
        self.gestor.agregar_cliente(cliente)
        
        self.assertEqual(self.gestor.obtener_cantidad_total(), 1)
        
        eliminado = self.gestor.eliminar_cliente("eliminar@test.com")
        
        self.assertEqual(eliminado.nombre, "Eliminar User")
        self.assertEqual(self.gestor.obtener_cantidad_total(), 0)
    
    def test_eliminar_cliente_no_existente_lanza_excepcion(self):
        """Prueba que eliminar un cliente inexistente lanza ClienteNoEncontradoError."""
        with self.assertRaises(ClienteNoEncontradoError):
            self.gestor.eliminar_cliente("noexiste@test.com")
    
    def test_listar_clientes(self):
        """Prueba listar todos los clientes."""
        cliente1 = ClienteRegular("User 1", "user1@test.com", "1111111111")
        cliente2 = ClientePremium("User 2", "user2@test.com", "2222222222")
        
        self.gestor.agregar_cliente(cliente1)
        self.gestor.agregar_cliente(cliente2)
        
        clientes = self.gestor.listar_clientes()
        
        self.assertEqual(len(clientes), 2)
    
    def test_obtener_cantidad_por_tipo(self):
        """Prueba obtener cantidad de clientes por tipo."""
        self.gestor.agregar_cliente(ClienteRegular("R1", "r1@test.com", "1111111111"))
        self.gestor.agregar_cliente(ClienteRegular("R2", "r2@test.com", "2222222222"))
        self.gestor.agregar_cliente(ClientePremium("P1", "p1@test.com", "3333333333"))
        self.gestor.agregar_cliente(ClienteCorporativo("C1", "c1@test.com", "4444444444", "Empresa"))
        
        conteo = self.gestor.obtener_cantidad_por_tipo()
        
        self.assertEqual(conteo.get('ClienteRegular', 0), 2)
        self.assertEqual(conteo.get('ClientePremium', 0), 1)
        self.assertEqual(conteo.get('ClienteCorporativo', 0), 1)


class TestValidaciones(unittest.TestCase):
    """Pruebas adicionales para validaciones."""
    
    def test_email_formatos_validos(self):
        """Prueba varios formatos de email válidos."""
        emails_validos = [
            "simple@ejemplo.com",
            "nombre.apellido@ejemplo.com",
            "nombre+tag@ejemplo.com",
            "nombre@subdominio.ejemplo.com",
        ]
        
        for email in emails_validos:
            try:
                cliente = ClienteRegular("Test", email, "1234567890")
                self.assertEqual(cliente.email, email)
            except EmailInvalidoError:
                self.fail(f"Email válido rechazado: {email}")
    
    def test_telefono_formatos_validos(self):
        """Prueba varios formatos de teléfono válidos."""
        telefonos_validos = [
            "1234567890",
            "123-456-7890",
            "(123) 456-7890",
            "+52 123 456 7890",
        ]
        
        for i, telefono in enumerate(telefonos_validos):
            try:
                cliente = ClienteRegular("Test", f"test{i}@ejemplo.com", telefono)
                # Solo verificar que se creó sin error
                self.assertIsNotNone(cliente)
            except TelefonoInvalidoError:
                self.fail(f"Teléfono válido rechazado: {telefono}")


if __name__ == '__main__':
    # Ejecutar las pruebas
    unittest.main(verbosity=2)

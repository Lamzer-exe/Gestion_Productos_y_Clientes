# Sistema de Gestión de Productos – Python

Sistema de gestión de productos desarrollado en **Python**, orientado a consola, que permite administrar productos, realizar ventas y mantener control de stock.

Proyecto correspondiente al **Examen del Módulo 3 – Introducción a Python**.

---

## Objetivo del proyecto

Desarrollar una aplicación modular en Python que implemente:
- Manejo de diccionarios
- Funciones reutilizables
- Validaciones de datos
- Control de errores
- Navegación mediante menú en consola

---

## Funcionalidades

-  Listar productos en tablas
-  Agregar productos
-  Editar productos por ID
-  Eliminar productos
-  Vender productos (descuento de stock)
-  Buscar productos por ID o nombre
-  Cancelación global de acciones ingresando `0`
-  Generación automática de IDs
-  Visualización en tablas con `tabulate`

---

## Estructura del proyecto

Examen_Modulo_3/
│
├── main.py
│
├── modulos/
│ ├── menu.py
│ ├── datos_basicos.py
│ ├── funciones_utiles.py
│ └── validaciones.py
│
└── README.md

---

## Estructura de los datos

Los productos se almacenan en un diccionario con la siguiente estructura:

```python
{
    "P001": {
        "nombre": "pan",
        "descripcion": "pan integral",
        "precio": 1200,
        "stock": 10
    }
}

Descripción de módulos

main.py

Archivo principal del sistema.
Ejecuta el menú principal y da inicio a la aplicación.

-----------------------------------------
menu.py

Gestiona la navegación del sistema:

Muestra el menú

Ejecuta las acciones según la opción elegida

-----------------------------------------
datos_basicos.py

Contiene los datos base del sistema:

Diccionario global PRODUCTOS

-----------------------------------------
funciones_utiles.py

Funciones auxiliares reutilizables:

Lectura segura de números

Generación automática de IDs

Impresión de tablas

Validaciones de texto y números

Pausas, limpieza de consola y cancelaciones

-----------------------------------------
validaciones.py

Contiene la lógica de validación:

Verificación de existencia de productos

Validación de precio y stock

Búsqueda por ID o nombre

Descuento seguro de stock

Control de errores y cancelaciones

---------------------------------------

❌ Cancelación global

En cualquier ingreso de datos, el usuario puede escribir:

0

Para cancelar la acción y volver al menú anterior.

---------------------------------------

Requisitos

Python 3.10 o superior

Librería externa:

pip install tabulate

---------------------------------------

▶️ Ejecución del programa

Desde la carpeta raíz del proyecto:

python main.py

--------------------------------------

Consideraciones técnicas

Aplicación 100% en consola

Datos almacenados en memoria

Código modular y reutilizable

Uso de match-case

Validaciones centralizadas

Manejo de errores con control de flujo

---------------------------------------

Autor

Exequiel Uribe
Examen Módulo 3 – Python
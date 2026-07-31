import random

# Lista de datos curiosos locales para probar sin usar dinero/API
DATOS_CURIOSOS_LOCALES = [
    "La salsa nació en Nueva York en la década de 1960 gracias a la mezcla de ritmos caribeños como el son cubano y el mambo con el jazz estadounidense.",
    "El término 'Salsa' fue popularizado por el sello Fania Records para comercializar la mezcla de ritmos latinos bajo un solo nombre pegajoso.",
    "Fania All-Stars realizó un histórico concierto en Zaire (África) en 1974 durante el marco de la pelea entre Muhammad Ali y George Foreman."
]

def generar_dato_curioso(titulo_nodo, descripcion_nodo):
    """
    Simula la generación de un dato curioso devolviendo un dato local aleatorio.
    (Versión offline / sin costo).
    """
    return random.choice(DATOS_CURIOSOS_LOCALES)
import random

# Datos curiosos por ID de nodo
DATOS_POR_NODO = {
    1: [
        "La salsa nació en Nueva York en la década de 1960 gracias a la mezcla de ritmos caribeños con el jazz estadounidense.",
        "El término 'Salsa' fue popularizado por el sello Fania Records para comercializar la mezcla de ritmos latinos."
    ],
    2: [
        "Celia Cruz grabó más de 70 álbumes a lo largo de su carrera y ganó múltiples premios Grammy.",
        "El famoso grito '!Azúcar!' de Celia Cruz nació de una anécdota en un restaurante cubano en Miami."
    ],
    3: [
        "Héctor Lavoe fue apodado 'El Cantante de los Cantantes' por su estilo único de fildeo e improvisación.",
        "El álbum 'Comedia' de 1978 incluye el tema 'El Cantante', compuesto especialmente para él por Rubén Blades."
    ]
}

def generar_dato_curioso(nodo_id, titulo_nodo="", descripcion_nodo=""):
    """
    Devuelve un dato curioso local basado en el ID del nodo actual.
    """
    # Si el ID existe en el diccionario, saca uno aleatorio de ese nodo
    if nodo_id in DATOS_POR_NODO:
        return random.choice(DATOS_POR_NODO[nodo_id])
    
    # Dato por defecto si el ID no está registrado
    return "La música latina ha influenciado fuertemente la cultura popular mundial a lo largo de las décadas."
import random

# Datos curiosos por ID de nodo de la linea de tiempo.
# NOTA: esta funcion todavia no esta conectada a ninguna ruta/endpoint
# -- es el servicio "de respaldo local" pensado para cuando se integre
# la llamada real a la API de Anthropic (con try/except alrededor).
DATOS_POR_NODO = {
    1: [
        "La salsa nació en Nueva York en la década de 1960 gracias a la mezcla de ritmos caribeños con el jazz estadounidense.",
        "El término 'Salsa' fue popularizado por el sello Fania Records para comercializar la mezcla de ritmos latinos."
    ],
    2: [
        "Celia Cruz grabó más de 70 álbumes a lo largo de su carrera y ganó múltiples premios Grammy.",
        "El famoso grito '¡Azúcar!' de Celia Cruz nació de una anécdota en un restaurante cubano en Miami."
    ],
    3: [
        "Héctor Lavoe fue apodado 'El Cantante de los Cantantes' por su estilo único de fildeo e improvisación.",
        "El álbum 'Comedia' de 1978 incluye el tema 'El Cantante', compuesto especialmente para él por Rubén Blades."
    ]
}


def generar_dato_curioso(nodo_id, titulo_nodo="", descripcion_nodo=""):
    """
    Devuelve un dato curioso local basado en el ID del nodo actual.
    (Version offline / sin costo -- no depende de la API de Anthropic).
    """
    if nodo_id in DATOS_POR_NODO:
        return random.choice(DATOS_POR_NODO[nodo_id])

    return "La música latina ha influenciado fuertemente la cultura popular mundial a lo largo de las décadas."

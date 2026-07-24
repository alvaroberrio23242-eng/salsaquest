# app/models/timeline_data.py
"""
Datos de la línea de tiempo de SalsaQuest.
Por ahora es una lista de diccionarios en Python (datos "hardcodeados").
Más adelante esto se migrará a una tabla real en SQLite usando SQLAlchemy,
pero mantenemos la misma estructura de campos para que la migración sea directa.
"""

timeline_nodes = [
    {
        "id": 1,
        "era": "raices",
        "anio_inicio": 1900,
        "anio_fin": 1940,
        "titulo": "Son cubano",
        "descripcion_corta": "La fusión de ritmos africanos y españoles en Cuba que dio origen a la salsa.",
        "imagen": "son_cubano.jpg",
        "orden": 1,
    },
    {
        "id": 2,
        "era": "nueva_york",
        "anio_inicio": 1940,
        "anio_fin": 1960,
        "titulo": "Migración y Latin Jazz en Nueva York",
        "descripcion_corta": "La migración puertorriqueña y cubana a NYC mezcla el son con el jazz, sentando las bases de la salsa moderna.",
        "imagen": "nyc_latin_jazz.jpg",
        "orden": 2,
    },
    {
        "id": 3,
        "era": "fania",
        "anio_inicio": 1960,
        "anio_fin": 1975,
        "titulo": "Fania Records populariza la 'salsa'",
        "descripcion_corta": "El sello discográfico Fania reúne a los grandes músicos del género y consolida el nombre 'salsa'.",
        "imagen": "fania_all_stars.jpg",
        "orden": 3,
    },
]


def obtener_todos_los_nodos():
    """Devuelve todos los nodos ordenados cronológicamente."""
    return sorted(timeline_nodes, key=lambda nodo: nodo["orden"])


def obtener_nodo_por_id(nodo_id):
    """Busca un nodo específico por su id. Devuelve None si no existe."""
    for nodo in timeline_nodes:
        if nodo["id"] == nodo_id:
            return nodo
    return None
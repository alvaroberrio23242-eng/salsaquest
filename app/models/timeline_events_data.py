# app/models/timeline_events_data.py
"""
Fuente UNICA de datos de la linea del tiempo (EVENTOS_TIMELINE).

La consumen init_db.py y app/routes/timeline.py. No duplicar esta
lista en otro lado (la duplicacion init_db/timeline fue la causa de
datos divergentes entre entornos).

Orden cronologico: SIEMPRE via _anio_numerico (regex sobre el campo
anio, que puede ser "1967" o rangos como "1900-1940"), nunca
alfabetico ni SQL .asc() -- el orden alfabético de strings rompe con
formatos mixtos de año.

Videos (audio_url): solo IDs verificados como existentes via oEmbed de
YouTube (canal/oficialidad revisada a mano). Una version anterior de
este dataset llevaba 7 IDs inventados que daban 404 y rompian los
embeds; por eso cualquier audio_url fuera de esta lista se considera
invalido y se neutraliza en el siembra/backfill (ver timeline.py).
"""

import re

_ANIO_RE = re.compile(r"\d{1,4}")


def _anio_numerico(anio):
    """Extrae el primer numero del anio ("1900-1940" -> 1900).
    Sin numero => 9999 (queda al final, orden estable)."""
    m = _ANIO_RE.search(str(anio or ""))
    return int(m.group()) if m else 9999


# Columnas reales del modelo TimelineData; todo lo demas (ej.
# imagen_credito) vive SOLO aqui y se adjunta en el API, para no
# requerir migraciones en bases existentes.
COLUMNAS_MODELO = (
    "anio",
    "titulo",
    "artista",
    "descripcion",
    "trivia",
    "imagen_url",
    "audio_url",
    "spotify_album_id",
)


def filtrar_columnas(datos):
    return {k: v for k, v in datos.items() if k in COLUMNAS_MODELO}


_CREDITO_TRESCUBANO = "Foto: Claireislovely · Dominio público (Wikimedia Commons)"
_CREDITO_FANIA_LAVOE = "Foto: Fania Records · Dominio público (foto publicitaria)"
_CREDITO_NICHE = "Foto: Tefita228 · CC BY-SA 4.0 (Wikimedia Commons)"
_CREDITO_EDDIE_SANTIAGO = "Foto: Eddie Santiago · Dominio público (Wikimedia Commons)"

_EVENTOS = [
    dict(
        anio="1900-1940",
        titulo="El Son Cubano",
        descripcion=(
            "Fusión de ritmos africanos y españoles en el oriente de Cuba "
            "que sentó las bases rítmicas de lo que siglos después el mundo "
            "bailaría como salsa."
        ),
        trivia=(
            "El son nació en las zonas rurales del oriente cubano antes de "
            "tomar los salones de La Habana."
        ),
        imagen_url=(
            "https://commons.wikimedia.org/wiki/Special:FilePath/"
            "Trescubano.jpg?width=800"
        ),
        imagen_credito=_CREDITO_TRESCUBANO,
        audio_url="https://www.youtube-nocookie.com/embed/tGbRZ73NvlY",
    ),
    dict(
        anio="1964",
        titulo="Nace Fania Records",
        artista="Jerry Masucci y Johnny Pacheco",
        descripcion=(
            "La fundación del sello que masificó la salsa: catálogo, estrellas "
            "y una identidad musical para toda una generación latina."
        ),
        trivia=(
            "Pacheco vendía los primeros discos de Fania directamente desde "
            "la cajuela de su auto."
        ),
        imagen_url=(
            "https://commons.wikimedia.org/wiki/Special:FilePath/"
            "H%C3%A9ctor%20Lavoe%20(1969%20Fania%20Records%20publicity%20photo).jpg"
            "?width=800"
        ),
        imagen_credito=_CREDITO_FANIA_LAVOE,
    ),
    dict(
        anio="1965-1968",
        titulo="El Boogaloo: puente entre el mambo y la salsa",
        artista="Joe Cuba, Pete Rodriguez, Joe Bataan",
        descripcion=(
            "Fusión de son montuno con R&B y soul que explotó en los barrios "
            "latinos de Nueva York. 'Bang Bang' de Joe Cuba (1966) fue su "
            "himno; el movimiento abrió el camino para lo que sería la salsa."
        ),
        trivia=(
            "El Palladium Ballroom cerró en 1966 y el boogaloo llenó el "
            "vacío: los jóvenes nuyorricans crearon su propia música "
            "mezclando lo que sonaba en la radio con sus raíces caribeñas."
        ),
    ),
    dict(
        anio="1967",
        titulo="El Malo",
        artista="Willie Colón con Héctor Lavoe",
        descripcion=(
            "Álbum debut de Willie Colón, grabado a los 17 años, con un joven "
            "Héctor Lavoe de 21: nace el sonido 'duro' de la salsa neoyorquina."
        ),
        trivia=(
            "Fue la primera colaboración entre Colón y Lavoe, una de las "
            "duplas más influyentes de la historia del género."
        ),
        spotify_album_id="6ROTUtQlp130rdHDff3nhE",
    ),
    dict(
        anio="1971",
        titulo="Fania All-Stars en el Cheetah Club",
        artista="Fania All-Stars",
        descripcion=(
            "El 26 de agosto de 1971, la Fania All-Stars tocó en el Cheetah "
            "de Manhattan frente a 2.000 personas: Willie Colón, Ray Barretto, "
            "Larry Harlow, Héctor Lavoe y Cheo Feliciano definieron el 'sonido "
            "Fania'. El concierto se filmó como 'Our Latin Thing'."
        ),
        trivia=(
            "El productor Jerry Masucci lo concibió como el 'Woodstock "
            "Latino': una sola noche para que el mundo escuchara la salsa "
            "como movimiento unificado."
        ),
    ),
    dict(
        anio="1974",
        titulo="Celia & Johnny",
        artista="Celia Cruz y Johnny Pacheco",
        descripcion=(
            "Consagró a Celia Cruz como reina de la salsa tras su exilio de "
            "Cuba, con 'Quimbara' como himno."
        ),
        trivia=(
            "En 2014 la Biblioteca del Congreso de EE. UU. lo declaró de "
            "importancia histórica y cultural."
        ),
        spotify_album_id="416lPCtckkTOPYQslZ6QH1",
    ),
    dict(
        anio="1974",
        titulo="Celia Cruz y la Fania All-Stars en Zaire",
        artista="Celia Cruz · Fania All-Stars",
        descripcion=(
            "En el festival previo a la pelea Ali-Foreman, la Fania All-Stars "
            "tocó frente a decenas de miles de personas en Kinshasa: la salsa "
            "quedaba grabada para siempre en África."
        ),
        trivia=(
            "Fue el famoso '¡Azúcar!' proyectado ante el público africano; "
            "el concierto se recuperó en los documentales 'Soul Power' y "
            "'Live in Africa'."
        ),
        audio_url="https://www.youtube-nocookie.com/embed/-SJfoBFjdnQ",
    ),
    dict(
        anio="1975",
        titulo="Live At Yankee Stadium, Vol. 1",
        artista="Fania All-Stars",
        descripcion=(
            "Registro en vivo de uno de los conciertos más grandes que ha "
            "tenido la salsa como movimiento masivo."
        ),
        trivia=(
            "Grabado en el legendario estadio de béisbol de Nueva York, con "
            "'Mi Gente' entre sus temas centrales."
        ),
        spotify_album_id="2W5VinmurxO8g1QgKN5j4P",
    ),
    dict(
        anio="1977",
        titulo="Metiendo Mano!",
        artista="Willie Colón y Rubén Blades",
        descripcion=(
            "Primer álbum de la dupla Colón-Blades, un año antes de 'Siembra'."
        ),
        trivia=(
            "'Pablo Pueblo' es considerado uno de los primeros pasos hacia "
            "la salsa 'consciente', con letras de crítica social."
        ),
        spotify_album_id="4aagt0vBz9fm14XaYzlOdL",
    ),
    dict(
        anio="1978",
        titulo="Siembra",
        artista="Willie Colón y Rubén Blades",
        descripcion=(
            "El álbum de salsa más vendido de la historia, con más de "
            "3 millones de copias."
        ),
        trivia=(
            "'Pedro Navaja' está inspirado en 'Mack the Knife' de Brecht; el "
            "sello no quería incluirlo por ser 'muy largo'."
        ),
        spotify_album_id="7wOJ9RTQr05ytqROWtTPzy",
    ),
    dict(
        anio="1981",
        titulo="Grupo Niche: la salsa caleña toma fuerza",
        artista="Grupo Niche (dir. Jairo Varela)",
        descripcion=(
            "Jairo Varela consolida al Grupo Niche en Colombia y convierte a "
            "Cali en referente mundial de la salsa."
        ),
        trivia=(
            "Varela componía tarareando sus arreglos completos sin tocar "
            "instrumentos armónicos."
        ),
        imagen_url=(
            "https://commons.wikimedia.org/wiki/Special:FilePath/"
            "Feria%20de%20Cali%20Grupo%20Niche%20WV%2001.jpg?width=800"
        ),
        audio_url="https://www.youtube-nocookie.com/embed/7KxkMLAZlzw",
        imagen_credito=_CREDITO_NICHE,
    ),
    dict(
        anio="1982-1986",
        titulo="La salsa romántica llega para quedarse",
        artista="Eddie Santiago, Frankie Ruiz, Louie Ramírez",
        descripcion=(
            "La salsa se suaviza con baladas y letras de amor. 'Noche "
            "Caliente' (1982) de Louie Ramírez abrió la puerta; Eddie "
            "Santiago ('Tú Me Quemas', 1986) y Frankie Ruiz ('Solista pero "
            "no solo', 1985) la consolidaron como fenómeno comercial."
        ),
        trivia=(
            "Eddie Santiago fue despedido de un grupo anterior porque su "
            "forma de cantar era 'muy suave'. Ese estilo suave se convirtió "
            "en el sonido dominante de la salsa en los años 80."
        ),
        imagen_url=(
            "https://commons.wikimedia.org/wiki/Special:FilePath/"
            "Eddie_santiago_2_(cropped).png?width=800"
        ),
        imagen_credito=_CREDITO_EDDIE_SANTIAGO,
    ),
    dict(
        anio="1970s-1990s",
        titulo="Medellín, capital salsera de Colombia",
        artista="Fruko y sus Tesos, The Latin Brothers, Grupo Galé",
        descripcion=(
            "Desde los años 70, Medellín consolidó una escena salsera "
            "propia con emisoras, coleccionistas y bailarines. La Feria de "
            "las Flores se convirtió en escenario clave del género, y la "
            "ciudad es reconocida como epicentro salsero de Colombia."
        ),
        trivia=(
            "Fruko y sus Tesos, fundados en Medellño en 1970, son una de "
            "las orquestas más longevas de América Latina: más de 50 años "
            "de trayectoria ininterrumpida."
        ),
    ),
    dict(
        anio="1990",
        titulo="Orquesta de la Luz: la salsa conquista Japón",
        artista="Orquesta de la Luz (Nora Suzuki)",
        descripcion=(
            "La banda japonesa debutó con 'Salsa Caliente Del Japón' en "
            "1990, que pasó 12 semanas en el #1 del Billboard Latin Chart. "
            "Probó que la salsa no tiene fronteras geográficas ni lingüísticas."
        ),
        trivia=(
            "A pesar de cantar en español con comprensión limitada del "
            "idioma, la banda embodiment el espíritu de la salsa. En 1993 "
            "recibieron el Premio de Paz de las Naciones Unidas."
        ),
    ),
    dict(
        anio="1995",
        titulo="La explosión de la timba: Los Van Van",
        artista="Juan Formell y Los Van Van",
        descripcion=(
            "Juan Formell y Los Van Van llevan la timba cubana a su punto "
            "álgido, modernizando la charanga tradicional."
        ),
        trivia=(
            "Formell creó el ritmo 'songo' fusionando sintetizadores con la "
            "percusión afrocubana."
        ),
        audio_url="https://www.youtube-nocookie.com/embed/zhvMhzJ4tEk",
    ),
    dict(
        anio="1996-Actualidad",
        titulo="Salsa global: congresos, competencias y baile competitivo",
        descripcion=(
            "El World Salsa Championships (1996) estableció formatos de "
            "competencia estándar. Hoy la salsa genera ~2.3 mil millones de "
            "streams anuales en Spotify, con congresos en todo el mundo: "
            "Japón, Corea, Europa, África. El baile se profesionalizó "
            "como deporte internacional."
        ),
        trivia=(
            "Solo en Seoul, Corea del Sur, había más de 200 academias de "
            "salsa para 2005. Rusia ha producido parejas campeonas mundiales "
            "de salsa competitiva."
        ),
    ),
]

EVENTOS_TIMELINE = _EVENTOS


def credito_por_titulo(titulo):
    """Crédito de foto declarado aqui (fuente unica), asociable a las
    filas ya existentes en BD sin tocar el esquema."""
    for e in _EVENTOS:
        if e.get("titulo") == titulo:
            return e.get("imagen_credito")
    return None

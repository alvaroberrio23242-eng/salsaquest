# app/models/content_data.py
"""
Contenido estático (no depende de la base de datos) para las nuevas
secciones de SalsaQuest: grandes eventos de la salsa, récords/hitos,
biografías de artistas/ritmos clave, y la sección de Timba.

Se sirve vía app/routes/content.py como JSON, igual que timeline.py
sirve TimelineData. Se deja como diccionarios en Python (no en la BD)
para poder editarlo rápido sin migraciones mientras el contenido
todavía se está afinando.
"""

GRANDES_EVENTOS = [
    {
        "id": "cheetah-club-1971",
        "anio": "1971",
        "titulo": "Fania All-Stars en el Cheetah Club",
        "lugar": "Nueva York, EE. UU.",
        "descripcion": (
            "El concierto que quedó inmortalizado en el documental "
            "'Our Latin Thing' (Nuestra Cosa Latina), considerado el "
            "momento fundacional que le dio visibilidad masiva a la "
            "Salsa como movimiento."
        ),
        "imagen_url": "https://images.unsplash.com/photo-1465847899084-d164df4dedc6?w=600",
    },
    {
        "id": "yankee-stadium-1973",
        "anio": "1973",
        "titulo": "Fania All-Stars en el Yankee Stadium",
        "lugar": "Nueva York, EE. UU.",
        "descripcion": (
            "Un estadio repleto de salseros llevó el concierto a un "
            "final abrupto cuando el público invadió el campo, "
            "demostrando el poder de convocatoria que ya tenía la Salsa."
        ),
        "imagen_url": "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600",
    },
    {
        "id": "feria-cali",
        "anio": "Anual desde 1957",
        "titulo": "Feria de Cali",
        "lugar": "Cali, Colombia",
        "descripcion": (
            "La feria que consolidó a Cali como la 'Capital Mundial de "
            "la Salsa', con desfiles, orquestas en vivo y el Salsódromo, "
            "uno de los desfiles bailados más grandes del mundo."
        ),
        "imagen_url": "https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?w=600",
    },
    {
        "id": "world-salsa-congress-2001",
        "anio": "2001",
        "titulo": "Primer World Salsa Congress",
        "lugar": "Puerto Rico",
        "descripcion": (
            "El primer congreso mundial dedicado exclusivamente al "
            "baile y la cultura de la salsa, que desde entonces se "
            "replicó en ciudades de todo el mundo."
        ),
        "imagen_url": "https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=600",
    },
]

RECORDS_SALSA = [
    {
        "id": "guinness-cali-2015",
        "titulo": "Récord Guinness de baile masivo",
        "dato": "Más de 850 bailarines simultáneos",
        "anio": "2015",
        "descripcion": (
            "Cali, Colombia, obtuvo el récord Guinness a la clase de "
            "salsa más grande del mundo, con cientos de bailarines "
            "sincronizados en una sola coreografía."
        ),
    },
    {
        "id": "siembra-mas-vendido",
        "titulo": "Álbum de salsa más vendido de la historia",
        "dato": "'Siembra' — Willie Colón & Rubén Blades (1978)",
        "anio": "1978",
        "descripcion": (
            "Sigue siendo, décadas después, el álbum de salsa más "
            "vendido, con clásicos como 'Pedro Navaja' y 'Plástico'."
        ),
    },
    {
        "id": "primer-grammy-salsa",
        "titulo": "Primer Grammy a Mejor Álbum de Salsa",
        "dato": "Categoría creada en 1993",
        "anio": "1993",
        "descripcion": (
            "La Academia de la Grabación reconoció formalmente a la "
            "salsa con su propia categoría en los Grammy, tras años de "
            "presión de artistas y sellos discográficos latinos."
        ),
    },
]

ARTISTAS = [
    {
        "slug": "la-lupe",
        "nombre": "La Lupe",
        "tipo": "artista",
        "resumen": "La 'Reina del Soul Latino', voz cruda y teatral que rompió moldes.",
        "texto": (
            "Lupe Victoria Yolí Raymond, conocida como La Lupe, nació en Santiago "
            "de Cuba y se convirtió en una de las voces más viscerales de la música "
            "latina. Su estilo, cargado de gritos, llanto en escena y una entrega "
            "física poco convencional para la época, la hizo tan polémica como "
            "admirada. Trabajó con Tito Puente en Nueva York durante los años "
            "sesenta antes de firmar con Fania Records, donde grabó como solista. "
            "Hoy se le reconoce como una precursora del soul latino y una influencia "
            "directa en generaciones de soneras."
        ),
        "imagen_url": "https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=600",
    },
    {
        "slug": "guaguanco",
        "nombre": "El Guaguancó",
        "tipo": "ritmo",
        "resumen": "El estilo de rumba cubana que sentó las bases rítmicas de la salsa.",
        "texto": (
            "El guaguancó es uno de los tres estilos clásicos de la rumba cubana "
            "(junto al yambú y la columbia), nacido en los barrios afrocubanos de "
            "La Habana y Matanzas a finales del siglo XIX. Se caracteriza por la "
            "'vacunao', un juego de cortejo escénico entre el bailador y la "
            "bailadora, y por el uso de tumbadoras, claves y cajones. Su "
            "estructura rítmica y su función social —música de barrio, de solar, "
            "de conversación entre percusión y voz— influyó directamente en la "
            "forma en que después se construyeron los arreglos de salsa."
        ),
        "imagen_url": "https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=600",
    },
    {
        "slug": "fruko",
        "nombre": "Fruko",
        "tipo": "artista",
        "resumen": "El padre de la salsa colombiana, motor de Discos Fuentes.",
        "texto": (
            "Julio Ernesto Estrada Rincón, 'Fruko', empezó como bajista "
            "adolescente en Discos Fuentes, el sello discográfico más importante "
            "de Colombia, y terminó convertido en productor, arreglista y "
            "director de orquesta. Con Fruko y sus Tesos popularizó un sonido "
            "salsero propiamente colombiano, con influencia del son cubano y la "
            "guaracha, pero con acentos locales. Su trabajo como productor "
            "también fue clave para lanzar a otras agrupaciones del sello, "
            "consolidando a Medellín y la Costa Caribe colombiana como polos "
            "de producción salsera."
        ),
        "imagen_url": "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=600",
    },
    {
        "slug": "afrosound",
        "nombre": "Afrosound",
        "tipo": "artista",
        "resumen": "La fusión afro-tropical de Discos Fuentes que traspasó fronteras.",
        "texto": (
            "También surgida de Discos Fuentes, Afrosound mezcló ritmos "
            "afrocolombianos y caribeños —cumbia, salsa, música africana— en un "
            "sonido experimental y bailable para su época. Canciones como "
            "'El Alacrán' se volvieron himnos que trascendieron Colombia y "
            "circularon por radios de toda América Latina y África Occidental, "
            "donde la música de Discos Fuentes tuvo una recepción sorprendente "
            "y duradera."
        ),
        "imagen_url": "https://images.unsplash.com/photo-1509824227185-9c5a01ceba0d?w=600",
    },
    {
        "slug": "gilberto-santa-rosa",
        "nombre": "Gilberto Santa Rosa",
        "tipo": "artista",
        "resumen": "'El Caballero de la Salsa', de corista a figura central del género.",
        "texto": (
            "El puertorriqueño Gilberto Santa Rosa inició su carrera a finales "
            "de los años setenta como corista y cantante de orquestas "
            "establecidas de la escena salsera de Puerto Rico, un camino típico "
            "para los soneros de su generación antes de dar el salto como "
            "solista. Con el tiempo desarrolló un estilo elegante y técnicamente "
            "impecable que lo distanció del sonido más crudo de la salsa "
            "callejera de los setenta, ganándose el apodo de 'El Caballero de "
            "la Salsa' y una carrera con múltiples premios Grammy Latino."
        ),
        "imagen_url": "https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=600",
    },
    {
        "slug": "willie-colon",
        "nombre": "Willie Colón",
        "tipo": "artista",
        "resumen": "Trombonista, compositor y una de las mentes detrás de Fania.",
        "texto": (
            "Nacido en el Bronx de padres puertorriqueños, Willie Colón fue uno "
            "de los artistas más prolíficos del sello Fania desde finales de los "
            "sesenta, primero junto a Héctor Lavoe y luego con Rubén Blades como "
            "cantantes de su orquesta. Como compositor y productor, sus arreglos "
            "—con el trombón como protagonista en lugar de la trompeta— "
            "definieron buena parte del sonido 'duro' de la salsa neoyorquina. "
            "Más adelante también incursionó en la política y el activismo "
            "comunitario en Nueva York."
        ),
        "imagen_url": "https://images.unsplash.com/photo-1465847899084-d164df4dedc6?w=600",
    },
    {
        "slug": "ruben-blades",
        "nombre": "Rubén Blades",
        "tipo": "artista",
        "resumen": "Cantautor, abogado y figura política panameña.",
        "texto": (
            "Rubén Blades es quizás el caso más singular de la salsa: cantante "
            "y compositor de letras con conciencia social y narrativa (como "
            "'Pedro Navaja' o 'Plástico', junto a Willie Colón), pero también "
            "abogado graduado de Harvard y una figura política activa en Panamá. "
            "Fundó el movimiento Papá Egoró y fue candidato presidencial en "
            "1994, y entre 2004 y 2009 se desempeñó como Ministro de Turismo de "
            "su país. Sus orígenes como escritor de canciones estuvieron "
            "marcados desde joven por el interés en contar historias urbanas y "
            "políticas a través de la música."
        ),
        "imagen_url": "https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=600",
    },
    {
        "slug": "oscar-de-leon",
        "nombre": "Oscar D'León",
        "tipo": "artista",
        "resumen": "'El Sonero del Mundo', el venezolano que conquistó a Cuba.",
        "texto": (
            "Oscar D'León empezó como bajista y cantante en orquestas de Caracas "
            "antes de formar su propia agrupación y convertirse en una de las "
            "voces más reconocibles de la salsa. Su fraseo y su forma de "
            "improvisar soneos —tan fiel al estilo cubano que en su primera "
            "visita a Cuba en 1983 el público local lo aclamó como si fuera uno "
            "de los suyos— le valieron el apodo de 'El Sonero del Mundo' y del "
            "'León de la Salsa'."
        ),
        "imagen_url": "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=600",
    },
]

TIMBA = {
    "historia": (
        "La timba nació en Cuba a finales de los años ochenta y se consolidó "
        "en los noventa como una evolución del son y la salsa cubana, "
        "mezclada con funk, jazz y ritmos afrocubanos como el guaguancó y el "
        "songo. Se le considera más agresiva, virtuosa y rítmicamente compleja "
        "que la salsa tradicional, con arreglos de metales elaborados y letras "
        "que retratan directamente la vida cotidiana cubana del llamado "
        "'Período Especial'. La orquesta NG La Banda, liderada por José Luis "
        "'El Tosco' Cortés, es considerada la pionera y fundadora del "
        "movimiento en 1988, seguida por agrupaciones como Los Van Van y la "
        "Charanga Habanera, que llevaron el género a audiencias internacionales."
    ),
    "records": [
        {
            "titulo": "Nacimiento oficial del género",
            "dato": "NG La Banda, fundada en 1988",
            "descripcion": "Considerada el punto de partida formal de la timba como movimiento diferenciado de la salsa.",
        },
        {
            "titulo": "Grammy para Los Van Van",
            "dato": "1999 — Mejor Álbum de Salsa",
            "descripcion": "'Van Van is Here' les dio el primer Grammy a una orquesta de timba cubana.",
        },
    ],
    "playlists": [
        {
            "titulo": "Lo mejor de la Timba Cubana",
            "descripcion": "Búsqueda curada en Spotify con los grandes clásicos del género.",
            "url": "https://open.spotify.com/search/timba%20cubana",
        },
        {
            "titulo": "NG La Banda, Los Van Van y Charanga Habanera",
            "descripcion": "Búsqueda directa por las orquestas fundadoras del movimiento.",
            "url": "https://open.spotify.com/search/NG%20La%20Banda%20Los%20Van%20Van%20Charanga%20Habanera",
        },
    ],
}

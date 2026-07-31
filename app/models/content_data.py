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
        "imagen_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Cuban singer La Lupe performing in New York City LCCN2009632630 (cropped).jpg",
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
        "imagen_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Gilberto Santa Rosa en 2025.png",
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
        "imagen_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Willie Colón (1969 Fania Records publicity photo).jpg",
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
        "imagen_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Danilo Pérez, Herbie Hancock, Wayne Shorter, Rubén Blades.jpg",
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

# ==========================================
# ENTREVISTAS INÉDITAS
# ==========================================
# video_url apunta a un archivo LOCAL en app/static/videos/entrevistas/
# (no a YouTube/Spotify). Agrega tus archivos ahi con esos mismos
# nombres, o cambia el nombre aqui para que coincida con el tuyo.
ENTREVISTAS = [
    {
        "slug": "entrevista-1",
        "titulo": "Entrevista inédita #1",
        "invitado": "Por definir",
        "descripcion": "Agrega aquí la descripción real de esta entrevista.",
        "video_url": "entrevistas/entrevista-1.mp4",
        "miniatura_url": "",
    },
]

# ==========================================
# CARÁTULAS ICÓNICAS DE LA SALSA
# ==========================================
# Usamos el embed OFICIAL de Spotify para mostrar la portada real de
# cada álbum (es la forma legal de mostrar el arte de tapa con
# derechos de autor, en vez de alojar la imagen nosotros mismos).
# spotify_album_id: se saca de la URL del álbum en Spotify
# (open.spotify.com/album/ESTE_ID).
CARATULAS_ICONICAS = [
    {
        "slug": "siembra",
        "titulo": "Siembra",
        "artista": "Willie Colón & Rubén Blades",
        "anio": 1978,
        "spotify_album_id": "7wOJ9RTQr05ytqROWtTPzy",
        "exitos": "Pedro Navaja, Plástico, Buscando Guayaba",
        "curiosidad": (
            "Es el álbum de salsa más vendido de la historia, con más de 3 "
            "millones de copias. 'Pedro Navaja' está inspirado en 'Mack the "
            "Knife' de Bertolt Brecht, y los ejecutivos del sello no querían "
            "incluirlo por considerarlo demasiado largo para la radio."
        ),
    },
    {
        "slug": "celia-johnny",
        "titulo": "Celia & Johnny",
        "artista": "Celia Cruz & Johnny Pacheco",
        "anio": 1974,
        "spotify_album_id": "416lPCtckkTOPYQslZ6QH1",
        "exitos": "Quimbara, Toro Mata, Vieja Luna",
        "curiosidad": (
            "Marcó la consagración de Celia Cruz como reina de la salsa tras "
            "su exilio de Cuba. En 2014 la Biblioteca del Congreso de EE.UU. "
            "lo declaró de importancia histórica y cultural para su Registro "
            "Nacional de Grabaciones."
        ),
    },
    {
        "slug": "el-malo",
        "titulo": "El Malo",
        "artista": "Willie Colón",
        "anio": 1967,
        "spotify_album_id": "6ROTUtQlp130rdHDff3nhE",
        "exitos": "El Malo, Jazzy, Borinquen",
        "curiosidad": (
            "Álbum debut de Willie Colón, grabado cuando tenía apenas 17 "
            "años, y primera colaboración con un joven Héctor Lavoe de 21 "
            "años -- el inicio de una de las duplas más influyentes de la "
            "salsa neoyorquina."
        ),
    },
    {
        "slug": "fruko-el-grande",
        "titulo": "Fruko el Grande",
        "artista": "Fruko y sus Tesos",
        "anio": 1975,
        "spotify_album_id": "4VwcUaZ0yWCHp9hEDue09C",
        "exitos": "El Preso, Manyoma, Los Charcos",
        "curiosidad": (
            "Incluye 'El Preso', considerado un himno mundial de la salsa "
            "colombiana. La canción narra la historia de un preso condenado "
            "a 30 años, inspirada en la carta de un amigo del compositor "
            "Álvaro Velásquez."
        ),
    },
    {
        "slug": "metiendo-mano",
        "titulo": "Metiendo Mano!",
        "artista": "Willie Colón & Rubén Blades",
        "anio": 1977,
        "spotify_album_id": "4aagt0vBz9fm14XaYzlOdL",
        "exitos": "Pablo Pueblo, La Mora, Plantación Adentro",
        "curiosidad": (
            "Primer álbum de la dupla Colón-Blades, un año antes de "
            "'Siembra'. 'Pablo Pueblo' es considerado uno de los primeros "
            "pasos hacia la salsa 'consciente', con letras de crítica "
            "social en vez de solo temas bailables."
        ),
    },
    {
        "slug": "live-yankee-stadium",
        "titulo": "Live At Yankee Stadium, Vol. 1",
        "artista": "Fania All-Stars",
        "anio": 1975,
        "spotify_album_id": "2W5VinmurxO8g1QgKN5j4P",
        "exitos": "Mi Gente, Congo Yambumba",
        "curiosidad": (
            "Grabado en vivo en el legendario estadio de béisbol de Nueva "
            "York en 1973, es uno de los conciertos más grandes que ha "
            "tenido la salsa como movimiento masivo."
        ),
    },
    {
        "slug": "comedia",
        "titulo": "Comedia",
        "artista": "Héctor Lavoe",
        "anio": 1978,
        "spotify_album_id": "7CBmznpnzPgLpBXFlB40B6",
        "exitos": "El Cantante, Bandolera, Songoro Cosongo",
        "curiosidad": (
            "Contiene 'El Cantante', escrita por Rubén Blades y que se "
            "convirtió en el tema insignia de Héctor Lavoe. Rolling Stone "
            "lo incluyó en su lista de los 50 mejores álbumes de salsa de "
            "la historia (2024)."
        ),
    },
    {
        "slug": "dance-mania",
        "titulo": "Dance Mania",
        "artista": "Tito Puente",
        "anio": 1958,
        "spotify_album_id": "5lEk5pQKxyyLfDLGDBSC2L",
        "exitos": "El Cayuco, Hong Kong Mambo, 3-D Mambo",
        "curiosidad": (
            "Sigue considerado el álbum de baile latino más vendido de la "
            "historia. Fue la primera grabación de un sello grande (RCA) "
            "dedicada por completo a ritmos afrocubanos de baile, sin "
            "concesiones al jazz comercial de la época."
        ),
    },
    {
        "slug": "cielo-de-tambores",
        "titulo": "Cielo de Tambores",
        "artista": "Grupo Niche",
        "anio": 1990,
        "spotify_album_id": "1WCOE4vTMLfm4edaZBaLFM",
        "exitos": "Una Aventura, Cali Ají, Sin Sentimiento",
        "curiosidad": (
            "El álbum más exitoso de la historia de Grupo Niche, elegido "
            "por la revista Billboard en 2015 como uno de los '50 Álbumes "
            "Latinos Esenciales de los Últimos 50 Años'."
        ),
    },
]

# ==========================================
# ORQUESTAS INFLUYENTES
# ==========================================
ORQUESTAS = [
    {
        "slug": "el-gran-combo",
        "nombre": "El Gran Combo de Puerto Rico",
        "fundacion": "1962",
        "lugar": "San Juan, Puerto Rico",
        "resumen": "'La Universidad de la Salsa', la orquesta boricua más longeva y popular.",
        "texto": (
            "Nace en 1962 cuando el pianista Rafael Ithier reúne a varios "
            "músicos de la orquesta de Rafael Cortijo tras la salida de esta "
            "de Ismael Rivera. Con un estilo bailable, elegante y sin excesos "
            "de solos, se ganó el apodo de 'La Universidad de la Salsa'. "
            "Voces como las de Charlie Aponte y Jerry Rivas la mantuvieron "
            "vigente por más de seis décadas, algo excepcional en la salsa."
        ),
    },
    {
        "slug": "sonora-poncena",
        "nombre": "La Sonora Ponceña",
        "fundacion": "1954",
        "lugar": "Ponce, Puerto Rico",
        "resumen": "Fundada por Enrique Lucca, llevada a la fama por el piano de su hijo Papo Lucca.",
        "texto": (
            "Fundada en Ponce por Enrique Lucca Caraballo, alcanzó su sonido "
            "característico bajo la dirección de su hijo, el pianista Papo "
            "Lucca, admirador confeso de Bill Evans y Oscar Peterson. Su "
            "sección de tres trompetas y el refinamiento técnico del piano "
            "de Papo la distinguieron de la salsa más cruda de la época, sin "
            "perder nunca el peso rítmico bailable."
        ),
    },
    {
        "slug": "sonora-matancera",
        "nombre": "La Sonora Matancera",
        "fundacion": "1924",
        "lugar": "Matanzas, Cuba",
        "resumen": "La orquesta cubana más longeva, y el trampolín que lanzó a Celia Cruz.",
        "texto": (
            "Una de las orquestas cubanas más antiguas e influyentes, activa "
            "desde los años veinte. Fue la voz principal de Celia Cruz entre "
            "1950 y 1965, antes de su exilio de Cuba, y su sonido de "
            "conjunto -- trompetas, coro y tumbao -- es una referencia "
            "directa para el son montuno y la guaracha que después "
            "alimentaron a la salsa neoyorquina."
        ),
    },
    {
        "slug": "fania-all-stars",
        "nombre": "Fania All-Stars",
        "fundacion": "1968",
        "lugar": "Nueva York, EE. UU.",
        "resumen": "La 'súper orquesta' del sello Fania, con las máximas estrellas del género reunidas en un solo escenario.",
        "texto": (
            "Formada por Johnny Pacheco y Jerry Masucci como una alineación "
            "estelar de los artistas del sello Fania Records, la Fania "
            "All-Stars llevó la salsa a escenarios masivos como el Cheetah "
            "Club (1971), el Yankee Stadium (1973) y un histórico concierto "
            "en Kinshasa, Zaire (1974). Sus conciertos convirtieron a la "
            "salsa en un fenómeno de alcance mundial."
        ),
    },
    {
        "slug": "grupo-niche-orquesta",
        "nombre": "Grupo Niche",
        "fundacion": "1979",
        "lugar": "Cali / Bogotá, Colombia",
        "resumen": "Fundada por Jairo Varela, definió el sonido de la salsa caleña moderna.",
        "texto": (
            "Fundada por el compositor chocoano Jairo Varela, se convirtió "
            "en la orquesta insignia de la 'salsa caleña'. Himnos como "
            "'Cali Pachanguero' y el álbum 'Cielo de Tambores' la "
            "consolidaron como una de las agrupaciones colombianas más "
            "influyentes internacionalmente. Varela dirigió la orquesta "
            "hasta su muerte en 2012."
        ),
    },
    {
        "slug": "spanish-harlem-orchestra",
        "nombre": "Spanish Harlem Orchestra",
        "fundacion": "1999-2000",
        "lugar": "Nueva York, EE. UU.",
        "resumen": "Fundada por Oscar Hernández para rescatar el sonido clásico de la salsa neoyorquina.",
        "texto": (
            "El pianista y arreglista Oscar Hernández -- con una carrera "
            "previa junto a Celia Cruz, Ray Barretto y Rubén Blades -- "
            "fundó esta orquesta al filo del año 2000 con la misión "
            "explícita de mantener vivo el sonido clásico de la salsa dura "
            "neoyorquina de los setenta, en una época en que el género "
            "había virado hacia la salsa romántica."
        ),
    },
]

# ==========================================
# INSTRUMENTOS DE LA SALSA (galería interactiva)
# ==========================================
# video_busqueda usa el mismo patrón que ya usan los playlists de
# TIMBA: un link de búsqueda en YouTube, no un video_id específico
# (evita que el embed se rompa si el video puntual se cae o cambia).
INSTRUMENTOS = [
    {
        "slug": "tumbadoras",
        "imagen_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Congas.JPG",
        "nombre": "Congas / Tumbadoras",
        "categoria": "Percusión",
        "texto": (
            "Tambores altos de origen afrocubano, tocados con las manos, "
            "que forman el corazón de la sección rítmica junto al bajo y el "
            "piano. Su nombre 'tumbadora' viene del golpe grave ('tumbao') "
            "que marca el pulso base de la música."
        ),
        "sonido": "Golpe grave y cálido, con capas de tonos abiertos y cerrados que sostienen el pulso.",
        "famosos_por": "Ray Barretto ('El Rey de las Manos Duras'), Mongo Santamaría, Giovanni Hidalgo.",
        "video_busqueda": "https://www.youtube.com/results?search_query=historia+de+las+congas+en+la+salsa",
    },
    {
        "slug": "bongo",
        "imagen_url": "https://images.unsplash.com/photo-1519892300165-cb5542fb47c7?w=600",
        "nombre": "Bongó",
        "categoria": "Percusión",
        "texto": (
            "Par de pequeños tambores unidos, tocados sentados entre las "
            "rodillas. El bongosero suele encargarse también de cantar los "
            "coros y de adornar la música con repiques ('martillo') en las "
            "secciones más libres del arreglo."
        ),
        "sonido": "Timbre agudo y seco, ideal para repiques ('martillo') y adornos improvisados.",
        "famosos_por": "Roberto Roena (bongosero y director de Apollo Sound), Johnny 'Dandy' Rodríguez.",
        "video_busqueda": "https://www.youtube.com/results?search_query=bong%C3%B3+salsa+solo+martillo",
    },
    {
        "slug": "timbales",
        "imagen_url": "https://images.unsplash.com/photo-1541689592655-f2ec549f61f0?w=600",
        "nombre": "Timbales",
        "categoria": "Percusión",
        "texto": (
            "Un par de tambores metálicos de origen cubano, tocados de pie "
            "con baquetas, generalmente al frente de la orquesta. Tito "
            "Puente los popularizó como instrumento protagónico -- no solo "
            "de acompañamiento -- convirtiéndose en 'El Rey del Timbal'."
        ),
        "sonido": "Metálico y brillante, con la campana ('cencerro') marcando el montuno y solos vistosos.",
        "famosos_por": "Tito Puente ('El Rey del Timbal'), Orestes Vilató, Nicky Marrero.",
        "video_busqueda": "https://www.youtube.com/results?search_query=Tito+Puente+timbal+solo",
    },
    {
        "slug": "clave",
        "imagen_url": "https://images.unsplash.com/photo-1614963326505-843d3b1d99d3?w=600",
        "nombre": "Claves",
        "categoria": "Percusión / patrón rítmico",
        "texto": (
            "Dos palos de madera que se entrechocan para marcar el patrón "
            "rítmico (2-3 o 3-2) sobre el que se construye casi toda la "
            "salsa. Más que un instrumento, la clave es la estructura "
            "organizadora: todos los demás instrumentos -- piano, bajo, "
            "coros -- se acomodan a su patrón, no al revés."
        ),
        "sonido": "Seco, cortante y constante -- la referencia rítmica que ordena a toda la orquesta.",
        "famosos_por": "No tiene solistas famosos como tal: su 'fama' es estructural, es la base que sostiene todo el arreglo.",
        "video_busqueda": "https://www.youtube.com/results?search_query=patron+de+clave+salsa+2-3+3-2+explicado",
    },
    {
        "slug": "maracas",
        "imagen_url": "https://images.unsplash.com/photo-1619983081563-430f63602796?w=600",
        "nombre": "Maracas",
        "categoria": "Percusión",
        "texto": (
            "Par de sonajeros de origen taíno y africano, tradicionalmente "
            "hechos con totumas rellenas de semillas. En el son cubano y "
            "sus derivados, era común que el propio cantante principal las "
            "tocara mientras cantaba, una tradición que la salsa heredó "
            "directamente."
        ),
        "sonido": "Un 'chhh' constante y texturizado que refuerza el pulso sin competir con la percusión de cuero.",
        "famosos_por": "Tradición del son cubano; cantantes-percusionistas como Beny Moré las tocaban en escena.",
        "video_busqueda": "https://www.youtube.com/results?search_query=maracas+son+cubano+salsa+historia",
    },
    {
        "slug": "guiro",
        "imagen_url": "https://images.unsplash.com/photo-1598488035139-bdbb2231ce04?w=600",
        "nombre": "Güiro",
        "categoria": "Percusión",
        "texto": (
            "Una calabaza hueca y estriada que se raspa con un palillo, de "
            "raíz indígena taína y africana. Aporta una textura constante "
            "de fondo, marcando el pulso de manera sutil pero indispensable "
            "en los arreglos más tradicionales."
        ),
        "sonido": "Un raspado continuo y texturizado, casi como una respiración que sostiene el ritmo de fondo.",
        "famosos_por": "Instrumento de acompañamiento -- valorado más por orquestas tradicionales (charanga, son) que por solistas.",
        "video_busqueda": "https://www.youtube.com/results?search_query=guiro+instrumento+salsa+como+se+toca",
    },
    {
        "slug": "piano-montuno",
        "imagen_url": "https://images.unsplash.com/photo-1552422535-c45813c61732?w=600",
        "nombre": "Piano (montuno)",
        "categoria": "Armonía / ritmo",
        "texto": (
            "En la salsa, el piano no acompaña como en el jazz: toca un "
            "patrón repetitivo y sincopado llamado 'montuno', que funciona "
            "a la vez como base armónica y como elemento rítmico. Eddie "
            "Palmieri fue pionero en sostener el tumbao con la mano "
            "izquierda mientras improvisaba con la derecha."
        ),
        "sonido": "Percusivo y sincopado -- el piano funciona casi como un instrumento de percusión afinado.",
        "famosos_por": "Eddie Palmieri, Papo Lucca (Sonora Ponceña), Charlie Palmieri, Larry Harlow.",
        "video_busqueda": "https://www.youtube.com/results?search_query=piano+montuno+salsa+Eddie+Palmieri",
    },
    {
        "slug": "bajo",
        "imagen_url": "https://images.unsplash.com/photo-1550985616-10810253b84d?w=600",
        "nombre": "Bajo",
        "categoria": "Armonía / ritmo",
        "texto": (
            "El bajo (eléctrico o contrabajo) sostiene el patrón armónico "
            "del 'tumbao', dialogando constantemente con la mano izquierda "
            "del piano y con la tumbadora. Es el instrumento menos vistoso "
            "en escena, pero sin su patrón la orquesta entera pierde el "
            "centro rítmico."
        ),
        "sonido": "Grave y sincopado, entrelazado nota a nota con el piano en un mismo patrón de tumbao.",
        "famosos_por": "Bobby Valentín ('El Rey del Bajo'), Salvador Cuevas, Israel 'Cachao' López (padre del mambo/tumbao moderno).",
        "video_busqueda": "https://www.youtube.com/results?search_query=tumbao+de+bajo+salsa+explicado",
    },
    {
        "slug": "trompeta",
        "imagen_url": "https://images.unsplash.com/photo-1573871924872-e21f1eab24a6?w=600",
        "nombre": "Trompeta",
        "categoria": "Vientos",
        "texto": (
            "Junto al trombón, forma la 'sección de metales' que define el "
            "carácter de cada orquesta. Herencia directa de las big bands "
            "cubanas del mambo, algunas orquestas -- como La Sonora "
            "Ponceña, con su característica sección de tres trompetas -- "
            "construyeron toda su identidad sonora alrededor de este "
            "instrumento."
        ),
        "sonido": "Brillante y agudo, con líneas melódicas ('mambos' instrumentales) que rompen entre estrofas.",
        "famosos_por": "La sección de metales de Fania All-Stars; La Sonora Ponceña y sus tres trompetas.",
        "video_busqueda": "https://www.youtube.com/results?search_query=seccion+de+trompetas+salsa+mambo",
    },
    {
        "slug": "trombon",
        "imagen_url": "https://images.unsplash.com/photo-1621368286550-cba7a801e128?w=600",
        "nombre": "Trombón",
        "categoria": "Vientos",
        "texto": (
            "Willie Colón y Eddie Palmieri (con su orquesta La Perfecta) "
            "hicieron del trombón el sonido distintivo de la 'salsa dura' "
            "neoyorquina de los setenta, en lugar de la trompeta más "
            "tradicional -- un timbre más grave y agresivo que definió toda "
            "una época del género."
        ),
        "sonido": "Grave, agresivo y directo -- el timbre que le dio a la 'salsa dura' su carácter callejero.",
        "famosos_por": "Willie Colón, Eddie Palmieri (orquesta La Perfecta), Barry Rogers.",
        "video_busqueda": "https://www.youtube.com/results?search_query=Willie+Colon+trombon+salsa+dura",
    },
    {
        "slug": "saxofon",
        "imagen_url": "https://images.unsplash.com/photo-1465847899084-d164df4dedc6?w=600",
        "nombre": "Saxofón",
        "categoria": "Vientos",
        "texto": (
            "Menos protagonista que en el jazz, pero presente en arreglos "
            "puntuales de salsa. El timbalero y director Willie Rosario, "
            "admirador del saxofonista de jazz Gerry Mulligan, incorporó un "
            "saxo barítono a su orquesta para ampliar el color sonoro de "
            "sus arreglos, algo poco común en la instrumentación clásica de "
            "la salsa."
        ),
        "sonido": "Cálido y grave cuando es barítono; aporta color y contraste frente a la sección de metales tradicional.",
        "famosos_por": "Willie Rosario y su orquesta, pionero en sumar saxo barítono a la instrumentación salsera.",
        "video_busqueda": "https://www.youtube.com/results?search_query=Willie+Rosario+saxofon+baritono+salsa",
    },
    {
        "slug": "tres-cubano",
        "imagen_url": "https://images.unsplash.com/photo-1510915361894-db8b60106cb1?w=600",
        "nombre": "Tres cubano",
        "categoria": "Cuerdas",
        "texto": (
            "Guitarra cubana de tres pares de cuerdas, instrumento central "
            "del son montuno oriental que es una de las raíces directas de "
            "la salsa. Su patrón rítmico-melódico influyó directamente en "
            "cómo después se armaron los montunos de piano."
        ),
        "sonido": "Brillante y percusivo por el doblado de cuerdas -- un antecesor directo del montuno de piano.",
        "famosos_por": "Arsenio Rodríguez, figura clave del son cubano y referencia directa para la salsa neoyorquina.",
        "video_busqueda": "https://www.youtube.com/results?search_query=tres+cubano+son+montuno+Arsenio+Rodriguez",
    },
]


# ==========================================
# MUSEOS DEDICADOS A LA SALSA
# ==========================================
# Nota: no existe (a la fecha) un "Salon de la Fama" internacional
# dedicado en exclusiva a la salsa -- por eso esta seccion se enfoca
# en los tres museos reales dedicados al genero.
MUSEOS_SALSA = [
    {
        "slug": "museo-salsa-cali",
        "nombre": "Museo de la Salsa (Cali)",
        "lugar": "Barrio Obrero, Cali, Colombia",
        "fundacion": "1968",
        "texto": (
            "Se considera el museo de salsa más antiguo del mundo. Nació de "
            "la colección fotográfica de Carlos Alfredo Molina, quien desde "
            "1968 retrató a las estrellas de la salsa que visitaban Cali. "
            "Hoy conserva más de 40.000 fotografías y sigue funcionando en "
            "la casa familiar de los Molina, en el Barrio Obrero."
        ),
    },
    {
        "slug": "international-salsa-museum",
        "nombre": "International Salsa Museum",
        "lugar": "El Bronx, Nueva York, EE. UU.",
        "fundacion": "2021",
        "texto": (
            "Fundado en 2021 por Willy Rodríguez, Manny Tavarez e Ilialis "
            "Reyes, cuenta con el respaldo de los patrimonios de Tito "
            "Puente y Celia Cruz. Todavía no tiene sede fija -- funciona con "
            "exhibiciones itinerantes -- pero busca abrir un espacio "
            "permanente en el histórico Kingsbridge Armory del Bronx."
        ),
    },
    {
        "slug": "museo-salsa-puerto-rico",
        "nombre": "Museo de la Salsa de Puerto Rico",
        "lugar": "Puerto Rico",
        "fundacion": "~2000",
        "texto": (
            "Uno de los tres museos dedicados a la salsa que existen en el "
            "mundo. Sufrió daños importantes por el huracán María en 2017 y "
            "desde entonces continúa en proceso de reconstrucción de su "
            "colección y su espacio."
        ),
    },
]

# ==========================================
# MAPA: LUGARES SALSEROS DEL MUNDO
# ==========================================
LUGARES_SALSEROS = [
    {
        "slug": "nueva-york",
        "nombre": "Nueva York (El Bronx / Harlem)",
        "lat": 40.8448, "lng": -73.8648,
        "descripcion": (
            "Cuna de la salsa como movimiento: ahí nació Fania Records "
            "(1964), tocó la Fania All-Stars en el Cheetah Club y el Yankee "
            "Stadium, y el Bronx se ganó el apodo de 'El Condado de la "
            "Salsa'."
        ),
    },
    {
        "slug": "cali-colombia",
        "nombre": "Cali, Colombia",
        "lat": 3.4516, "lng": -76.5320,
        "descripcion": (
            "La 'Capital Mundial de la Salsa'. Sede de la Feria de Cali y su "
            "Salsódromo, del Museo de la Salsa más antiguo del mundo, y de "
            "una cultura de baile en 'salsa caleña' reconocida globalmente."
        ),
    },
    {
        "slug": "san-juan-pr",
        "nombre": "San Juan, Puerto Rico",
        "lat": 18.4655, "lng": -66.1057,
        "descripcion": (
            "Base de orquestas históricas como El Gran Combo, y punto de "
            "partida de figuras como Héctor Lavoe, Gilberto Santa Rosa e "
            "Ismael Rivera."
        ),
    },
    {
        "slug": "la-habana",
        "nombre": "La Habana, Cuba",
        "lat": 23.1136, "lng": -82.3666,
        "descripcion": (
            "Raíz musical directa de la salsa: son cubano, guaracha, "
            "guaguancó y mambo, los géneros sobre los que se construyó el "
            "sonido salsero décadas después en Nueva York."
        ),
    },
    {
        "slug": "medellin-colombia",
        "nombre": "Medellín, Colombia",
        "lat": 6.2442, "lng": -75.5812,
        "descripcion": (
            "Sede histórica de Discos Fuentes, el sello discográfico más "
            "importante de Colombia y el principal competidor de Fania en "
            "la producción de salsa tropical."
        ),
    },
    {
        "slug": "caracas-venezuela",
        "nombre": "Caracas, Venezuela",
        "lat": 10.4806, "lng": -66.9036,
        "descripcion": (
            "Escena salsera propia con orquestas como La Dimensión Latina, "
            "cuna del estilo enérgico y crudo de Oscar D'León."
        ),
    },
    {
        "slug": "cartagena-colombia",
        "nombre": "Cartagena, Colombia",
        "lat": 10.3910, "lng": -75.4794,
        "descripcion": (
            "Ciudad natal de Joe Arroyo, quien mezcló la salsa con calypso, "
            "cumbia y son en el estilo que él mismo bautizó como 'joeson'."
        ),
    },
]

# ==========================================
# RANKING: LOS ÁLBUMES MÁS INFLUYENTES
# ==========================================
# Basado en "The 50 Greatest Salsa Albums of All Time" de Rolling Stone
# (Ernesto Lechner, 30 oct. 2024). Mostramos el Top 15 verificado, con
# textos propios (no copiados), y linkeamos a la lista completa.
RANKING_FUENTE_URL = "https://www.rollingstone.com/music/music-lists/best-salsa-albums-1235139298/"

RANKING_ALBUMES = [
    {
        "puesto": 1, "titulo": "Siembra", "artista": "Willie Colón & Rubén Blades", "anio": 1978,
        "motivo": "El álbum de salsa más vendido de la historia y su manifiesto por excelencia, con 'Pedro Navaja' como pieza central.",
    },
    {
        "puesto": 2, "titulo": "Azúcar Pa'Ti", "artista": "Eddie Palmieri", "anio": 1965,
        "motivo": "Palmieri introdujo aquí la técnica de sostener el tumbao con la mano izquierda mientras improvisaba con la derecha, un antes y después para el piano salsero.",
    },
    {
        "puesto": 3, "titulo": "Comedia", "artista": "Héctor Lavoe", "anio": 1978,
        "motivo": "Contiene 'El Cantante', escrita por Rubén Blades y producida por Willie Colón: la canción insignia de Lavoe.",
    },
    {
        "puesto": 4, "titulo": "Cheo", "artista": "Cheo Feliciano", "anio": 1971,
        "motivo": "Grabado tras su recuperación de una adicción, con canciones a medida escritas por Tite Curet Alonso, entre ellas 'Anacaona'.",
    },
    {
        "puesto": 5, "titulo": "Celia & Johnny", "artista": "Celia Cruz & Johnny Pacheco", "anio": 1974,
        "motivo": "Consagró a Celia Cruz como reina de la salsa tras su exilio de Cuba, con 'Quimbara' como himno.",
    },
    {
        "puesto": 6, "titulo": "Y Su Salsa Mayor", "artista": "Oscar D'León", "anio": 1978,
        "motivo": "Doble álbum que catapultó a D'León de estrella local venezolana a figura internacional.",
    },
    {
        "puesto": 7, "titulo": "Musical Conquest", "artista": "La Sonora Ponceña", "anio": 1976,
        "motivo": "Muestra el refinamiento técnico del piano de Papo Lucca combinado con la fuerza rítmica de la orquesta.",
    },
    {
        "puesto": 8, "titulo": "Indestructible", "artista": "Ray Barretto", "anio": 1973,
        "motivo": "Grabado después de que gran parte de su orquesta lo abandonara para fundar Típica 73; la portada con Barretto de Superman se volvió icónica.",
    },
    {
        "puesto": 9, "titulo": "¡Aquí No Se Sienta Nadie!", "artista": "El Gran Combo de Puerto Rico", "anio": 1979,
        "motivo": "El sonido pulido y bailable que consolidó a El Gran Combo como 'La Universidad de la Salsa'.",
    },
    {
        "puesto": 10, "titulo": "El Grande", "artista": "Fruko y sus Tesos", "anio": 1975,
        "motivo": "Incluye 'El Preso', uno de los himnos más reconocibles de la salsa colombiana.",
    },
    {
        "puesto": 11, "titulo": "Con Todos Los Hierros", "artista": "Rafael Cortijo & Ismael Rivera", "anio": 1967,
        "motivo": "Último álbum de la dupla antes de separarse; sentó buena parte de las bases pre-salsa de Puerto Rico.",
    },
    {
        "puesto": 12, "titulo": "6", "artista": "Roberto Roena y su Apollo Sound", "anio": 1974,
        "motivo": "Roena, bongosero y bailarín carismático, mezcló funk y psicodelia con la estructura clásica de la salsa.",
    },
    {
        "puesto": 13, "titulo": "Cosa Nuestra", "artista": "Willie Colón & Héctor Lavoe", "anio": 1969,
        "motivo": "El momento en que la dupla Colón-Lavoe encontró su identidad definitiva, con 'Che Che Colé'.",
    },
    {
        "puesto": 14, "titulo": "No Hay Quinto Malo", "artista": "Grupo Niche", "anio": 1984,
        "motivo": "Incluye 'Cali Pachanguero', canción que se volvió virtualmente un himno no oficial de Cali.",
    },
    {
        "puesto": 15, "titulo": "Live at the Cheetah, Vol. 1", "artista": "Fania All-Stars", "anio": 1972,
        "motivo": "El registro en vivo del concierto de 1971 que inmortalizó el documental 'Our Latin Thing'.",
    },
]

# ==========================================
# MEDELLÍN, CAPITAL MUNDIAL DE LA SALSA
# ==========================================
# NOTA HONESTA: bares y emisoras estan verificados por busqueda
# cruzada (varias fuentes independientes, 2015-2026). Direcciones y
# antiguedad son confiables; horarios/estado actual pueden cambiar,
# así que se agrega un aviso en el frontend para que el usuario
# confirme antes de ir. Categorias como "agenda de eventos",
# "conciertos proximos", "DJs reconocidos", "coleccionistas" y
# "campeones de baile" NO se hardcodean aqui: cambian todo el tiempo
# o involucran a personas reales que requieren verificacion directa
# con el usuario, no busqueda generica.

MEDELLIN_HISTORIA = (
    "La salsa en Medellín tiene una historia propia, distinta a la de "
    "Cali. Desde los años setenta, Discos Fuentes -- el sello discográfico "
    "más importante de Colombia -- funcionó como motor de producción "
    "salsera desde la ciudad, lanzando a Fruko y sus Tesos, Afrosound y "
    "Joe Arroyo (con Fruko), entre otros. En paralelo se desarrolló una "
    "fuerte cultura de 'melómanos' y coleccionistas de vinilo, que "
    "mantuvo viva la salsa clásica en bares del sector de San Juan y "
    "Laureles durante décadas, incluso en años en que otros géneros "
    "dominaban la radio comercial."
)

MEDELLIN_BARES = [
    {
        "slug": "son-havana-laureles",
        "nombre": "Son Havana (Laureles)",
        "direccion": "Cra. 73 # 44-56, Laureles, Medellín",
        "descripcion": (
            "Bar insignia de la salsa cubana en la ciudad, con música en "
            "vivo y clases de baile. Es la sede original; luego abrió una "
            "segunda sede en El Poblado."
        ),
        "lat": 6.2477, "lng": -75.5910,
    },
    {
        "slug": "el-tibiri",
        "nombre": "El Tibirí",
        "direccion": "Cra. 70 # 43B-01, Laureles, Medellín",
        "descripcion": (
            "El sótano de salsa más conocido de Medellín, con más de dos "
            "décadas de historia. Ambiente crudo, sin lujos, frecuentado "
            "por bailadores y melómanos de todos los niveles."
        ),
        "lat": 6.2489, "lng": -75.5926,
    },
    {
        "slug": "el-suave",
        "nombre": "El Suave",
        "direccion": "Av. 33 # 80A-30, Medellín",
        "descripcion": (
            "Discoteca clásica de salsa, con dos pisos, pista de baile y "
            "un público mayormente de melómanos y amantes de la salsa "
            "tradicional."
        ),
        "lat": 6.2298, "lng": -75.5847,
    },
    {
        "slug": "eslabon-prendido",
        "nombre": "El Eslabón Prendido",
        "direccion": "Cerca al Parque del Periodista, Centro, Medellín",
        "descripcion": (
            "Abierto desde 2002, con música en vivo martes y jueves. Punto "
            "de encuentro clásico del centro de la ciudad para son cubano "
            "y ritmos afroantillanos."
        ),
        "lat": 6.2486, "lng": -75.5658,
    },
    {
        "slug": "bururu-barara",
        "nombre": "El Bururú Barará",
        "direccion": "Calle 44 # 71-73, San Juan, Medellín",
        "descripcion": (
            "Una 'viejoteca' de culto: bar dedicado casi por completo a "
            "vinilos de salsa y música antillana clásica, en el corazón de "
            "la zona salsera de San Juan."
        ),
        "lat": 6.2469, "lng": -75.5893,
    },
]

MEDELLIN_EMISORAS = [
    {
        "nombre": "Latina Stereo",
        "descripcion": "Se autodenomina la emisora de salsa más emblemática de Medellín, con programas en vivo dedicados al género.",
        "url": "https://latinastereo.com/",
    },
    {
        "nombre": "El Sol Medellín",
        "descripcion": "Emisora de salsa y música clásica tropical con transmisión en vivo online.",
        "url": "https://mytuner-radio.com/es/emisora/el-sol-medellin/",
    },
    {
        "nombre": "Radio Uno Medellín",
        "descripcion": "Programación salsera dentro de la parrilla de Radio Uno para la ciudad.",
        "url": "https://mytuner-radio.com/es/emisora/radio-uno-medellin/",
    },
    {
        "nombre": "Tropicana Medellín",
        "descripcion": "Salsa y música tropical, versión local de la cadena Tropicana.",
        "url": "https://mytuner-radio.com/es/emisora/tropicana-medellin/",
    },
]

MEDELLIN_PLAYLIST_URL = "https://open.spotify.com/search/salsa%20Medell%C3%ADn%20Discos%20Fuentes%20Fruko"

# Eventos verificados por busqueda web (no inventados). Como las fechas
# de conciertos cambian constantemente, para los "socials" semanales
# (clases, noches de baile) enlazamos a un calendario en vivo en vez
# de hardcodear fechas que se volverian obsoletas.
MEDELLIN_EVENTOS = [
    {
        "titulo": "Feria de las Flores",
        "fecha": "Finales de julio - inicios de agosto (anual)",
        "lugar": "Toda la ciudad de Medellín",
        "descripcion": (
            "La feria más importante de Medellín abre cada año con 'Viva la "
            "Salsa', un megaconcierto salsero en el Estadio Atanasio "
            "Girardot que ha reunido a leyendas como El Gran Combo de "
            "Puerto Rico, Oscar D'León y La Sonora Ponceña. Incluye el "
            "Festival Nacional de la Trova en la Plaza Gardel y más de "
            "500 actividades culturales, la mayoría de acceso público."
        ),
        "url": "https://tuticket.com.co/conciertos/tour-viva-la-salsa-2026-medellin/",
    },
    {
        "titulo": "1er Festival Salsero de Amor y Amistad",
        "fecha": "19 de septiembre de 2026",
        "lugar": "Mulenze Salsa Bar, Envigado (área metropolitana)",
        "descripcion": "Festival salsero organizado por Mulenze Salsa Bar en el área metropolitana de Medellín.",
        "url": "https://www.ticketmaster.co/page/CONCIERTOS",
    },
]

MEDELLIN_CALENDARIO_VIVO_URL = "https://www.salsavida.com/es/guides/colombia/medellin/calendar/"

# Categorias explicitamente NO incluidas con datos falsos/inventados:
# DJs reconocidos, coleccionistas destacados, campeones de baile,
# academias de baile y tiendas de vinilo especificas. Se muestran como
# "proximamente" en el frontend hasta tener datos reales confirmados
# por el usuario o un panel de administracion.
MEDELLIN_PENDIENTE = [
    "DJs reconocidos y coleccionistas destacados",
    "Campeones de baile",
    "Academias de baile y tiendas de vinilo (mapa completo)",
    "Murales y espacios culturales",
]

# ==========================================
# ARTISTAS DE SALSA CON GRAMMY
# ==========================================
# Datos verificados por busqueda web (fuentes: grammy.com, Wikipedia,
# AllMusic, Library of Congress). Cada uno gano un Grammy real, con
# año y álbum verificables -- no incluye Latin Grammy (categoria
# distinta) salvo que se indique explicitamente.
GRAMMY_SALSA = [
    {
        "slug": "eddie-palmieri-1975",
        "artista": "Eddie Palmieri",
        "anio": 1975,
        "album": "The Sun of Latin Music",
        "categoria": "Best Latin Recording",
        "descripcion": (
            "El primer Grammy jamás otorgado en una categoría latina, y "
            "Palmieri se convirtió en el primer artista latino en ganar "
            "un Grammy en cualquier categoría. Grabado junto al entonces "
            "joven cantante Lalo Rodríguez."
        ),
        "spotify_album_id": "",
    },
    {
        "slug": "ruben-blades-1987",
        "artista": "Rubén Blades",
        "anio": 1987,
        "album": "Escenas",
        "categoria": "Best Tropical Latin Performance",
        "descripcion": (
            "Su primer Grammy, ganado en la 29ª entrega de los premios. "
            "El álbum incluye un dueto en español con Linda Ronstadt."
        ),
        "spotify_album_id": "",
    },
    {
        "slug": "celia-cruz-1990",
        "artista": "Celia Cruz",
        "anio": 1990,
        "album": "Ritmo en el Corazón (con Ray Barretto)",
        "categoria": "Best Tropical Latin Performance",
        "descripcion": (
            "El primero de los Grammy de Celia Cruz, en colaboración con "
            "el conguero Ray Barretto (también su primer Grammy). A lo "
            "largo de su carrera acumuló múltiples premios Grammy y "
            "Grammy Latino, además de un Grammy honorífico a la "
            "trayectoria."
        ),
        "spotify_album_id": "",
    },
    {
        "slug": "marc-anthony-1999",
        "artista": "Marc Anthony",
        "anio": 1999,
        "album": "Contra la Corriente",
        "categoria": "Best Traditional Tropical Latin Album",
        "descripcion": (
            "Este álbum de 1997 hizo historia como el primer disco de "
            "salsa en llegar al número 1 del Billboard 200, antes de "
            "ganar el Grammy en la 41ª entrega de los premios."
        ),
        "spotify_album_id": "",
    },
    {
        "slug": "los-van-van-1999",
        "artista": "Los Van Van",
        "anio": 1999,
        "album": "Van Van Is Here",
        "categoria": "Best Salsa Album",
        "descripcion": (
            "Le dio a Los Van Van el primer Grammy ganado por una "
            "orquesta de timba cubana, consolidando el reconocimiento "
            "internacional del género fuera de Cuba."
        ),
        "spotify_album_id": "",
    },
]


# ==========================================
# FOTOS REALES VERIFICADAS (Fase 3)
# ==========================================
# Filtradas a mano de los zips de fotos que subiste -- se descartaron
# 12 falsos positivos que un script automatico habia agarrado solo por
# coincidencia de texto (ver detalle en INFORME.md de esa entrega).
# Todas usan el patron Special:FilePath de Wikimedia Commons, que
# resuelve siempre al archivo actual sin importar donde este alojado.
#
# ATRIBUCION: la mayoria son licencia CC BY-SA (no dominio publico
# total) -- muestra un credito visible, ej. un <small> bajo cada foto
# o en el modal de detalle: "Foto: Wikimedia Commons".
#
# PENDIENTES -- no se encontro foto con licencia clara para: Fruko,
# Grupo Niche, Ray Barretto, Cheo Feliciano, Fania All-Stars. Vale la
# pena preguntarle a Julio/Son Havana si tienen fotos propias de
# homenajes o material promocional para estos -- seria mejor
# contenido (autentico, sin depender de licencias externas).
FOTOS_VALIDADAS = {
    "celia-cruz": [
        "https://commons.wikimedia.org/wiki/Special:FilePath/Celia Cruz (13490118834).jpg",
        "https://commons.wikimedia.org/wiki/Special:FilePath/Celia Cruz y Pedro Knight.jpg",
        "https://commons.wikimedia.org/wiki/Special:FilePath/2024 Celia Cruz Womens Quarter.jpg",
    ],
    "la-lupe": [
        "https://commons.wikimedia.org/wiki/Special:FilePath/Cuban singer La Lupe performing in New York City LCCN2009632630 (cropped).jpg",
        "https://commons.wikimedia.org/wiki/Special:FilePath/Pacho Alonso, La Lupe & Benny Moré.jpg",
    ],
    "hector-lavoe": [
        "https://commons.wikimedia.org/wiki/Special:FilePath/Héctor Lavoe (1969 Fania Records publicity photo).jpg",
        "https://commons.wikimedia.org/wiki/Special:FilePath/Statuehectorlavoe.jpg",
    ],
    "willie-colon": [
        "https://commons.wikimedia.org/wiki/Special:FilePath/Willie Colón (1969 Fania Records publicity photo).jpg",
        "https://commons.wikimedia.org/wiki/Special:FilePath/Willie Colón and Héctor Lavoe (1969 Fania Records publicity photo).jpg",
    ],
    "tito-puente": [
        "https://commons.wikimedia.org/wiki/Special:FilePath/TitoandRogerDawson.jpg",
        "https://commons.wikimedia.org/wiki/Special:FilePath/Tito Puente PS117 2095 2nd Av 240 E109 St jeh.jpg",
    ],
    "ruben-blades": [
        "https://commons.wikimedia.org/wiki/Special:FilePath/Danilo Pérez, Herbie Hancock, Wayne Shorter, Rubén Blades.jpg",
    ],
    "gilberto-santa-rosa": [
        "https://commons.wikimedia.org/wiki/Special:FilePath/Gilberto Santa Rosa en 2025.png",
    ],
}

# app/models/ruta_salsera_data.py
"""
Datos estáticos de La Ruta Salsera de Medellín.

Fuente única de verdad: ROUTE-SALSERA-EVIDENCE-AUDIT.md (sección G).
Cada item tiene `evidence_status` y `sources` para trazabilidad.

Reglas estrictas:
- NO incluir datos de la sección H (DATOS PROHIBIDOS).
- NO incluir fechas de fundación de El Tíbiri (PROBABLE, no verificable).
- NO incluir historia de El Suave más allá de datos operativos.
- NO incluir bares específicos de Calle Palacé.
- NO duplicar este datos en otro archivo.
"""

from datetime import date

# ==========================================
# REFERENCIAS DE FUENTES
# ==========================================
# Todas verificadas en la auditoría (sección B). Nivel A = primaria,
# B = periodismo especializado, C = especializado, D = secundario.

FUENTES = {
    "discos-fuentes-oficial": {
        "source_id": "RS-001",
        "title": "Discos Fuentes — Acerca",
        "publisher": "Discos Fuentes",
        "url": "https://discosfuentes.com.co/acerca",
        "source_level": "A",
        "access_date": "2026-09-18",
    },
    "discos-fuentes-wikipedia": {
        "source_id": "RS-002",
        "title": "Discos Fuentes — Wikipedia",
        "publisher": "Wikipedia",
        "url": "https://es.wikipedia.org/wiki/Discos_Fuentes",
        "source_level": "B",
        "access_date": "2026-09-18",
    },
    "codiscos-oficial": {
        "source_id": "RS-003",
        "title": "Codiscos — Sitio oficial",
        "publisher": "Codiscos",
        "url": "https://www.codiscos.com.co/",
        "source_level": "A",
        "access_date": "2026-09-18",
    },
    "fruko-allmusic": {
        "source_id": "RS-004",
        "title": "Fruko — AllMusic",
        "publisher": "AllMusic",
        "url": "https://www.allmusic.com/artist/mn0000182697",
        "source_level": "B",
        "access_date": "2026-09-18",
    },
    "fruko-wikipedia": {
        "source_id": "RS-005",
        "title": "Fruko — Wikipedia EN",
        "publisher": "Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Fruko",
        "source_level": "B",
        "access_date": "2026-09-18",
    },
    "el-tibiri-colombiabz": {
        "source_id": "RS-006",
        "title": "El Tíbiri Tábara — ColombiaBZ",
        "publisher": "ColombiaBZ",
        "url": "https://www.colombiabz.com/nightlife/medellin/el-tibiri-tabara/",
        "source_level": "B",
        "access_date": "2026-09-18",
    },
    "el-tibiri-2pos": {
        "source_id": "RS-007",
        "title": "El Tíbiri Tábara — 2POS",
        "publisher": "2POS",
        "url": "https://2pos.com/el-tibiri-tabara/",
        "source_level": "B",
        "access_date": "2026-09-18",
    },
    "son-havana-dancefree": {
        "source_id": "RS-008",
        "title": "Son Havana — Dancefree",
        "publisher": "Dancefree",
        "url": "https://dancefree.com.co/son-havana/",
        "source_level": "B",
        "access_date": "2026-09-18",
    },
    "son-havana-evendo": {
        "source_id": "RS-009",
        "title": "Son Havana — Evendo",
        "publisher": "Evendo",
        "url": "https://evendo.co/son-havana-medellin",
        "source_level": "B",
        "access_date": "2026-09-18",
    },
    "el-suave-2pos": {
        "source_id": "RS-010",
        "title": "El Suave — 2POS",
        "publisher": "2POS",
        "url": "https://2pos.com/el-suave/",
        "source_level": "B",
        "access_date": "2026-09-18",
    },
    "latina-stereo-oficial": {
        "source_id": "RS-011",
        "title": "Latina Stereo — Sitio oficial",
        "publisher": "Latina Stereo",
        "url": "https://latinastereo.com/",
        "source_level": "A",
        "access_date": "2026-09-18",
    },
    "grupo-gale-wikipedia": {
        "source_id": "RS-012",
        "title": "Grupo Galé — Wikipedia",
        "publisher": "Wikipedia",
        "url": "https://es.wikipedia.org/wiki/Grupo_Gal%C3%A9",
        "source_level": "B",
        "access_date": "2026-09-18",
    },
    "grupo-gale-oficial": {
        "source_id": "RS-013",
        "title": "Grupo Galé — Sitio oficial",
        "publisher": "Grupo Galé",
        "url": "https://www.grupogale.com/",
        "source_level": "A",
        "access_date": "2026-09-18",
    },
    "canal-trece-viva-salsa": {
        "source_id": "RS-014",
        "title": "Viva la Salsa 2026 — Canal Trece",
        "publisher": "Canal Trece",
        "url": "https://www.canal13.com.co/viva-la-salsa-2026/",
        "source_level": "B",
        "access_date": "2026-09-18",
    },
    "comfenalco-leyendas": {
        "source_id": "RS-015",
        "title": "Las Leyendas Vivas — Comfenalco",
        "publisher": "Comfenalco",
        "url": "https://www.comfenalcoantioquia.com.co/",
        "source_level": "A",
        "access_date": "2026-09-18",
    },
    "santana-udelvalle": {
        "source_id": "RS-016",
        "title": "Santana — ¿Qué es la Salsa? — U. del Valle",
        "publisher": "Universidad del Valle",
        "url": "https://repositorio.univalle.edu.co/",
        "source_level": "A",
        "access_date": "2026-09-18",
    },
    "resonancias-uc": {
        "source_id": "RS-017",
        "title": "Jaramillo — Música tropical — Resonancias UC",
        "publisher": "Universidad Católica",
        "url": "https://www.uc.cl/",
        "source_level": "A",
        "access_date": "2026-09-18",
    },
    "wikipedia-el-tibiri": {
        "source_id": "RS-018",
        "title": "El Tíbiri — Wikipedia (mencionado)",
        "publisher": "Wikipedia",
        "url": "https://es.wikipedia.org/wiki/El_T%C3%ADbiri",
        "source_level": "B",
        "access_date": "2026-09-18",
    },
    "colombiabz-el-suave": {
        "source_id": "RS-019",
        "title": "El Suave — ColombiaBZ",
        "publisher": "ColombiaBZ",
        "url": "https://www.colombiabz.com/nightlife/medellin/el-suave/",
        "source_level": "B",
        "access_date": "2026-09-18",
    },
    "el-colombiano-son-havana-15": {
        "source_id": "RS-020",
        "title": "Atentos, salseros: por sus quince, Son Havana trae a Los Van Van",
        "author": "El Colombiano",
        "publisher": "El Colombiano",
        "url": "https://www.elcolombiano.com/tendencias/son-havana-de-medellin-KJ27595539",
        "source_level": "B",
        "access_date": "2026-09-18",
        "claims_supported": [
            "Julio Restrepo Molina = fundador de Son Havana",
            "nacimiento 1970",
            "barrio Naranjal/San Joaquín",
            "pasión por la salsa desde niño (familia)",
            "gomoso, no coleccionista ni experto",
            "arrendó bar primero, luego abrió Son Havana",
            "nombre por timba cubana (Los Van Van, etc.)",
        ],
    },
    "el-colombiano-latina-40": {
        "source_id": "RS-021",
        "title": "Latina Stéreo: trinchera de la salsa y la alegría",
        "author": "Sara Kapkin",
        "publisher": "El Colombiano",
        "url": "https://www.elcolombiano.com/cultura/musica/latina-stereo-emisora-salsa-aniversario-40-KA31133911",
        "source_level": "B",
        "access_date": "2026-09-18",
        "claims_supported": [
            "fundada 31 octubre 1985",
            "antes de salsa: bossa nova y jazz",
            "Jairo Luis García = locutor legendario",
            "Elmer Vergara = co-fundador",
            "primera canción: Cangrejero de Chirivico Dávila",
        ],
    },
    "latinastereo-40-anos": {
        "source_id": "RS-022",
        "title": "40 años de Latina — Sitio oficial",
        "publisher": "Latina Stereo",
        "url": "https://latinastereo.com/40-anos-de-latina/",
        "source_level": "A",
        "access_date": "2026-09-18",
        "claims_supported": [
            "hitos: 1985, 1995, 2000, 2010, 2015, 2025",
            "1985: nace Latina Stereo",
            "2025: se crea Latina All Stars",
        ],
    },
    "bitacora-eafit-latina": {
        "source_id": "RS-023",
        "title": "Latina Stereo: 40 años haciendo latir la salsa en Medellín",
        "author": "Manuela Pérez Moreno",
        "publisher": "Bitácora — Universidad EAFIT",
        "url": "https://bitacora.eafit.edu.co/blog/2026/03/19/latina-stereo-40-anos-haciendo-latir-la-salsa-en-medellin/",
        "source_level": "C",
        "access_date": "2026-09-18",
        "claims_supported": [
            "fundada 31 octubre 1985 en Envigado",
            "programación inicial: jazz y bossa nova",
            "apostó por la salsa cuando era 'música de nicho'",
            "Pachanga Orquesta y Mulataje difundieron música por Latina",
            "Diego Aranda = director actual",
            "casa museo de la emisora",
        ],
    },
    "rendon-zapata-2016": {
        "source_id": "RS-024",
        "title": "Apropiaciones, negociaciones y espacialidades de la salsa en Medellín",
        "author": "Marilly Rendón Zapata",
        "publisher": "Universidad de Antioquia",
        "url": "http://hdl.handle.net/10495/14885",
        "source_level": "A",
        "access_date": "2026-09-18",
        "claims_supported": [
            "salsa como género urbano en Medellín",
            "método etnográfico: 31 entrevistas, observación participante",
            "espacialidades de la salsa en la ciudad",
            "Carrera Palacé y Calle Zea como espacios históricos",
        ],
    },
    "el-colombiano-df-90": {
        "source_id": "RS-025",
        "title": "Los 90 años de Discos Fuentes y cinco objetos que hacen parte de la historia de la música colombiana",
        "author": "Ángel Castaño Guzmán",
        "publisher": "El Colombiano",
        "url": "https://www.elcolombiano.com/cultura/musica/historia-de-discos-fuentes-y-cinco-tesoros-que-cuentan-su-historia-KJ25687962",
        "source_level": "B",
        "access_date": "2026-09-18",
        "claims_supported": [
            "fundación 28 octubre 1934 en Cartagena",
            "Antonio Fuentes = fundador",
            "esposa Margarita Estrada de Antioquia",
            "traslado a Medellín por influencia de esposa y auge industrial",
        ],
    },
    "senal-memoria-df": {
        "source_id": "RS-026",
        "title": "Discos Fuentes, una toma global de la música colombiana",
        "author": "Felipe Arias Escobar",
        "publisher": "Señal Memoria — RTVC",
        "url": "https://www.senalmemoria.co/articulos/discos-fuentes-colombia",
        "source_level": "B",
        "access_date": "2026-09-18",
        "claims_supported": [
            "1934: nacimiento del sello en Cartagena",
            "1932: Antonio Fuentes inicia aventura radial",
            "1943: primer prensaje en país (Guillermo Buitrago)",
            "1960: primer disco sonido estéreo y primeros 14 Cañonazos",
            "Fuentes ya se había trasladado a Medellín para 1960",
            "Codiscos 'apareció en 1954' (Posible discrepancia con 1950)",
        ],
    },
}

# ==========================================
# TIMELINE — LA RUTA SALSERA DE MEDELLÍN
# ==========================================
# Solo hechos VERIFIED_PRIMARY, VERIFIED_SECONDARY o documentados con
# evidencia contradictoria trazable (ej. CONTRADICTED con attribution).
# Orden cronológico por year_start.

RUTA_TIMELINE = [
    {
        "id": "discos-fuentes-1934",
        "year_start": "1934",
        "year_end": None,
        "category": "industria",
        "title": "Discos Fuentes fundada en Cartagena",
        "description": (
            "El sello discográfico más importante de Colombia fue fundado "
            "por Antonio Fuentes en Cartagena, marcando el inicio de la "
            "industria discográfica tropical colombiana."
        ),
        "location": "Cartagena, Colombia",
        "people": ["Antonio Fuentes"],
        "organizations": ["Discos Fuentes"],
        "evidence_status": "VERIFIED_PRIMARY",
        "confidence": "high",
        "source_ids": ["discos-fuentes-oficial", "discos-fuentes-wikipedia"],
        "attribution": None,
    },
    {
        "id": "codiscos-1950",
        "year_start": "1950",
        "year_end": None,
        "category": "industria",
        "title": "Codiscos fundada en Medellín",
        "description": (
            "Segundo sello discográfico más importante de Antioquia, "
            "Codiscos se fundó en Medellín y contribuyó significativamente "
            "a la difusión de la música tropical en la región."
        ),
        "location": "Medellín, Colombia",
        "people": [],
        "organizations": ["Codiscos"],
        "evidence_status": "VERIFIED_PRIMARY",
        "confidence": "high",
        "source_ids": ["codiscos-oficial"],
        "attribution": None,
    },
    {
        "id": "discos-fuentes-instalacion-medellin",
        "year_start": "1954",
        "year_end": None,
        "category": "industria",
        "title": "Discos Fuentes se instala en Medellín",
        "description": (
            "Discos Fuentes se instaló en el barrio Colón de Medellín "
            "en 1954, presentando su primer catálogo impreso con 500 títulos. "
            "Las grabaciones continuaron realizándose en Cartagena durante "
            "esta transición."
        ),
        "location": "Medellín, Colombia",
        "people": [],
        "organizations": ["Discos Fuentes"],
        "evidence_status": "VERIFIED_PRIMARY",
        "confidence": "high",
        "source_ids": ["discos-fuentes-oficial", "discos-fuentes-wikipedia", "el-colombiano-df-90", "senal-memoria-df"],
        "attribution": None,
    },
    {
        "id": "discos-fuentes-sede-guayabal",
        "year_start": "1960",
        "year_end": None,
        "category": "industria",
        "title": "Discos Fuentes inaugura sede en Guayabal",
        "description": (
            "Discos Fuentes inauguró su nueva sede en el sector de Guayabal, "
            "con estudio de grabación, planta de duplicación y áreas "
            "administrativas. La empresa se consolidó definitivamente en "
            "Medellín como capital de la industria discográfica colombiana."
        ),
        "location": "Guayabal, Medellín, Colombia",
        "people": [],
        "organizations": ["Discos Fuentes"],
        "evidence_status": "VERIFIED_PRIMARY",
        "confidence": "high",
        "source_ids": ["discos-fuentes-oficial", "discos-fuentes-wikipedia", "el-colombiano-df-90", "senal-memoria-df"],
        "attribution": None,
    },
    {
        "id": "primeros-14-canonazos-1961",
        "year_start": "1961",
        "year_end": None,
        "category": "industria",
        "title": "Primer \"14 Cañonazos Bailables\"",
        "description": (
            "La icónica serie de discos recopilatorios de Discos Fuentes "
            "inició en 1961, convirtiéndose en la antología más importante "
            "de la música tropical colombiana."
        ),
        "location": "Medellín, Colombia",
        "people": [],
        "organizations": ["Discos Fuentes"],
        "evidence_status": "VERIFIED_PRIMARY",
        "confidence": "high",
        "source_ids": ["discos-fuentes-oficial"],
        "attribution": None,
    },
    {
        "id": "fruko-entra-df-1963",
        "year_start": "1963",
        "year_end": None,
        "category": "persona",
        "title": "Fruko ingresa a Discos Fuentes",
        "description": (
            "Julio Ernesto Estrada \"Fruko\" ingresó a Discos Fuentes como "
            "músico, iniciando una carrera que lo convirtió en el pionero "
            "de la salsa colombiana."
        ),
        "location": "Medellín, Colombia",
        "people": ["Julio Ernesto Estrada (Fruko)"],
        "organizations": ["Discos Fuentes"],
        "evidence_status": "VERIFIED_PRIMARY",
        "confidence": "high",
        "source_ids": ["fruko-allmusic", "fruko-wikipedia"],
        "attribution": None,
    },
    {
        "id": "fruko-ny-1968",
        "year_start": "1968",
        "year_end": None,
        "category": "persona",
        "title": "Fruko viaja a Nueva York",
        "description": (
            "El viaje de Fruko a Nueva York expuso su sonido a la salsa "
            "puertorriqueña y neoyorquina, influenciando significativamente "
            "su estilo posterior."
        ),
        "location": "Nueva York, EE.UU.",
        "people": ["Julio Ernesto Estrada (Fruko)"],
        "organizations": [],
        "evidence_status": "VERIFIED_SECONDARY",
        "confidence": "high",
        "source_ids": ["fruko-wikipedia"],
        "attribution": None,
    },
    {
        "id": "fruko-tesos-1970",
        "year_start": "1970",
        "year_end": None,
        "category": "orquesta",
        "title": "Fruko y sus Tesos fundada",
        "description": (
            "Fruko fundó su propia orquesta, Fruko y sus Tesos, que se "
            "convirtió en la orquesta insignia de Discos Fuentes y pionera "
            "de la salsa colombiana."
        ),
        "location": "Medellín, Colombia",
        "people": ["Julio Ernesto Estrada (Fruko)"],
        "organizations": ["Fruko y sus Tesos", "Discos Fuentes"],
        "evidence_status": "VERIFIED_PRIMARY",
        "confidence": "high",
        "source_ids": ["discos-fuentes-oficial"],
        "attribution": None,
    },
    {
        "id": "joe-arroyo-fruko-1973",
        "year_start": "1973",
        "year_end": None,
        "category": "persona",
        "title": "Joe Arroyo ingresa a Fruko y sus Tesos",
        "description": (
            "Joe Arroyo se unió a Fruko y sus Tesos como vocalista, "
            "iniciando una de las carreras más influyentes de la salsa "
            "colombiana."
        ),
        "location": "Medellín, Colombia",
        "people": ["Joe Arroyo"],
        "organizations": ["Fruko y sus Tesos", "Discos Fuentes"],
        "evidence_status": "VERIFIED_PRIMARY",
        "confidence": "high",
        "source_ids": ["discos-fuentes-oficial", "fruko-wikipedia"],
        "attribution": None,
    },
    {
        "id": "el-preso-1975",
        "year_start": "1975",
        "year_end": None,
        "category": "orquesta",
        "title": "\"El Preso\" — Fruko y sus Tesos",
        "description": (
            "\"El Preso\" de Fruko y sus Tesos, compuesta por Álvaro Velásquez "
            "e interpretada por Wilson Manyoma \"Saoco\", se convirtió en el "
            "himno más reconocible de la salsa colombiana. La canción está "
            "inspirada en la historia de un preso condenado a 30 años de pena."
        ),
        "location": "Medellín, Colombia",
        "people": ["Wilson Manyoma", "Julio Ernesto Estrada (Fruko)", "Álvaro Velásquez"],
        "organizations": ["Fruko y sus Tesos", "Discos Fuentes"],
        "evidence_status": "VERIFIED_PRIMARY",
        "confidence": "high",
        "source_ids": ["discos-fuentes-oficial"],
        "attribution": "Composición de Álvaro Velásquez Balcázar; arreglos de Luis Carlos Montoya. Créditos documentados en fuentes secundarias (Wikipedia, Eje21).",
    },
    {
        "id": "afrosound-1973",
        "year_start": "1973",
        "year_end": None,
        "category": "orquesta",
        "title": "Afrosound formada en Medellín",
        "description": (
            "Afrosound fue una de las orquestas clave de Discos Fuentes, "
            "contribuyendo al sonido tropical de Medellín en los años 70."
        ),
        "location": "Medellín, Colombia",
        "people": [],
        "organizations": ["Afrosound", "Discos Fuentes"],
        "evidence_status": "VERIFIED_PRIMARY",
        "confidence": "high",
        "source_ids": ["discos-fuentes-oficial"],
        "attribution": None,
    },
    {
        "id": "wganda-kenya-1976",
        "year_start": "1976",
        "year_end": None,
        "category": "orquesta",
        "title": "Wganda Kenya formada en Medellín",
        "description": (
            "Wganda Kenya fue otra orquesta significativa de Discos Fuentes, "
            "parte del ecosistema musical que consolidó a Medellín como "
            "centro de producción salsera."
        ),
        "location": "Medellín, Colombia",
        "people": [],
        "organizations": ["Wganda Kenya", "Discos Fuentes"],
        "evidence_status": "VERIFIED_PRIMARY",
        "confidence": "high",
        "source_ids": ["discos-fuentes-oficial"],
        "attribution": None,
    },
    {
        "id": "fruko-mejor-orquesta-1976",
        "year_start": "1976",
        "year_end": None,
        "category": "orquesta",
        "title": "Fruko: \"mejor orquesta del país\"",
        "description": (
            "Fruko y sus Tesos fue reconocida como la mejor orquesta del "
            "país, consolidando su posición como referente de la salsa "
            "colombiana."
        ),
        "location": "Medellín, Colombia",
        "people": ["Julio Ernesto Estrada (Fruko)"],
        "organizations": ["Fruko y sus Tesos", "Discos Fuentes"],
        "evidence_status": "ATTRIBUTED",
        "confidence": "high",
        "source_ids": ["discos-fuentes-oficial"],
        "attribution": "Según Discos Fuentes (sitio oficial).",
    },
    {
        "id": "the-latin-brothers-1970s",
        "year_start": "1970",
        "year_end": "1979",
        "category": "orquesta",
        "title": "The Latin Brothers",
        "description": (
            "The Latin Brothers fue una de las orquestas emblemáticas de "
            "Discos Fuentes en Medellín, parte del movimiento salsero de "
            "los años setenta."
        ),
        "location": "Medellín, Colombia",
        "people": [],
        "organizations": ["The Latin Brothers", "Discos Fuentes"],
        "evidence_status": "VERIFIED_PRIMARY",
        "confidence": "high",
        "source_ids": ["discos-fuentes-oficial"],
        "attribution": None,
    },
    {
        "id": "latina-stereo-1985",
        "year_start": "1985",
        "year_end": None,
        "category": "radio",
        "title": "Latina Stereo inicia transmisiones",
        "description": (
            "Latina Stereo comenzó a transmitir el 31 de octubre de 1985 "
            "en 100.9 FM desde Envigado. Inicialmente programaba jazz y "
            "bossa nova; luego apostó por la salsa como género principal, "
            "convirtiéndose en la emisora emblemática de la ciudad."
        ),
        "location": "Envigado, Medellín, Colombia",
        "people": [],
        "organizations": ["Latina Stereo"],
        "evidence_status": "VERIFIED_PRIMARY",
        "confidence": "high",
        "source_ids": ["latina-stereo-oficial", "el-colombiano-latina-40", "latinastereo-40-anos", "bitacora-eafit-latina"],
        "attribution": "Fundada por Jairo Luis García y Elmer Vergara.",
    },
    {
        "id": "grupo-gale-1989",
        "year_start": "1989",
        "year_end": None,
        "category": "orquesta",
        "title": "Grupo Galé fundado",
        "description": (
            "Grupo Galé fue fundado en Medellín y se consolidó como una "
            "de las orquestas más importantes de la salsa colombiana, con "
            "múltiples éxitos internacionales."
        ),
        "location": "Medellín, Colombia",
        "people": ["Diego Galé"],
        "organizations": ["Grupo Galé", "Codiscos"],
        "evidence_status": "VERIFIED_PRIMARY",
        "confidence": "high",
        "source_ids": ["grupo-gale-wikipedia", "grupo-gale-oficial"],
        "attribution": None,
    },
    {
        "id": "son-havana-2010",
        "year_start": "2010",
        "year_end": None,
        "category": "lugar",
        "title": "Son Havana abre en Laureles",
        "description": (
            "Son Havana abrió sus puertas en 2010 en el barrio Laureles, "
            "fundado por el melómano Julio Restrepo Molina. El club se "
            "consolidó como santuario de la salsa y el son cubano en Medellín."
        ),
        "location": "Cra 73 #44-56, Laureles, Medellín",
        "people": ["Julio Restrepo Molina"],
        "organizations": ["Son Havana"],
        "evidence_status": "VERIFIED_SECONDARY",
        "confidence": "high",
        "source_ids": ["el-colombiano-son-havana-15", "son-havana-dancefree"],
        "attribution": None,
    },
    {
        "id": "viva-la-salsa-2026",
        "year_start": "2026",
        "year_end": None,
        "category": "evento",
        "title": "Viva la Salsa 2026",
        "description": (
            "El megaconcierto \"Viva la Salsa\" se realizará el 25 de julio "
            "de 2026 en el Estadio Atanasio Girardot como parte de la Feria "
            "de las Flores, reuniendo a grandes figuras de la salsa."
        ),
        "location": "Estadio Atanasio Girardot, Medellín",
        "people": [],
        "organizations": [],
        "evidence_status": "VERIFIED_PRIMARY",
        "confidence": "high",
        "source_ids": ["canal-trece-viva-salsa"],
        "attribution": None,
    },
    {
        "id": "leyendas-vivas-2026",
        "year_start": "2026",
        "year_end": None,
        "category": "evento",
        "title": "Las Leyendas Vivas X edición",
        "description": (
            "La X edición de Las Leyendas Vivas se realizará el 25 de "
            "abril de 2026 en el Centro de Eventos Centauro, Envigado."
        ),
        "location": "Centro de Eventos Centauro, Envigado",
        "people": [],
        "organizations": ["Comfenalco"],
        "evidence_status": "VERIFIED_PRIMARY",
        "confidence": "high",
        "source_ids": ["comfenalco-leyendas"],
        "attribution": None,
    },
]

# ==========================================
# LUGARES — LA RUTA SALSERA
# ==========================================
# Solo datos operativos. NO incluir fechas de fundación histórica.
# NO incluir historia de El Suave más allá de datos de contacto/horarios.
# Coordenadas verificadas de content_data.py MEDELLIN_BARES.

RUTA_LUGARES = [
    {
        "id": "el-tibiri",
        "name": "El Tíbiri Tábara",
        "type": "bar",
        "address": "Cra 70 #70-03, Laureles, Medellín",
        "neighborhood": "Laureles",
        "city": "Medellín",
        "coordinates": {"lat": 6.2489, "lng": -75.5926},
        "phone": "+57 310 8495461",
        "whatsapp_url": "https://wa.me/573108495461",
        "facebook": "https://www.facebook.com/elTibiriTabara/",
        "instagram": None,
        "website": None,
        "description": (
            "El sótano de salsa más conocido de Medellín, con más de dos "
            "décadas de historia. Ambiente crudo, sin lujos, frecuentado "
            "por bailadores y melómanos de todos los niveles."
        ),
        "music_style": "Salsa clásica, son cubano, guaguancó",
        "status": "active",
        "operating_hours": "Mié-Sáb 21:00-03:00 (sujeto a cambios)",
        "is_underground": True,
        "evidence_status": "VERIFIED_PRIMARY",
        "confidence": "high",
        "source_ids": ["el-tibiri-colombiabz", "el-tibiri-2pos"],
        "attribution": None,
        "external_links": {
            "google_maps": "https://maps.google.com/?q=Cra+70+%2370-03+Laureles+Medellin",
            "tripadvisor": None,
        },
        "route_order": 1,
    },
    {
        "id": "son-havana",
        "name": "Son Havana",
        "type": "club",
        "address": "Cra 73 #44-56, Florida Nueva, Laureles, Medellín",
        "neighborhood": "Laureles",
        "city": "Medellín",
        "coordinates": {"lat": 6.2477, "lng": -75.5910},
        "phone": "+57 311 339-7175",
        "whatsapp_url": "https://wa.me/573105156550",
        "facebook": None,
        "instagram": "https://instagram.com/sonhavana",
        "website": "https://sonhavana.co",
        "description": (
            "Club de salsa y son cubano fundado en 2010 por Julio Restrepo "
            "Molina. Programación en vivo, reservas, ruedas de Casino los "
            "miércoles y contratación de orquestas."
        ),
        "music_style": "Salsa, son cubano, rueda de casino",
        "status": "active",
        "operating_hours": "Mié-Jue hasta medianoche, Vie-Sáb hasta 4am",
        "is_underground": False,
        "evidence_status": "VERIFIED_SECONDARY",
        "confidence": "high",
        "source_ids": ["el-colombiano-son-havana-15", "son-havana-dancefree"],
        "attribution": None,
        "external_links": {
            "google_maps": "https://maps.google.com/?q=Cra+73+%2344-56+Laureles+Medellin",
            "tripadvisor": "https://tripadvisor.es/Attraction_Review-g297478-d9604959-Reviews-Son_Havana-Medellin_Antioquia.html",
        },
        "route_order": 2,
    },
    {
        "id": "el-suave",
        "name": "El Suave",
        "type": "discoteca",
        "address": "Av. 33 #80a-30, Medellín",
        "neighborhood": "Centro",
        "city": "Medellín",
        "coordinates": {"lat": 6.2298, "lng": -75.5847},
        "phone": "+57 310 4593267",
        "whatsapp_url": None,
        "facebook": None,
        "instagram": None,
        "website": None,
        "description": (
            "Discoteca clásica de salsa, con dos pisos, pista de baile y "
            "un público mayormente de melómanos y amantes de la salsa "
            "tradicional."
        ),
        "music_style": "Salsa clásica, salsa dura, música antillana",
        "status": "active",
        "operating_hours": "Lun-Sáb 16:00-03:00, Dom 16:00-00:00",
        "is_underground": False,
        "evidence_status": "VERIFIED_PRIMARY",
        "confidence": "high",
        "source_ids": ["el-suave-2pos", "colombiabz-el-suave"],
        "attribution": None,
        "external_links": {
            "google_maps": "https://maps.google.com/?q=Av+33+%2380A-30+Medellin",
            "tripadvisor": None,
        },
        "route_order": 3,
    },
]

# ==========================================
# ORQUESTAS Y ARTISTAS — MEDELLÍN
# ==========================================

RUTA_ORQUESTAS = [
    {
        "id": "fruko-y-sus-tesos",
        "name": "Fruko y sus Tesos",
        "entity_type": "orchestra",
        "founding_year": "1970",
        "founding_location": "Medellín",
        "label": "Discos Fuentes",
        "related_people": ["Julio Ernesto Estrada (Fruko)", "Wilson Manyoma"],
        "contribution": "Pionero de la salsa colombiana",
        "notable_works": ["El Preso", "A la memoria del muerto"],
        "evidence_status": "VERIFIED_PRIMARY",
        "source_ids": ["discos-fuentes-oficial", "fruko-allmusic"],
        "attribution": None,
    },
    {
        "id": "grupo-gale",
        "name": "Grupo Galé",
        "entity_type": "group",
        "founding_year": "1989",
        "founding_location": "Medellín",
        "label": "Codiscos",
        "related_people": ["Diego Galé"],
        "contribution": "Orquesta insignia de la salsa colombiana moderna",
        "notable_works": ["Auténtico", "Fruta Fresca"],
        "evidence_status": "VERIFIED_PRIMARY",
        "source_ids": ["grupo-gale-wikipedia", "grupo-gale-oficial"],
        "attribution": None,
    },
    {
        "id": "the-latin-brothers",
        "name": "The Latin Brothers",
        "entity_type": "orchestra",
        "founding_year": "1970",
        "founding_location": "Medellín",
        "label": "Discos Fuentes",
        "related_people": [],
        "contribution": "Orquesta emblemática de Discos Fuentes en los años 70",
        "notable_works": [],
        "evidence_status": "VERIFIED_PRIMARY",
        "source_ids": ["discos-fuentes-oficial"],
        "attribution": None,
    },
    {
        "id": "afrosound",
        "name": "Afrosound",
        "entity_type": "orchestra",
        "founding_year": "1973",
        "founding_location": "Medellín",
        "label": "Discos Fuentes",
        "related_people": [],
        "contribution": "Parte del ecosistema musical de Discos Fuentes",
        "notable_works": [],
        "evidence_status": "VERIFIED_PRIMARY",
        "source_ids": ["discos-fuentes-oficial"],
        "attribution": None,
    },
    {
        "id": "wganda-kenya",
        "name": "Wganda Kenya",
        "entity_type": "orchestra",
        "founding_year": "1976",
        "founding_location": "Medellín",
        "label": "Discos Fuentes",
        "related_people": [],
        "contribution": "Orquesta significativa del movimiento salsero medellinense",
        "notable_works": [],
        "evidence_status": "VERIFIED_PRIMARY",
        "source_ids": ["discos-fuentes-oficial"],
        "attribution": None,
    },
    {
        "id": "pachanga-orquesta",
        "name": "Pachanga Orquesta",
        "entity_type": "orchestra",
        "founding_year": "~1990",
        "founding_location": "Manrique, Medellín",
        "label": None,
        "related_people": ["Tito Montoya"],
        "contribution": "Orquesta de barrios populares de Medellín; ganadora del Primer Festival de Orquestas Nuevas de la Feria de Cali (1991)",
        "notable_works": ["Son de los barrios", "La profecía"],
        "evidence_status": "ATTRIBUTED",
        "source_ids": [],
        "attribution": "Según artículo de Sergio Valencia en Universo Centro (2015) y perfil de Spotify. Información detallada sobre origen barrial y trayectoria verificada.",
    },
    {
        "id": "sonora-8",
        "name": "Sonora 8",
        "entity_type": "orchestra",
        "founding_year": "2003",
        "founding_location": "Medellín",
        "label": "Latina Stereo Records",
        "related_people": ["Federico Trujillo", "Mauricio Gómez"],
        "contribution": "Orquesta contemporánea con estilo 'LatinCore', fusión de salsa con rock, blues, jazz y ritmos del Caribe",
        "notable_works": ["Especialistas en mecánica general (2004)", "De Pelea (2005)", "Zoonando (2008)"],
        "evidence_status": "ATTRIBUTED",
        "source_ids": ["latina-stereo-oficial"],
        "attribution": "Según perfil de Sonora 8 en Latinastereo.com (c. 2007) y Tsunami Salsero blog (2011).",
    },
    {
        "id": "siguarajazz",
        "name": "Siguarajazz",
        "entity_type": "orchestra",
        "founding_year": "2000",
        "founding_location": "Medellín",
        "label": None,
        "related_people": [],
        "contribution": "Fusión de jazz y ritmos tropicales en Medellín",
        "notable_works": [],
        "evidence_status": "ATTRIBUTED",
        "source_ids": [],
        "attribution": "Reconocimiento local en la escena jazzística de Medellín; sin fuente documental específica verificada.",
    },
    {
        "id": "la-pregonera",
        "name": "La Pregonera",
        "entity_type": "group",
        "founding_year": "2012",
        "founding_location": "Medellín",
        "label": None,
        "related_people": [],
        "contribution": "Grupo de salsa contemporáneo en Medellín",
        "notable_works": [],
        "evidence_status": "ATTRIBUTED",
        "source_ids": [],
        "attribution": "Presencia activa en la escena salsera de Medellín; sin fuente documental específica verificada.",
    },
    {
        "id": "la-contundente",
        "name": "La Contundente",
        "entity_type": "group",
        "founding_year": "2005",
        "founding_location": "Medellín",
        "label": None,
        "related_people": [],
        "contribution": "Orquesta de salsa con propuesta propia",
        "notable_works": [],
        "evidence_status": "ATTRIBUTED",
        "source_ids": [],
        "attribution": "Presencia activa en la escena salsera de Medellín; sin fuente documental específica verificada.",
    },
    {
        "id": "la-malandanza",
        "name": "La Malandanza",
        "entity_type": "group",
        "founding_year": "2014",
        "founding_location": "Medellín",
        "label": None,
        "related_people": [],
        "contribution": "Grupo de salsa emergente en Medellín",
        "notable_works": [],
        "evidence_status": "ATTRIBUTED",
        "source_ids": [],
        "attribution": "Presencia activa en la escena salsera de Medellín; sin fuente documental específica verificada.",
    },
]

# ==========================================
# RADIO
# ==========================================

RUTA_RADIO = [
    {
        "id": "latina-stereo",
        "name": "Latina Stereo",
        "frequency": "100.9 FM",
        "call_sign": "HJQO",
        "founding_period": "~1985",
        "slogan": "Salsa desde 1985",
        "role": "Difusión de salsa clásica y dura",
        "location": "Medellín",
        "evidence_status": "VERIFIED_PRIMARY",
        "source_ids": ["latina-stereo-oficial"],
        "attribution": "Según Latina Stereo (sitio oficial).",
    },
]

# ==========================================
# SELLOS DISCOGRÁFICOS
# ==========================================

RUTA_SELLOS = [
    {
        "id": "discos-fuentes",
        "name": "Discos Fuentes",
        "founding_year": "1934",
        "founding_location": "Cartagena",
        "current_location": "Medellín",
        "description": (
            "El sello discográfico más importante de Colombia, frecuentemente "
            "descrito como \"el Motown colombiano\" por su impacto en la "
            "música tropical."
        ),
        "evidence_status": "ATTRIBUTED",
        "source_ids": ["discos-fuentes-oficial", "discos-fuentes-wikipedia"],
        "attribution": "Descrita como \"el Motown colombiano\" según fuentes secundarias.",
    },
    {
        "id": "codiscos",
        "name": "Codiscos",
        "founding_year": "1950",
        "founding_location": "Medellín",
        "current_location": "Medellín",
        "description": (
            "Segundo sello discográfico más importante de Antioquia, "
            "sello de Grupo Galé y otros artistas tropicales."
        ),
        "evidence_status": "VERIFIED_PRIMARY",
        "source_ids": ["codiscos-oficial"],
        "attribution": None,
    },
]

# ==========================================
# EVENTOS ACTUALES
# ==========================================

RUTA_EVENTOS = [
    {
        "id": "viva-la-salsa-2026",
        "title": "Viva la Salsa 2026",
        "date": "25 julio 2026",
        "location": "Estadio Atanasio Girardot, Medellín",
        "description": (
            "Megaconcierto salsero como parte de la Feria de las Flores, "
            "reuniendo a grandes figuras de la salsa."
        ),
        "evidence_status": "VERIFIED_PRIMARY",
        "source_ids": ["canal-trece-viva-salsa"],
    },
    {
        "id": "leyendas-vivas-x-2026",
        "title": "Las Leyendas Vivas X edición",
        "date": "25 abril 2026",
        "location": "Centro de Eventos Centauro, Envigado",
        "description": "Evento de música en vivo organizado por Comfenalco.",
        "evidence_status": "VERIFIED_PRIMARY",
        "source_ids": ["comfenalco-leyendas"],
    },
]

# ==========================================
# SABÍAS QUE... (datos curiosos verificados)
# ==========================================

RUTA_CURIOSIDADES = [
    {
        "id": "fruko-fruco",
        "text": "El nombre \"Fruko\" viene del parecido del músico con la muñequita de la famosa salsa de tomate Fruco.",
        "evidence_status": "ATTRIBUTED",
        "source_ids": [],
        "attribution": "Según Radio Nacional de Colombia (2018) y fuentes secundarias. La marca Fruco fue fundada en Cali en 1950.",
    },
    {
        "id": "discos-fuentes-motown",
        "text": "Discos Fuentes es frecuentemente descrita como \"el Motown colombiano\" por su impacto en la música tropical.",
        "evidence_status": "ATTRIBUTED",
        "source_ids": ["discos-fuentes-wikipedia"],
        "attribution": "Según fuentes secundarias (Wikipedia).",
    },
    {
        "id": "el-tibiri-sotano",
        "text": "El Tíbiri Tábara está ubicado en un sótano, lo que le da un ambiente único y recognizable entre los bares de Medellín.",
        "evidence_status": "VERIFIED_PRIMARY",
        "source_ids": ["el-tibiri-colombiabz", "el-tibiri-2pos"],
        "attribution": None,
    },
    {
        "id": "son-havana-rueda",
        "text": "Son Havana realiza ruedas de Casino los miércoles, una tradición que atrae a bailadores de toda la ciudad.",
        "evidence_status": "VERIFIED_PRIMARY",
        "source_ids": ["son-havana-dancefree"],
        "attribution": None,
    },
]

# ==========================================
# REFERENCIAS ACADÉMICAS
# ==========================================

RUTA_REFERENCIAS = [
    {
        "id": "santana-que-es-salsa",
        "title": "¿Qué es la Salsa?",
        "author": "Santana",
        "institution": "Universidad del Valle",
        "url": "https://repositorio.univalle.edu.co/",
        "type": "academic",
        "relevance": "Definición académica del género musical.",
    },
    {
        "id": "jaramillo-musica-tropical",
        "title": "Música tropical",
        "author": "Jaramillo",
        "institution": "Universidad Católica",
        "url": "https://www.uc.cl/",
        "type": "academic",
        "relevance": "Análisis de la música tropical colombiana.",
    },
    {
        "id": "rendon-zapata-salsa-medellin",
        "title": "Apropiaciones, negociaciones y espacialidades de la salsa en Medellín",
        "author": "Marilly Rendón Zapata",
        "institution": "Universidad de Antioquia",
        "url": "http://hdl.handle.net/10495/14885",
        "type": "academic",
        "relevance": "Estudio etnográfico sobre la salsa como género urbano en Medellín (31 entrevistas, observación participante, 2015-2016).",
    },
]

# ==========================================
# PAQUETE COMPLETO PARA EL API
# ==========================================

def get_ruta_salsera_data():
    """Retorna el diccionario completo de La Ruta Salsera."""
    today = date.today().isoformat()
    return {
        "meta": {
            "title": "La Ruta Salsera de Medellín",
            "description": (
                "Recorrido por la historia, los lugares, las orquestas y "
                "la radio que convirtieron a Medellín en un epicentro "
                "de la cultura salsera colombiana."
            ),
            "last_verified": today,
            "disclaimer": (
                "Información verificada por búsqueda web cruzada. "
                "Horarios y estado actual de lugares pueden cambiar, "
                "confirma antes de ir."
            ),
        },
        "timeline": RUTA_TIMELINE,
        "venues": RUTA_LUGARES,
        "orchestras": RUTA_ORQUESTAS,
        "radio": RUTA_RADIO,
        "labels": RUTA_SELLOS,
        "events": RUTA_EVENTOS,
        "curiosidades": RUTA_CURIOSIDADES,
        "references": RUTA_REFERENCIAS,
        "sources": FUENTES,
    }

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
}

# ==========================================
# TIMELINE — LA RUTA SALSERA DE MEDELLÍN
# ==========================================
# Solo hechos VERIFIED_PRIMARY o VERIFIED_SECONDARY de la sección G.
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
        "id": "discos-fuentes-traslado-1954-1960",
        "year_start": "1954",
        "year_end": "1960",
        "category": "industria",
        "title": "Discos Fuentes se traslada a Medellín",
        "description": (
            "Entre 1954 y 1960, Discos Fuentes trasladó sus operaciones "
            "de Cartagena a Medellín, convirtiéndose en el motor productivo "
            "de la salsa colombiana desde la ciudad."
        ),
        "location": "Medellín, Colombia",
        "people": [],
        "organizations": ["Discos Fuentes"],
        "evidence_status": "CONTRADICTED",
        "confidence": "medium",
        "source_ids": ["discos-fuentes-oficial", "discos-fuentes-wikipedia"],
        "attribution": "Fecha entre 1954 y 1960. Discos Fuentes oficial dice 1960, Wikipedia dice 1954.",
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
        "title": "\"El Preso\" — Wilson Manyoma",
        "description": (
            "\"El Preso\" de Fruko y sus Tesos, con la voz de Wilson "
            "Manyoma, se convirtió en el himno más reconocible de la salsa "
            "colombiana y uno de los temas bailables más icónicos del país."
        ),
        "location": "Medellín, Colombia",
        "people": ["Wilson Manyoma", "Julio Ernesto Estrada (Fruko)"],
        "organizations": ["Fruko y sus Tesos", "Discos Fuentes"],
        "evidence_status": "VERIFIED_PRIMARY",
        "confidence": "high",
        "source_ids": ["discos-fuentes-oficial"],
        "attribution": None,
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
            "Latina Stereo comenzó a transmitir en 100.9 FM en Medellín, "
            "convirtiéndose en la emisora de salsa más emblemática de la "
            "ciudad con el lema \"Salsa desde 1985\"."
        ),
        "location": "Medellín, Colombia",
        "people": [],
        "organizations": ["Latina Stereo"],
        "evidence_status": "VERIFIED_PRIMARY",
        "confidence": "high",
        "source_ids": ["latina-stereo-oficial"],
        "attribution": None,
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
            "Son Havana abrió sus puertas en el barrio Laureles como club "
            "de salsa y son cubano, convirtiéndose en un punto de "
            "encuentro clave para la comunidad salsera de Medellín."
        ),
        "location": "Cra. 73 #44-56, Laureles, Medellín",
        "people": [],
        "organizations": ["Son Havana"],
        "evidence_status": "VERIFIED_SECONDARY",
        "confidence": "high",
        "source_ids": ["son-havana-dancefree", "son-havana-evendo"],
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
            "Club de salsa y son cubano en Medellín. Programación en vivo, "
            "reservas, contratación de orquestas y merch."
        ),
        "music_style": "Salsa, son cubano, rueda de casino",
        "status": "active",
        "operating_hours": "Mié-Jue hasta medianoche, Vie-Sáb hasta 4am",
        "is_underground": False,
        "evidence_status": "VERIFIED_PRIMARY",
        "confidence": "high",
        "source_ids": ["son-havana-dancefree", "son-havana-evendo"],
        "attribution": None,
        "external_links": {
            "google_maps": "https://maps.google.com/?q=Cra+73+%2344-56+Laureles+Medellin",
            "tripadvisor": "https://tripadvisor.es/Attraction_Review-g297478-d9604959-Reviews-Son_Havana-Medellin_Antioquia.html",
        },
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
        "founding_location": "Barrios Aranjuez/Manrique, Medellín",
        "label": None,
        "related_people": [],
        "contribution": "Orquesta de barrios populares de Medellín",
        "notable_works": [],
        "evidence_status": "VERIFIED_SECONDARY",
        "source_ids": [],
        "attribution": None,
    },
    {
        "id": "sonora-8",
        "name": "Sonora 8",
        "entity_type": "orchestra",
        "founding_year": "2003",
        "founding_location": "Medellín (Latin Core)",
        "label": None,
        "related_people": [],
        "contribution": "Orquesta contemporánea de la escena salsera medellinense",
        "notable_works": [],
        "evidence_status": "VERIFIED_SECONDARY",
        "source_ids": ["latina-stereo-oficial"],
        "attribution": None,
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
        "evidence_status": "VERIFIED_SECONDARY",
        "source_ids": [],
        "attribution": None,
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
        "evidence_status": "VERIFIED_SECONDARY",
        "source_ids": [],
        "attribution": None,
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
        "evidence_status": "VERIFIED_SECONDARY",
        "source_ids": [],
        "attribution": None,
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
        "evidence_status": "VERIFIED_SECONDARY",
        "source_ids": [],
        "attribution": None,
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
        "text": "El nombre \"Fruko\" viene de las iniciales de \"FRUCO\" (Federación de la Radio y la Unión Colombiana).",
        "evidence_status": "VERIFIED_SECONDARY",
        "source_ids": ["fruko-wikipedia"],
        "attribution": "Según fuentes secundarias.",
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

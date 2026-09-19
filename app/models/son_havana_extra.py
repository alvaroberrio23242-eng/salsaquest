# app/models/son_havana_extra.py
"""
Datos adicionales de Son Havana: galería de fotos y enlaces externos.

Fuente aislada — NO se importa desde content_data.py ni desde
ruta_salsera_data.py. Solo la consume /api/son-havana-extra
y la página /son-havana via content.js.

Reglas:
- NO incluir fotos con people_identifiable=True sin consentimiento confirmado.
- NO inventar URLs — dejar url="" para que el autor las complete.
- NO incluir calificaciones numéricas de terceros.
"""

SON_HAVANA_EXTRA = {
    "photos": [
        # EJEMPLO — reemplazar con fotos reales del autor
        # {
        #     "id": "sh-ext-001",
        #     "file": "img/lugares/son-havana/ext-001.webp",
        #     "category": "actual",
        #     "date_taken": "2026",
        #     "date_confidence": "aprox",
        #     "credit": {
        #         "author": "Nombre del fotógrafo",
        #         "source_url": "",
        #         "license": "CC BY 4.0",
        #         "license_url": "https://creativecommons.org/licenses/by/4.0/",
        #     },
        #     "alt": {"es": "Fachada de Son Havana de noche"},
        #     "caption": {"es": "Vista exterior del local en Laureles"},
        #     "people_identifiable": False,
        # },
        # {
        #     "id": "sh-ext-002",
        #     "file": "img/lugares/son-havana/ext-002.webp",
        #     "category": "historica",
        #     "date_taken": "2015",
        #     "date_confidence": "aprox",
        #     "credit": {
        #         "author": "",
        #         "source_url": "",
        #         "license": "",
        #         "license_url": "",
        #     },
        #     "alt": {"es": "Interior de Son Havana con bailadores"},
        #     "caption": {"es": "Rueda de Casino en el club"},
        #     "people_identifiable": True,
        # },
    ],
    "external_links": [
        # {
        #     "id": "sh-ta-001",
        #     "kind": "visitor_opinion",
        #     "platform": "tripadvisor",
        #     "url": "",  # TODO: autor debe completar con la URL real verificada
        #     "label": {"es": "Ver opiniones en Tripadvisor"},
        # },
        # {
        #     "id": "sh-gm-001",
        #     "kind": "visitor_opinion",
        #     "platform": "google_maps",
        #     "url": "",  # TODO: autor debe completar
        #     "label": {"es": "Ver opiniones en Google Maps"},
        # },
        # {
        #     "id": "sh-wl-001",
        #     "kind": "aggregator",
        #     "platform": "wanderlog",
        #     "url": "",  # TODO: autor debe completar
        #     "label": {"es": "Ver en Wanderlog"},
        # },
        # {
        #     "id": "sh-ig-001",
        #     "kind": "official",
        #     "platform": "instagram",
        #     "url": "",  # TODO: autor debe completar
        #     "label": {"es": "Instagram oficial"},
        # },
    ],
}

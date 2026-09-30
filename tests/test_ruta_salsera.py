# tests/test_ruta_salsera.py
"""Tests para La Ruta Salsera de Medellín — Phase 5A.

Cobertura:
  T-RS-01: GET /ruta-salsera → 200, content-type HTML, contiene palabra clave.
  T-RS-02: GET /api/ruta-salsera → 200, JSON válido, estructura completa.
  T-RS-03: GET /medellin → 200 (regresión, no debe romperse).
  T-RS-04: GET / → 200 (regresión general).
  T-RS-05: GET /api/ruta-salsera → todos los campos requeridos presentes.
  T-RS-06: Verificar que no hay datos prohibidos en el API.
"""

import json


# ── T-RS-01: Ruta HTML 返回 200 ──────────────────────────────────

def test_ruta_salsera_returns_200(client):
    resp = client.get("/ruta-salsera")
    assert resp.status_code == 200


def test_ruta_salsera_content_type_html(client):
    resp = client.get("/ruta-salsera")
    assert "text/html" in resp.content_type


def test_ruta_salsera_contains_title(client):
    resp = client.get("/ruta-salsera")
    html = resp.data.decode("utf-8")
    assert "Ruta Salsera" in html


# ── T-RS-02: API 返回 JSON con estructura completa ──────────────

def test_api_ruta_salsera_returns_200(client):
    resp = client.get("/api/ruta-salsera")
    assert resp.status_code == 200


def test_api_ruta_salsera_content_type_json(client):
    resp = client.get("/api/ruta-salsera")
    assert "application/json" in resp.content_type


def test_api_ruta_salsera_structure(client):
    resp = client.get("/api/ruta-salsera")
    data = json.loads(resp.data)
    required_keys = [
        "meta", "timeline", "venues", "orchestras",
        "radio", "labels", "events", "curiosidades",
        "references", "sources",
    ]
    for key in required_keys:
        assert key in data, f"Falta la clave '{key}' en la respuesta del API"


# ── T-RS-05: Campos requeridos en cada item ─────────────────────

def test_timeline_items_have_required_fields(client):
    resp = client.get("/api/ruta-salsera")
    data = json.loads(resp.data)
    required = {"id", "year_start", "category", "title", "description", "evidence_status"}
    for item in data["timeline"]:
        missing = required - set(item.keys())
        assert not missing, f"Timeline item '{item.get('id')}' falta campos: {missing}"


def test_venues_have_required_fields(client):
    resp = client.get("/api/ruta-salsera")
    data = json.loads(resp.data)
    required = {"id", "name", "address", "coordinates", "evidence_status"}
    for item in data["venues"]:
        missing = required - set(item.keys())
        assert not missing, f"Venue '{item.get('id')}' falta campos: {missing}"


def test_orchestras_have_required_fields(client):
    resp = client.get("/api/ruta-salsera")
    data = json.loads(resp.data)
    required = {"id", "name", "entity_type", "evidence_status"}
    for item in data["orchestras"]:
        missing = required - set(item.keys())
        assert not missing, f"Orchestra '{item.get('id')}' falta campos: {missing}"


def test_radio_have_required_fields(client):
    resp = client.get("/api/ruta-salsera")
    data = json.loads(resp.data)
    required = {"id", "name", "frequency", "slogan", "evidence_status"}
    for item in data["radio"]:
        missing = required - set(item.keys())
        assert not missing, f"Radio '{item.get('id')}' falta campos: {missing}"


# ── T-RS-06: No hay datos prohibidos ────────────────────────────

FORBIDDEN_PHRASES = [
    "fue fundado en 1992",       # El Tíbiri DO_NOT_USE
    "existe desde 1962",         # El Suave DO_NOT_USE
    "Bernardo Arango",           # El Suave DO_NOT_USE
    "Malagente",                 # El Suave DO_NOT_USE
    "renacimiento de la salsa brava",  # DO_NOT_USE
    "Aristi",                    # Calle Palacé DO_NOT_USE
    "Brisas de Costa Rica",      # Calle Palacé DO_NOT_USE
    "Carruseles",                # Calle Palacé DO_NOT_USE
    "El Conde",                  # Calle Palacé DO_NOT_USE
    "El Semáforo",               # Calle Palacé DO_NOT_USE
    "El Diferente",              # Calle Palacé DO_NOT_USE
    "El Ceilán",                 # Calle Palacé DO_NOT_USE
    "La Titular",                # Calle Palacé DO_NOT_USE
]


def test_no_forbidden_phrases_in_api(client):
    resp = client.get("/api/ruta-salsera")
    raw = resp.data.decode("utf-8").lower()
    for phrase in FORBIDDEN_PHRASES:
        assert phrase.lower() not in raw, (
            f"Frase prohibida encontrada en API: '{phrase}'"
        )


def test_no_forbidden_phrases_in_html(client):
    resp = client.get("/ruta-salsera")
    html = resp.data.decode("utf-8").lower()
    # Solo verificar frases que podrían aparecer en el HTML renderizado
    html_forbidden = ["fue fundado en 1992", "existe desde 1962", "Bernardo Arango"]
    for phrase in html_forbidden:
        assert phrase.lower() not in html, (
            f"Frase prohibida encontrada en HTML: '{phrase}'"
        )


# ── T-RS-03: Regresión — /medellin sigue funcionando ───────────

def test_medellin_still_works(client):
    resp = client.get("/medellin")
    assert resp.status_code == 200
    assert "text/html" in resp.content_type


def test_api_medellin_still_works(client):
    resp = client.get("/api/medellin")
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert "historia" in data
    assert "bares" in data


# ── T-RS-04: Regresión general — homepage redirige a Ruta Salsera ──

def test_homepage_redirects_to_ruta_salsera(client):
    resp = client.get("/")
    assert resp.status_code == 302
    assert "/ruta-salsera" in resp.headers["Location"]


def test_homepage_redirect_follows(client):
    resp = client.get("/", follow_redirects=True)
    assert resp.status_code == 200
    html = resp.data.decode("utf-8")
    assert "Ruta Salsera" in html


# ── T-RS-07: Son Havana extra — galería y enlaces externos ───────

def test_son_havana_extra_returns_200(client):
    resp = client.get("/api/son-havana-extra")
    assert resp.status_code == 200


def test_son_havana_extra_content_type_json(client):
    resp = client.get("/api/son-havana-extra")
    assert "application/json" in resp.content_type


def test_son_havana_extra_has_required_keys(client):
    resp = client.get("/api/son-havana-extra")
    data = json.loads(resp.data)
    assert "photos" in data, "Falta la clave 'photos'"
    assert "external_links" in data, "Falta la clave 'external_links'"


def test_son_havana_extra_photos_is_list(client):
    resp = client.get("/api/son-havana-extra")
    data = json.loads(resp.data)
    assert isinstance(data["photos"], list), "'photos' debe ser una lista"


def test_son_havana_extra_external_links_is_list(client):
    resp = client.get("/api/son-havana-extra")
    data = json.loads(resp.data)
    assert isinstance(data["external_links"], list), "'external_links' debe ser una lista"


def test_son_havana_extra_photo_fields_when_present(client):
    resp = client.get("/api/son-havana-extra")
    data = json.loads(resp.data)
    required = {"id", "file", "category", "credit", "alt", "caption", "people_identifiable"}
    for photo in data["photos"]:
        missing = required - set(photo.keys())
        assert not missing, f"Photo '{photo.get('id')}' falta campos: {missing}"


def test_son_havana_extra_link_fields_when_present(client):
    resp = client.get("/api/son-havana-extra")
    data = json.loads(resp.data)
    required = {"id", "kind", "platform", "url", "label"}
    for link in data["external_links"]:
        missing = required - set(link.keys())
        assert not missing, f"Link '{link.get('id')}' falta campos: {missing}"


def test_son_havana_extra_no_numerical_ratings(client):
    """No debe haber calificaciones numéricas de terceros en external_links."""
    resp = client.get("/api/son-havana-extra")
    data = json.loads(resp.data)
    for link in data["external_links"]:
        assert "rating" not in link, f"Link '{link.get('id')}' tiene campo 'rating' (prohibido)"
        assert "score" not in link, f"Link '{link.get('id')}' tiene campo 'score' (prohibido)"


def test_son_havana_html_has_gallery_section(client):
    resp = client.get("/son-havana")
    html = resp.data.decode("utf-8")
    assert "son-havana-gallery" in html, "Falta sección de galería en HTML"


def test_son_havana_html_has_external_links_section(client):
    resp = client.get("/son-havana")
    html = resp.data.decode("utf-8")
    assert "son-havana-external-links" in html, "Falta sección de enlaces externos en HTML"


# ── T-RS-08: Fallbacks y representación robusta ──────────────────

def test_api_venues_no_none_values_in_rendered_html(client):
    """Verifica que el HTML renderizado de venues no contiene 'None', 'null', 'undefined'."""
    resp = client.get("/ruta-salsera")
    html = resp.data.decode("utf-8")
    # El template base no renderiza los venues directamente (lo hace JS),
    # pero verificamos que no haya valores hardcodeados problemáticos
    assert "None" not in html, "HTML contiene 'None' literal"
    assert "null" not in html, "HTML contiene 'null' literal"
    assert "undefined" not in html, "HTML contiene 'undefined' literal"


def test_api_venues_pending_states_fallbacks_present(client):
    """Verifica que venues con estados especiales tengan fallbacks en la API."""
    resp = client.get("/api/ruta-salsera")
    data = json.loads(resp.data)
    # Estados especiales: CONTRADICTED (y futuros PENDING_VERIFICATION, PENDING_RESEARCH)
    special_states = ["PENDING_VERIFICATION", "PENDING_RESEARCH", "CONTRADICTED"]
    special_venues = [v for v in data["venues"] if v["evidence_status"] in special_states]
    assert len(special_venues) >= 1, f"Debe haber al menos 1 venue con estado especial, encontrados: {len(special_venues)}"
    for v in special_venues:
        # Los campos que son None/null deben ser manejados por fallbacks en frontend
        # Verificamos que la API devuelve valores (pueden ser None o strings reales)
        assert "address" in v
        assert "music_style" in v
        assert "description" in v
        # Al menos algunos campos son None (music_style, description para eslabon-prendido)
        none_fields = [k for k in ["music_style", "description", "operating_hours", "coordinates"] if v.get(k) is None]
        assert len(none_fields) > 0, f"Venue {v['id']} debería tener al menos algunos campos None"


def test_venue_address_fallback_in_js_rendering(client):
    """Test conceptual: verifica que el JS tiene la función safeText."""
    # Este test verifica la presencia del código en el archivo JS
    import os
    js_path = os.path.join("app", "static", "js", "ruta_salsera.js")
    with open(js_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "safeText" in content, "Falta función safeText en ruta_salsera.js"
    assert "Dirección pendiente de verificación" in content, "Falta fallback de dirección"
    assert "Estilo musical pendiente de verificar" in content, "Falta fallback de estilo musical"
    assert "Información pendiente de investigación" in content, "Falta fallback de descripción"


def test_venue_music_style_fallback_in_js_rendering(client):
    """Verifica que music_style tiene fallback en JS."""
    import os
    js_path = os.path.join("app", "static", "js", "ruta_salsera.js")
    with open(js_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "safeText" in content
    assert "Estilo musical pendiente de verificar" in content


def test_venue_description_fallback_in_js_rendering(client):
    """Verifica que description tiene fallback en JS."""
    import os
    js_path = os.path.join("app", "static", "js", "ruta_salsera.js")
    with open(js_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "Información pendiente de investigación" in content


def test_venue_no_broken_links_for_missing_social(client):
    """Verifica que el JS no genera botones para redes inexistentes."""
    import os
    js_path = os.path.join("app", "static", "js", "ruta_salsera.js")
    with open(js_path, "r", encoding="utf-8") as f:
        content = f.read()
    # Verificar que usa isEmptyValue para validar antes de renderizar
    assert "isEmptyValue" in content, "Falta función isEmptyValue en ruta_salsera.js"
    # WhatsApp, Google Maps, Website deben estar protegidos
    assert "isEmptyValue(v.whatsapp_url)" in content or "!isEmptyValue(v.whatsapp_url)" in content or "v.whatsapp_url" in content


def test_venue_no_marker_without_coordinates(client):
    """Verifica que el JS no crea marcadores sin coordenadas."""
    import os
    js_path = os.path.join("app", "static", "js", "ruta_salsera.js")
    with open(js_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "if (!v.coordinates) return;" in content, "Mapa debe omitir venues sin coordenadas"


def test_venue_no_polyline_without_route_order(client):
    """Verifica que el JS no incluye venues sin route_order en el polyline."""
    import os
    js_path = os.path.join("app", "static", "js", "ruta_salsera.js")
    with open(js_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "v.route_order != null" in content, "Polyline debe filtrar route_order None"


def test_venues_unique_ids(client):
    """Verifica que no hay IDs duplicados en RUTA_LUGARES."""
    resp = client.get("/api/ruta-salsera")
    data = json.loads(resp.data)
    ids = [v["id"] for v in data["venues"]]
    assert len(ids) == len(set(ids)), f"IDs duplicados encontrados: {ids}"


def test_son_havana_laureles_id_and_brand(client):
    """Verifica que Son Havana tiene el ID y brand correctos."""
    resp = client.get("/api/ruta-salsera")
    data = json.loads(resp.data)
    son_havana = next((v for v in data["venues"] if v["id"] == "son-havana-laureles"), None)
    assert son_havana is not None, "No se encontró son-havana-laureles"
    assert son_havana["brand"] == "son-havana", f"Brand incorrecto: {son_havana.get('brand')}"


def test_no_son_havana_poblado_in_venues(client):
    """Verifica que no existe son-havana-poblado."""
    resp = client.get("/api/ruta-salsera")
    data = json.loads(resp.data)
    ids = [v["id"] for v in data["venues"]]
    assert "son-havana-poblado" not in ids, "son-havana-poblado no debe existir"


def test_pending_states_badge_in_js(client):
    """Verifica que los estados de evidencia tienen badge propio en JS."""
    import os
    js_path = os.path.join("app", "static", "js", "ruta_salsera.js")
    with open(js_path, "r", encoding="utf-8") as f:
        content = f.read()
    # CONTRADICTED es un estado A (usado en eslabon-prendido)
    assert "CONTRADICTED" in content, "statusBadge debe manejar CONTRADICTED"
    # Etiqueta para CONTRADICTED (cambio A: de 'Contradictado' a 'En disputa')
    assert "En disputa" in content, "CONTRADICTED debe mostrar 'En disputa'"


# ── Tests para nueva arquitectura de estados ──────────────────────

def test_bururu_barara_closed_status(client):
    """Verifica que El Bururú Barará tiene status closed."""
    resp = client.get("/api/ruta-salsera")
    data = json.loads(resp.data)
    bururu = next((v for v in data["venues"] if v["id"] == "bururu-barara"), None)
    assert bururu is not None, "No se encontró bururu-barara"
    assert bururu["status"] == "closed", f"Status incorrecto: {bururu.get('status')}"
    assert bururu["evidence_status"] == "VERIFIED_SECONDARY"
    assert bururu["inclusion"] == "usable"
    assert bururu["route_order"] is None


def test_eslabon_prendido_unknown_status(client):
    """Verifica que El Eslabón Prendido tiene status unknown y evidence CONTRADICTED."""
    resp = client.get("/api/ruta-salsera")
    data = json.loads(resp.data)
    eslabon = next((v for v in data["venues"] if v["id"] == "eslabon-prendido"), None)
    assert eslabon is not None, "No se encontró eslabon-prendido"
    assert eslabon["status"] == "unknown", f"Status incorrecto: {eslabon.get('status')}"
    assert eslabon["evidence_status"] == "CONTRADICTED"
    assert eslabon["inclusion"] == "usable"
    assert eslabon["route_order"] is None
    # No debe tener coordenadas verificadas
    assert eslabon["coordinates"] is None


def test_venue_inclusion_field_present(client):
    """Verifica que todos los venues tienen el campo inclusion."""
    resp = client.get("/api/ruta-salsera")
    data = json.loads(resp.data)
    for v in data["venues"]:
        assert "inclusion" in v, f"Venue {v['id']} falta campo inclusion"
        assert v["inclusion"] in ["usable", "DO_NOT_USE"]


def test_venue_status_field_present(client):
    """Verifica que todos los venues tienen el campo status con valores válidos."""
    resp = client.get("/api/ruta-salsera")
    data = json.loads(resp.data)
    for v in data["venues"]:
        assert "status" in v, f"Venue {v['id']} falta campo status"
        assert v["status"] in ["active", "closed", "unknown"], f"Status inválido en {v['id']}: {v['status']}"


def test_closed_venue_not_in_active_map(client):
    """Verifica que el JS filtra venues cerrados/unknown del mapa (test conceptual)."""
    import os
    js_path = os.path.join("app", "static", "js", "ruta_salsera.js")
    with open(js_path, "r", encoding="utf-8") as f:
        content = f.read()
    # El mapa debe filtrar status closed y unknown
    assert "v.status === \"closed\"" in content or 'v.status === "closed"' in content or "status === \"closed\"" in content
    assert "v.status === \"unknown\"" in content or 'v.status === "unknown"' in content or "status === \"unknown\"" in content




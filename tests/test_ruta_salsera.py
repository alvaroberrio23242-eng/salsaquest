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

# ROUTE-SALSERA-IMPLEMENTATION-PLAN.md
## Plan de Implementación Técnica — La Ruta Salsera de Medellín
### SalsaQuest — Fase 4

**Fecha de planificación:** 18 septiembre 2026
**Arquitecto técnico:** OpenCode (mimo-v2.5-free)
**Documento de autoridad:** `ROUTE-SALSERA-PRODUCT-SPEC.md` → `ROUTE-SALSERA-EVIDENCE-AUDIT.md`

---

## 1. EXECUTIVE SUMMARY

Este documento define la implementación técnica de **La Ruta Salsera de Medellín** dentro de SalsaQuest. Cada decisión está rastreable desde la evidencia auditada hasta el componente técnico.

**Estado actual:** SalsaQuest es una app Flask multipágina con 19 templates, 4 blueprints, datos estáticos en Python dicts, y frontend Bootstrap 5 + Leaflet + FontAwesome.

**Decisión arquitectónica clave:** La Ruta Salsera es una **página nueva** (`/ruta-salsera`) con su propio template, datos, JS y CSS. NO modifica la sección `/medellin` existente. Reutiliza infraestructura existente (base.html, Leaflet, Bootstrap, FontAwesome) y sigue los patrones ya establecidos (Python dicts → API JSON → client-side rendering).

**Archivos a crear:** 4 (template, data, JS, CSS)
**Archivos a modificar:** 3 (main.py route, content.py API, navbar base.html)
**Archivos NO tocados:** Todos los demás (medellin.html, content_data.py existente, timeline.js, content.js, etc.)

---

## 2. CURRENT ARCHITECTURE

### Repository

```
D:\Proyectos\sonhavanagame
├── app/
│   ├── __init__.py          (app factory: crear_app())
│   ├── routes/
│   │   ├── main.py           (13 rutas multipágina)
│   │   ├── content.py        (15 endpoints /api/*)
│   │   ├── timeline.py       (/api/timeline)
│   │   └── auth.py           (auth + leaderboard)
│   ├── models/
│   │   ├── content_data.py   (1463 líneas, todos los datos estáticos)
│   │   ├── timeline_events_data.py
│   │   ├── timeline_data.py
│   │   ├── user.py
│   │   └── visit_counter.py
│   ├── templates/
│   │   ├── base.html         (navbar, footer, modales, scripts globales)
│   │   ├── medellin.html     (sección Medellín existente)
│   │   └── ... (17 templates más)
│   └── static/
│       ├── css/
│       │   ├── style.css     (468 líneas, variables, cards, timeline, forms)
│       │   └── fase1-diseno.css (237 líneas, glassmorphism, neon, responsive)
│       ├── js/
│       │   ├── content.js    (672 líneas, carga de contenido + Medellín)
│       │   ├── timeline.js   (331 líneas, timeline + quiz + leaderboard)
│       │   ├── scroll-reveal.js
│       │   ├── video-bg.js
│       │   ├── cursor-interactivo.js
│       │   └── trivia.js
│       └── videos/
└── sonhavana.db
```

### Backend Pattern

- **App factory:** `crear_app()` en `__init__.py`
- **Blueprints:** 4 (main, content, timeline, auth)
- **Rutas páginas:** `main_bp` → `render_template()` con `active_page` para navbar
- **API endpoints:** `content_bp` → `jsonify(dict)` (datos estáticos de Python)
- **Datos:** Todos en `content_data.py` como listas/diccionarios Python
- **DB:** SQLite solo para timeline events y users (NO para contenido editorial)

### Frontend Pattern

- **Template base:** `base.html` con navbar, footer, modales, scripts globales
- **Templates hijos:** `{% extends "base.html" %}` + `{% block content %}`
- **CSS:** 2 archivos (style.css + fase1-diseno.css), variables CSS, Bootstrap 5
- **JS:** Client-side rendering via `fetch('/api/...')` → DOM manipulation
- **Leaflet:** Cargado en todas las páginas (base.html), validación `typeof L !== 'undefined'`
- **Imágenes:** Patrón `imgFicha()` con fallback a `ficha-placeholder.svg`

### Data Pattern

```python
# content_data.py
DATOS = [
    {
        "id": "slug-unico",
        "nombre": "Nombre",
        "campo": "valor",
        "imagen_url": "https://...",
        "imagen_credito": {"autor": "...", "licencia": "...", "fuente_url": "..."},
    },
]

# content.py
@content_bp.route('/api/datos', methods=['GET'])
def get_datos():
    return jsonify(DATOS)
```

---

## 3. ARCHITECTURE GATE

### Proyecto

| Campo | Valor |
|-------|-------|
| Ruta raíz | `D:\Proyectos\sonhavanagame` |
| Framework | Flask (Python) |
| Entrypoint | `app/__init__.py` → `crear_app()` |
| Estructura | Multipágina (19 templates) |
| Entorno | Windows, Git Bash, Python |
| URL local | `http://127.0.0.1:5000` |

### Backend

| Componente | Estado |
|------------|--------|
| App factory | `crear_app()` en `__init__.py` |
| Blueprints | 4: main, content, timeline, auth |
| Rutas páginas | En `main.py` (13 rutas) |
| APIs | En `content.py` (15 endpoints) |
| Modelos | `content_data.py` (datos), `timeline_data.py` (BD) |
| Config | `SECRET_KEY` obligatoria, SQLite para timeline/users |

### Frontend

| Componente | Estado |
|------------|--------|
| Templates | 19, todos extienden `base.html` |
| CSS | `style.css` (468L) + `fase1-diseno.css` (237L) |
| JS | 6 archivos, cargados en TODAS las páginas via `base.html` |
| Leaflet | v1.9.4, ya cargado (CSS + JS) |
| Bootstrap | v5.3.0, ya cargado |
| FontAwesome | v6.4.0, ya cargado |

### Datos

| Tipo | Implementación |
|------|----------------|
| Contenido editorial | Python dicts en `content_data.py` |
| Timeline events | SQLAlchemy + `timeline_events_data.py` |
| Users | SQLAlchemy + `user.py` |
| Visit counter | Clase estática `VisitCounter` |

---

## 4. REPOSITORY CONFIRMATION

```
D:\Proyectos\sonhavanagame
```

**Confirmado como proyecto objetivo.**

- La app corre con `python run.py` (o similar)
- La DB es SQLite (`sonhavana.db`)
- `/medellin` existe como ruta en `main.py` línea 51-53
- `/ruta-salsera` NO existe actualmente
- No hay contenido de "ruta salsera" en ningún archivo

---

## 5. EXISTING `/MEDDELLIN` ANALYSIS

### Componentes actuales

| Componente | Archivo | Función |
|------------|---------|---------|
| Ruta Flask | `main.py:51-53` | `@main_bp.route('/medellin')` → template |
| Template | `medellin.html` (38 líneas) | Extiende `base.html`, 5 secciones |
| API | `content.py:77-87` | `/api/medellin` → JSON |
| Datos | `content_data.py:1156-1307` | `MEDELLIN_HISTORIA`, `MEDELLIN_BARES`, etc. |
| JS | `content.js:615-672` | `cargarMedellin()` + `cargarSonHavana()` |
| Mapa | `content.js:658-667` | Leaflet markers en `#mapa-medellin` |

### Datos actuales en `/api/medellin`

- `historia`: Texto descriptivo (1 párrafo)
- `bares`: 5 lugares (Son Havana, El Tíbiri, El Suave, Eslabón Prendido, Bururú Barará)
- `emisoras`: 4 emisoras
- `eventos`: 2 eventos
- `playlist_url`: Spotify search link
- `pendiente`: 4 items pendientes

### ¿Debe permanecer intacta?

**SÍ.** La sección `/medellin` es funcional, tiene datos propios, y sirve un propósito diferente (vista general de Medellín). No se modifica.

### ¿Reutiliza componentes de `/medellin`?

**NO directamente.** La Ruta Salsera tiene su propia arquitectura de datos (con `evidence_status`, `sources`, etc.) que `/medellin` no tiene. Sin embargo, reutiliza:
- Patrón de tarjetas (`card-glass`)
- Patrón de mapa (Leaflet)
- Patrón de API (fetch → JSON → DOM)
- Patrón de CSS (variables, glassmorphism)

### ¿Hay riesgo de acoplamiento?

**BAJO.** La Ruta es una página independiente. No comparte datos ni lógica con `/medellin`. El único punto de contacto potencial es el navbar (agregar enlace), que es un cambio mínimo en `base.html`.

### Decisión

**Crear `/ruta-salsera` como nueva experiencia.** `/medellin` permanece intacta.

---

## 6. TARGET ARCHITECTURE

### Decisión: Reutilizar patrón existente, no crear abstracciones nuevas

La Product Spec propone:

```
templates/ruta_salsera.html
routes/main.py o routes/ruta_salsera.py
models/ruta_salsera_data.py
/api/ruta-salsera
static/js/ruta_salsera.js
static/css/ruta_salsera.css
```

**Evaluación de la propuesta vs realidad:**

| Opción | Pros | Contras | Decisión |
|--------|------|---------|----------|
| Nuevo blueprint `routes/ruta_salsera.py` | Modularidad, separación | Archivo pequeño (~20 líneas), over-engineering | **NO** — agregar a `main.py` |
| Nuevo archivo `models/ruta_salsera_data.py` | Separación de datos | `content_data.py` ya tiene 1463L, agregar 300L más es razonable | **CREAR** — separar por claridad |
| Nuevo JS `static/js/ruta_salsera.js` | Modularidad | Los JS se cargan en TODAS las páginas (base.html), JS específico en `{% block extra_js %}` | **CREAR** — solo se carga en esta página |
| Nuevo CSS `static/css/ruta_salsera.css` | Separación | fase1-diseno.css ya maneja estilos específicos | **CREAR** — en `{% block extra_css %}` |
| API `/api/ruta-salsera` | Patrón existente | Patrón probado en content.py | **SÍ** — en content.py |

### Arquitectura final decidida

```
ARCHIVOS A CREAR:
  app/templates/ruta_salsera.html        (template)
  app/models/ruta_salsera_data.py        (datos con evidence)
  app/static/js/ruta_salsera.js          (interacciones)
  app/static/css/ruta_salsera.css        (estilos específicos)

ARCHIVOS A MODIFICAR:
  app/routes/main.py                      (+1 ruta)
  app/routes/content.py                   (+1 endpoint API)
  app/templates/base.html                 (+1 enlace navbar)

ARCHIVOS NO TOCADOS:
  app/routes/auth.py
  app/routes/timeline.py
  app/models/content_data.py
  app/models/timeline_events_data.py
  app/templates/medellin.html
  app/templates/son_havana.html
  app/static/js/content.js
  app/static/js/timeline.js
  app/static/css/style.css
  app/static/css/fase1-diseno.css
  app/__init__.py
  sonhavana.db
```

---

## 7. FILE-BY-FILE PLAN

### ARCHIVOS A CREAR

| Archivo | Acción | Propósito | Riesgo | Dependencias |
|---------|--------|-----------|--------|--------------|
| `app/models/ruta_salsera_data.py` | CREATE | Datos de la Ruta con evidence_status | Bajo | Ninguna |
| `app/templates/ruta_salsera.html` | CREATE | Template principal de la Ruta | Bajo | base.html |
| `app/static/js/ruta_salsera.js` | CREATE | Interacciones específicas (timeline, mapa, cards) | Bajo | Leaflet, DOM |
| `app/static/css/ruta_salsera.css` | CREATE | Estilos específicos de la Ruta | Bajo | style.css variables |

### ARCHIVOS A MODIFICAR

| Archivo | Acción | Cambio | Riesgo | Dependencias |
|---------|--------|--------|--------|--------------|
| `app/routes/main.py` | MODIFY | +1 ruta `@main_bp.route('/ruta-salsera')` | Muy bajo | ruta_salsera.html |
| `app/routes/content.py` | MODIFY | +1 endpoint `/api/ruta-salsera` | Muy bajo | ruta_salsera_data.py |
| `app/templates/base.html` | MODIFY | +1 enlace en navbar dropdown "Lugares" | Bajo | main.py (ruta nueva) |

### ARCHIVOS NO TOCADOS

| Archivo | Razón |
|---------|-------|
| `app/__init__.py` | No se agregan blueprints nuevos |
| `app/routes/auth.py` | Sin relación |
| `app/routes/timeline.py` | Sin relación |
| `app/models/content_data.py` | Datos existentes preservados |
| `app/models/timeline_events_data.py` | Sin relación |
| `app/models/user.py` | Sin relación |
| `app/models/visit_counter.py` | Sin relación |
| `app/templates/medellin.html` | Se preserva intacta |
| `app/templates/son_havana.html` | Se preserva intacta |
| `app/templates/inicio.html` | Sin cambios |
| `app/templates/base.html` | Solo +1 enlace navbar (cambio mínimo) |
| `app/static/js/content.js` | Sin cambios |
| `app/static/js/timeline.js` | Sin cambios |
| `app/static/js/scroll-reveal.js` | Sin cambios |
| `app/static/js/video-bg.js` | Sin cambios |
| `app/static/js/cursor-interactivo.js` | Sin cambios |
| `app/static/css/style.css` | Sin cambios |
| `app/static/css/fase1-diseno.css` | Sin cambios |
| `sonhavana.db` | Sin cambios |

---

## 8. DATA ARCHITECTURE

### Decisión: Python dicts en módulo separado

Los datos de la Ruta Salsera van en `app/models/ruta_salsera_data.py`, siguiendo el patrón de `content_data.py`. Cada entrada incluye `evidence_status` y `sources` como campos nuevos (no existentes en el sistema actual).

### Estructura del archivo

```python
# app/models/ruta_salsera_data.py
"""
Datos estáticos para La Ruta Salsera de Medellín.
Cada entrada incluye evidence_status y sources para trazabilidad.
Patrón: mismo que content_data.py (Python dicts → API JSON → client-side)
"""

# ==========================================
# CONSTANTES DE EVIDENCIA
# ==========================================
EVIDENCE_VERIFIED_PRIMARY = "VERIFIED_PRIMARY"
EVIDENCE_VERIFIED_SECONDARY = "VERIFIED_SECONDARY"
EVIDENCE_ATTRIBUTED = "ATTRIBUTED"
EVIDENCE_PROBABLE = "PROBABLE"
EVIDENCE_PENDING = "PENDING"
EVIDENCE_CONTRADICTED = "CONTRADICTED"

# ==========================================
# FUENTES
# ==========================================
RUTA_SALSERA_SOURCES = [
    {"source_id": "RS-001", "title": "...", "url": "...", "source_level": "A", ...},
    ...
]

# ==========================================
# TIMELINE EVENTS
# ==========================================
RUTA_SALSERA_TIMELINE = [
    {
        "id": "discos-fuentes-1934",
        "anio": "1934",
        "titulo": "Discos Fuentes fundada en Cartagena",
        "categoria": "industria",
        "description": "...",
        "people": ["Antonio Fuentes"],
        "organizations": ["Discos Fuentes"],
        "evidence_status": "VERIFIED_PRIMARY",
        "sources": ["RS-001"],
        "attribution": None,
        "display_order": 1,
    },
    ...
]

# ==========================================
# VENUES (lugares actuales)
# ==========================================
RUTA_SALSERA_VENUES = [
    {
        "id": "el-tibiri",
        "name": "El Tíbiri Tábara",
        "type": "discoteca",
        "address": "Cra 70 #70-03 (Calle 44B), Laureles",
        "neighborhood": "Laureles",
        "phone": "+57 310 8495461",
        "facebook": "https://facebook.com/tibiri.bar",
        "instagram": None,
        "website": None,
        "description": "Sótano de salsa clásica, son cubano y guaguancó.",
        "music_style": "Salsa clásica, son cubano, guaguancó",
        "is_underground": True,
        "operating_hours": "Mié-Sáb 21:00-03:00 (sujeto a cambios)",
        "coordinates": {"lat": 6.2520, "lng": -75.5910},
        "evidence_status": "VERIFIED_PRIMARY",
        "sources": ["RS-033", "RS-034", "RS-035", "RS-036", "RS-037", "RS-040"],
        "last_verified": "2026-09-18",
        "historical_founding": None,  # NO mostrar fecha
        "display_order": 1,
    },
    ...
]

# ==========================================
# ARTISTS / ORCHESTRAS
# ==========================================
RUTA_SALSERA_ARTISTS = [
    {
        "id": "fruko-persona",
        "name": "Julio Ernesto Estrada 'Fruko'",
        "entity_type": "person",
        "founding_year": None,
        "contribution": "Pionero de la salsa colombiana",
        "related_orchestras": ["fruko-y-sus-tesos"],
        "notable_works": [],
        "evidence_status": "VERIFIED_PRIMARY",
        "sources": ["RS-005", "RS-006"],
        "display_order": 1,
    },
    ...
]

# ==========================================
# RADIO
# ==========================================
RUTA_SALSERA_RADIO = [
    {
        "id": "latina-stereo",
        "name": "Latina Stereo",
        "frequency": "100.9 FM",
        "call_sign": "HJQO",
        "founding_period": "~1985",
        "slogan": "Salsa desde 1985",
        "role": "Difusión de salsa clásica y dura",
        "url": "https://latinastereo.com",
        "evidence_status": "VERIFIED_PRIMARY",
        "sources": ["RS-020", "RS-021"],
        "attribution": "Latina Stereo afirma haber iniciado transmisiones desde 1985",
        "display_order": 1,
    },
]

# ==========================================
# DISCOGRAPHIC INDUSTRY
# ==========================================
RUTA_SALSERA_LABELS = [
    {
        "id": "discos-fuentes",
        "name": "Discos Fuentes",
        "founding_year": "1934",
        "founding_location": "Cartagena, Colombia",
        "move_to_medellin": "Entre 1954 y 1960 (contradicho)",
        "founder": "Antonio Fuentes Estrada",
        "catalog_note": "75% música tropical (atribuido a Resonancias UC)",
        "description": "Primera discográfica de música tropical en Colombia.",
        "url": "https://discosfuentes.com.co",
        "evidence_status": "VERIFIED_PRIMARY",
        "sources": ["RS-001", "RS-002", "RS-003"],
        "display_order": 1,
    },
    ...
]

# ==========================================
# SOURCES (fuentes bibliográficas)
# ==========================================
RUTA_SALSERA_ACADEMIC_SOURCES = [
    {
        "id": "santana-1992",
        "author": "Sergio Santana Archbold",
        "title": "¿Qué es la Salsa? Buscando la Melodía",
        "publisher": "Ediciones Salsa y Cultura / Editorial Copiyepes",
        "location": "Medellín",
        "year": "1992",
        "evidence_status": "VERIFIED_PRIMARY",
        "sources": ["RS-053"],
    },
    ...
]

# ==========================================
# EVENTS (eventos actuales)
# ==========================================
RUTA_SALSERA_CURRENT_EVENTS = [
    {
        "id": "viva-la-salsa-2026",
        "title": "Viva la Salsa 2026",
        "date": "25 julio 2026",
        "location": "Estadio Atanasio Girardot, Medellín",
        "url": "https://canaltrece.com.co/noticias/viva-la-salsa-medellin",
        "evidence_status": "VERIFIED_PRIMARY",
        "sources": ["RS-024"],
    },
    ...
]

# ==========================================
# INTRO TEXT
# ==========================================
RUTA_SALSERA_INTRO = "..."
```

### Por qué módulo separado

1. **Claridad:** `content_data.py` tiene 1463 líneas. Agregar 300+ más lo haría más difícil de mantener.
2. **Responsabilidad:** Los datos de la Ruta tienen campos (`evidence_status`, `sources`) que no existen en el sistema actual.
3. **Independencia:** La Ruta puede evolucionar sin afectar a `content_data.py`.
4. **Patrón:** Cada sección importante de SalsaQuest tiene su propio patrón de datos (timeline en `timeline_events_data.py`, contenido general en `content_data.py`).

---

## 9. DATA CONTRACT

### HistoricalEvent

```python
{
    "id": str,                    # OBLIGATORIO, slug único
    "anio": str,                  # OBLIGATORIO, año o rango ("1934", "~1954-1960")
    "titulo": str,                # OBLIGATORIO
    "categoria": str,             # OBLIGATORIO: "industria"|"orquesta"|"radio"|"lugar"|"evento"|"persona"|"grabacion"
    "description": str,           # OBLIGATORIO
    "people": list[str],          # OPCIONAL
    "organizations": list[str],   # OPCIONAL
    "evidence_status": str,       # OBLIGATORIO: ver Evidence States
    "sources": list[str],         # OBLIGATORIO: IDs de source
    "attribution": str | None,    # OBLIGATORIO si evidence_status == "ATTRIBUTED"
    "display_order": int,         # OBLIGATORIO
}
```

### Venue

```python
{
    "id": str,                    # OBLIGATORIO, slug único
    "name": str,                  # OBLIGATORIO
    "type": str,                  # OBLIGATORIO: "bar"|"discoteca"|"salon"
    "address": str,               # OBLIGATORIO, dirección verificada
    "neighborhood": str,          # OBLIGATORIO
    "phone": str | None,          # OPCIONAL
    "facebook": str | None,       # OPCIONAL
    "instagram": str | None,      # OPCIONAL
    "website": str | None,        # OPCIONAL
    "description": str,           # OBLIGATORIO
    "music_style": str,           # OBLIGATORIO
    "is_underground": bool,       # OPCIONAL, default False
    "operating_hours": str | None,# OPCIONAL
    "coordinates": {"lat": float, "lng": float},  # OBLIGATORIO
    "evidence_status": str,       # OBLIGATORIO
    "sources": list[str],         # OBLIGATORIO
    "last_verified": str,         # OBLIGATORIO, "YYYY-MM-DD"
    "historical_founding": str | None,  # None si no documentado
    "display_order": int,         # OBLIGATORIO
}
```

### ArtistOrchestra

```python
{
    "id": str,                    # OBLIGATORIO
    "name": str,                  # OBLIGATORIO
    "entity_type": str,           # OBLIGATORIO: "person"|"orchestra"
    "founding_year": str | None,  # None si persona
    "label": str | None,          # Sello discográfico
    "contribution": str,          # OBLIGATORIO
    "related_orchestras": list[str],  # Para personas
    "notable_works": list[str],   # Obras destacadas
    "evidence_status": str,       # OBLIGATORIO
    "sources": list[str],         # OBLIGATORIO
    "attribution": str | None,    # Si ATTRIBUTED
    "display_order": int,         # OBLIGATORIO
}
```

### RadioStation

```python
{
    "id": str,
    "name": str,
    "frequency": str,
    "call_sign": str | None,
    "founding_period": str,       # "~1985"
    "slogan": str,
    "role": str,
    "url": str,
    "evidence_status": str,
    "sources": list[str],
    "attribution": str | None,
    "display_order": int,
}
```

### SourceRef

```python
{
    "source_id": str,             # "RS-001"
    "title": str,
    "publisher": str,
    "url": str,
    "source_level": str,          # "A"|"B"|"C"|"D"
    "access_date": str,           # "2026-09-18"
}
```

---

## 10. CONTENT CONTRACT IMPLEMENTATION

### Filtro de validación en Python

```python
# En ruta_salsera_data.py, al final del archivo:
ALLOWED_EVIDENCE_STATES = {
    "VERIFIED_PRIMARY",
    "VERIFIED_SECONDARY",
    "ATTRIBUTED",
    "PROBABLE",
    "PENDING",
    "CONTRADICTED",
}

# DO_NOT_USE items are simply never included in the data.
# This is the primary filter: if it's not in the data, it can't be displayed.
```

### Flujo de autorización

```
1. Datos en ruta_salsera_data.py
   → Solo incluyen items con evidence_status en ALLOWED_EVIDENCE_STATES
   → Items DO_NOTUSE simplemente NO EXISTEN en el archivo

2. API /api/ruta-salsera
   → Sirve el JSON completo (ya filtrado por diseño)

3. Frontend ruta_salsera.js
   → Renderiza todos los items del JSON
   → Muestra badge según evidence_status
   → Nunca interpreta ni filtra por su cuenta
```

### Badges en UI

```javascript
function badgeEvidencia(status) {
    const badges = {
        "VERIFIED_PRIMARY": '<span class="badge-evidence badge-primary">Documentado</span>',
        "VERIFIED_SECONDARY": '<span class="badge-evidence badge-secondary">Fuente verificada</span>',
        "ATTRIBUTED": '<span class="badge-evidence badge-attributed">Atribuido</span>',
        "PROBABLE": '<span class="badge-evidence badge-probable">Probable</span>',
        "PENDING": '<span class="badge-evidence badge-pending">En verificación</span>',
        "CONTRADICTED": '<span class="badge-evidence badge-disputed">En disputa</span>',
    };
    return badges[status] || '';
}
```

---

## 11. ROUTE ARCHITECTURE

### SSR vs API + Client-side

**Decisión: API + Client-side rendering** (mismo patrón que el resto de SalsaQuest).

Justificación:
- Todos los endpoints existentes usan este patrón
- El frontend ya tiene la infraestructura (fetch, DOM manipulation)
- Leaflet se inicializa en client-side
- Los badges de evidencia se renderizan en client-side
- SEO se resuelve con metadata en el template (server-side)

### Rutas

| Método | Ruta | Función | Archivo |
|--------|------|---------|---------|
| GET | `/ruta-salsera` | Renderiza template | `main.py` |
| GET | `/api/ruta-salsera` | Devuelve JSON con todos los datos | `content.py` |

### Endpoint API

```python
# En content.py, agregar:

from app.models.ruta_salsera_data import (
    RUTA_SALSERA_TIMELINE, RUTA_SALSERA_VENUES, RUTA_SALSERA_ARTISTS,
    RUTA_SALSERA_RADIO, RUTA_SALSERA_LABELS, RUTA_SALSERA_ACADEMIC_SOURCES,
    RUTA_SALSERA_CURRENT_EVENTS, RUTA_SALSERA_INTRO, RUTA_SALSERA_SOURCES
)

@content_bp.route('/api/ruta-salsera', methods=['GET'])
def get_ruta_salsera():
    return jsonify({
        "intro": RUTA_SALSERA_INTRO,
        "timeline": RUTA_SALSERA_TIMELINE,
        "venues": RUTA_SALSERA_VENUES,
        "artists": RUTA_SALSERA_ARTISTS,
        "radio": RUTA_SALSERA_RADIO,
        "labels": RUTA_SALSERA_LABELS,
        "academic_sources": RUTA_SALSERA_ACADEMIC_SOURCES,
        "current_events": RUTA_SALSERA_CURRENT_EVENTS,
        "sources": RUTA_SALSERA_SOURCES,
    })
```

### Ruta Flask

```python
# En main.py, agregar:

@main_bp.route('/ruta-salsera')
def ruta_salsera():
    return render_template('ruta_salsera.html', active_page='ruta_salsera')
```

---

## 12. FRONTEND ARCHITECTURE

### Template: `ruta_salsera.html`

```html
{% extends "base.html" %}
{% block title %}La Ruta Salsera de Medellín | SalsaQuest{% endblock %}
{% block meta_description %}Historia, lugares y cultura salsera de Medellín documentados con evidencia verificada.{% endblock %}
{% block og_title %}La Ruta Salsera de Medellín | SalsaQuest{% endblock %}
{% block og_description %}Descubre la historia de la salsa en Medellín: lugares, artistas, industria discográfica y ruta turística documentada.{% endblock %}

{% block extra_css %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/ruta_salsera.css') }}">
{% endblock %}

{% block content %}
<!-- Hero -->
<!-- Intro -->
<!-- Timeline -->
<!-- Industry -->
<!-- Radio -->
<!-- Artists -->
<!-- Venues -->
<!-- Map -->
<!-- Son Havana -->
<!-- Events -->
<!-- Sources -->
<!-- CTA -->
{% endblock %}

{% block extra_js %}
<script src="{{ url_for('static', filename='js/ruta_salsera.js') }}"></script>
{% endblock %}
```

### JS: `ruta_salsera.js`

```javascript
// Estructura conceptual
document.addEventListener('DOMContentLoaded', () => {
    cargarRutaSalsera();
});

async function cargarRutaSalsera() {
    const res = await fetch('/api/ruta-salsera');
    const data = await res.json();

    renderIntro(data.intro);
    renderTimeline(data.timeline);
    renderVenues(data.venues);
    renderMap(data.venues);
    renderArtists(data.artists);
    renderRadio(data.radio);
    renderLabels(data.labels);
    renderAcademicSources(data.academic_sources);
    renderCurrentEvents(data.current_events);
    renderSources(data.sources);
}
```

### CSS: `ruta_salsera.css`

Estilos específicos para:
- Timeline de la Ruta (horizontal scroll en mobile)
- Badges de evidencia
- Tarjetas de venues
- Secciones de fuentes
- Responsive

### Separación Content / Presentation / Behavior

| Capa | Archivo | Responsabilidad |
|------|---------|-----------------|
| Content | `ruta_salsera_data.py` | Datos + evidence_status + sources |
| Presentation | `ruta_salsera.html` + `ruta_salsera.css` | Estructura HTML + estilos |
| Behavior | `ruta_salsera.js` | Fetch + render + interacciones |

---

## 13. TIMELINE IMPLEMENTATION

### HTML structure

```html
<section id="rs-timeline-section">
    <h2 class="titulo-seccion-glass">La historia de la salsa en Medellín</h2>
    <div id="rs-timeline-filtros" class="d-flex flex-wrap gap-2 mb-3"></div>
    <div class="rs-timeline-scroll-wrapper">
        <div id="rs-timeline-container" class="rs-timeline-track">
            <!-- Rendered by JS -->
        </div>
    </div>
</section>
```

### JS rendering

```javascript
function renderTimeline(events) {
    const container = document.getElementById('rs-timeline-container');
    if (!container) return;

    // Ordenar por display_order
    const sorted = events.sort((a, b) => a.display_order - b.display_order);

    container.innerHTML = sorted.map(ev => `
        <div class="rs-timeline-card" data-anio="${ev.anio}" data-evidence="${ev.evidence_status}">
            <span class="rs-timeline-year">${ev.anio}</span>
            <span class="badge-evidence badge-${ev.evidence_status.toLowerCase()}">${evidenceLabel(ev.evidence_status)}</span>
            <h4>${ev.titulo}</h4>
            <p>${ev.description}</p>
            ${ev.attribution ? `<p class="rs-attribution"><em>${ev.attribution}</em></p>` : ''}
            <div class="rs-sources">${renderSources(ev.sources)}</div>
        </div>
    `).join('');
}
```

### Manejo de casos especiales

| Caso | Implementación |
|------|----------------|
| Año faltante | NO ocurre (todos los eventos tienen año) |
| Rango ("~1954-1960") | Se muestra tal cual, con tooltip explicativo |
| Contradictado | Badge naranja "En disputa" + nota |
| Atribuido | Badge amarillo "Atribuido" + attribution text |
| Probable | Badge gris "Probable" |

---

## 14. VENUES IMPLEMENTATION

### Venue card HTML

```html
<div class="rs-venue-card" data-evidence="${venue.evidence_status}">
    <span class="badge-evidence badge-${venue.evidence_status.toLowerCase()}">${evidenceLabel(venue.evidence_status)}</span>
    <h3>${venue.name}</h3>
    <p class="rs-venue-type">${venue.type} · ${venue.neighborhood}</p>
    <p class="rs-venue-address"><i class="fa-solid fa-location-dot"></i> ${venue.address}</p>
    ${venue.phone ? `<p class="rs-venue-phone"><i class="fa-solid fa-phone"></i> ${venue.phone}</p>` : ''}
    ${venue.operating_hours ? `<p class="rs-venue-hours"><i class="fa-solid fa-clock"></i> ${venue.operating_hours}</p>` : ''}
    <p class="rs-venue-style"><i class="fa-solid fa-music"></i> ${venue.music_style}</p>
    <div class="rs-venue-links">
        <a href="https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(venue.address)}" target="_blank" rel="noopener" class="btn btn-outline-warning btn-sm">
            <i class="fa-solid fa-map-location-dot"></i> Abrir en Maps
        </a>
        ${venue.facebook ? `<a href="${venue.facebook}" target="_blank" rel="noopener" class="btn btn-outline-primary btn-sm"><i class="fa-brands fa-facebook"></i></a>` : ''}
        ${venue.instagram ? `<a href="${venue.instagram}" target="_blank" rel="noopener" class="btn btn-outline-danger btn-sm"><i class="fa-brands fa-instagram"></i></a>` : ''}
    </div>
    <small class="rs-venue-verified">Verificado: ${venue.last_verified}</small>
</div>
```

### Regla: No presentar como histórico

Si `venue.historical_founding` es `None`, NO se muestra ningún año de fundación ni descripción como "establecimiento histórico".

---

## 15. MAP IMPLEMENTATION

### Leaflet (ya cargado)

Leaflet v1.9.4 ya está cargado en `base.html`. No se necesita dependencia adicional.

### Inicialización

```javascript
function renderMap(venues) {
    const mapDiv = document.getElementById('rs-map');
    if (!mapDiv || typeof L === 'undefined') return;

    const mapa = L.map('rs-map').setView([6.2477, -75.5850], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors',
        maxZoom: 18,
    }).addTo(mapa);

    venues.forEach(v => {
        L.marker([v.coordinates.lat, v.coordinates.lng]).addTo(mapa)
            .bindPopup(`
                <strong>${v.name}</strong><br>
                <span style="font-size:0.85em">${v.address}</span><br>
                <span style="font-size:0.85em">${v.music_style}</span><br>
                <a href="https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(v.address)}" target="_blank" rel="noopener">Abrir en Maps</a>
            `);
    });
}
```

### Coordenadas

Las coordenadas en `ruta_salsera_data.py` son aproximaciones basadas en direcciones verificadas. Durante implementación, se geocodificarán exactamente usando la API de Nominatim (OpenStreetMap) si es necesario, o se mantendrán como approximations con la nota de que deben verificarse.

---

## 16. SON HAVANA ENTITY INTEGRITY

### Separación en datos

```python
# Venue (el bar)
SON_HAVANA_VENUE = {
    "id": "son-havana",
    "name": "Son Havana",
    "entity_type": "venue",
    ...
}

# Orchestra (la banda)
SON_HAVANA_ALL_STARS = {
    "id": "son-havana-all-stars",
    "name": "Son Havana All Stars",
    "entity_type": "orchestra",
    "related_venue": "son-havana",  # Relación documentada
    ...
}

# NO incluir: Julio Restrepo Molina como fundador confirmado
# (estado PROBABLE, no se publica como hecho)
```

### Regla de implementación

- `Son Havana` aparece como **venue** en la lista de lugares
- `Son Havana All Stars` aparece como **orquesta** en la lista de artistas
- `Julio Restrepo` NO aparece como entidad separada (PROBABLE)
- `Latina Stereo` es una entidad separada (radio)
- `Inversiones Son Havana S.A.S.` NO aparece (sin evidencia)

---

## 17. ARTISTS / ORCHESTRAS

### Implementación

```python
RUTA_SALSERA_ARTISTS = [
    # PERSONAS
    {
        "id": "fruko-persona",
        "name": "Julio Ernesto Estrada 'Fruko'",
        "entity_type": "person",
        "founding_year": None,
        "contribution": "Pionero de la salsa colombiana (atribuido a Discos Fuentes)",
        "related_orchestras": ["fruko-y-sus-tesos"],
        "evidence_status": "VERIFIED_PRIMARY",
        "sources": ["RS-005", "RS-006"],
        "attribution": None,
        "display_order": 1,
    },
    {
        "id": "diego-gale-persona",
        "name": "Diego Galé",
        "entity_type": "person",
        "founding_year": None,
        "contribution": "Fundador de Grupo Galé, percusionista de Grupo Niche",
        "related_orchestras": ["grupo-gale"],
        "evidence_status": "VERIFIED_SECONDARY",
        "sources": ["RS-017"],
        "display_order": 2,
    },
    # ORQUESTAS
    {
        "id": "fruko-y-sus-tesos",
        "name": "Fruko y sus Tesos",
        "entity_type": "orchestra",
        "founding_year": "1970",
        "label": "Discos Fuentes",
        "contribution": "Primera orquesta de salsa colombiana",
        "notable_works": ["A la memoria del muerto", "El Preso"],
        "evidence_status": "VERIFIED_PRIMARY",
        "sources": ["RS-008", "RS-009", "RS-010"],
        "display_order": 3,
    },
    # ... (11 entradas totales)
]
```

---

## 18. RADIO

```python
RUTA_SALSERA_RADIO = [
    {
        "id": "latina-stereo",
        "name": "Latina Stereo",
        "frequency": "100.9 FM",
        "call_sign": "HJQO",
        "founding_period": "~1985",
        "slogan": "Salsa desde 1985",
        "role": "Difusión de salsa clásica y dura en Medellín",
        "url": "https://latinastereo.com",
        "evidence_status": "VERIFIED_PRIMARY",
        "sources": ["RS-020", "RS-021"],
        "attribution": "Latina Stereo afirma haber iniciado transmisiones de salsa clásica desde 1985",
        "display_order": 1,
    },
]
```

---

## 19. SOURCE SYSTEM

### Fuentes en la Ruta

Las fuentes se muestran de dos formas:

1. **Inline:** Cada claim lleva un badge de evidencia que, al hacer click, muestra la fuente en un tooltip/popover
2. **Panel de fuentes:** Sección al final de la página con la tabla completa de fuentes clasificadas

### Panel de fuentes (sección V1, no MVP)

```html
<section id="rs-sources-section">
    <h2 class="titulo-seccion-glass">Fuentes y evidencia</h2>
    <div class="rs-sources-table">
        <!-- Tabla de fuentes clasificadas por nivel -->
    </div>
</section>
```

### Para MVP: badges inline

Cada claim renderiza su badge. Click en badge → tooltip con:
- Nombre de la fuente
- Nivel (A/B/C/D)
- Enlace a la fuente
- Fecha de verificación

---

## 20. SEO IMPLEMENTATION

### Metadata

```html
{% block title %}La Ruta Salsera de Medellín | SalsaQuest{% endblock %}
{% block meta_description %}Descubre la historia de la salsa en Medellín: lugares, artistas, industria discográfica y ruta turística documentada con evidencia verificada.{% endblock %}
{% block og_title %}La Ruta Salsera de Medellín{% endblock %}
{% block og_description %}Historia, lugares y cultura salsera de Medellín documentados.{% endblock %}
{% block og_image %}{{ url_for('static', filename='img/cuba-flag.jpg', _external=True) }}{% endblock %}
{% block twitter_title %}La Ruta Salsera de Medellín | SalsaQuest{% endblock %}
{% block twitter_description %}Historia, lugares y cultura salsera de Medellín documentados.{% endblock %}
```

### Canonical

```html
<link rel="canonical" href="{{ url_for('main.ruta_salsera', _external=True) }}">
```

### Structured data

```html
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TouristTrip",
    "name": "La Ruta Salsera de Medellín",
    "description": "Historia, lugares y cultura salsera de Medellín documentados",
    "touristType": "Cultural tourism",
    "itinerary": {
        "@type": "ItemList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "item": {"@type": "NightClub", "name": "El Tíbiri Tábara", "address": "Cra 70 #70-03, Laureles, Medellín"}},
            {"@type": "ListItem", "position": 2, "item": {"@type": "NightClub", "name": "Son Havana", "address": "Cra 73 #44-56, Florida Nueva, Medellín"}},
            {"@type": "ListItem", "position": 3, "item": {"@type": "NightClub", "name": "Discoteca El Suave", "address": "Av. 33 #80a-30, Medellín"}}
        ]
    }
}
</script>
```

### Semantic HTML

- `<h1>` solo uno (Hero title)
- `<h2>` por sección (Timeline, Venues, Artists, etc.)
- `<h3>` por tarjeta individual
- `<nav>` para filtros de timeline
- `<section>` por sección
- `<article>` por card individual

---

## 21. I18N

### MVP: Solo español

No se implementa i18n en Fase 5. Solo se diseña la estructura para permitirlo después.

### Preparación para futuro

- Todos los textos visibles están en el template (no hardcodeados en JS)
- Los textos de evidencia ("Documentado", "Atribuido") están en una función JS que puede parametrizarse
- Los textos del template usan bloques `{% block %}` que pueden reemplazarse

### Reglas para futuro

- Nombres propios NO se traducen
- Fuentes NO se traducen
- Atribuciones viajan en idioma original
- Fallback: FR → EN → ES

---

## 22. ACCESSIBILITY

### WCAG 2.2 AA

| Requisito | Implementación |
|-----------|----------------|
| Heading hierarchy | h1 → h2 → h3 → h4 |
| Keyboard | Todos los interactivos navegables con Tab |
| Focus | Focus visible en todos los botones y enlaces |
| ARIA | `aria-label` en badges, `role` en timeline |
| Alt text | Todas las imágenes con alt descriptivo |
| Reduced motion | `@media (prefers-reduced-motion: reduce)` |
| Contrast | Texto sobre overlay con mínimo 4.5:1 |
| Mapa | Lista alternativa de lugares con direcciones |

---

## 23. PERFORMANCE

| Recurso | Strategy |
|---------|----------|
| Imágenes | `loading="lazy"` en todas |
| Mapa | Carga bajo demanda (solo cuando el usuario llega a la sección) |
| JS específico | Solo se carga en `/ruta-salsera` (via `{% block extra_js %}`) |
| CSS específico | Solo se carga en `/ruta-salsera` (via `{% block extra_css %}`) |
| Fuentes | Solo Poppins (ya cargada) |
| Leaflet | Ya cargado en todas las páginas |
| API response | JSON estático, caching del lado del servidor |

### Priority order

```
1. HTML (template renderizado server-side)
2. CSS (estilos aplicados)
3. Content (fetch → render)
4. Interaction (event listeners)
5. Map (Leaflet init)
```

---

## 24. SECURITY

| Riesgo | Mitigación |
|--------|------------|
| XSS en templates | Jinja2 auto-escaping (ya activo) |
| URLs externas | `rel="noopener noreferrer"` en todos los enlaces externos |
| Datos de usuario | No se recogen datos en la Ruta |
| API innecesaria | Solo 1 endpoint, datos estáticos |
| Leaflet | CDN oficial, versión verificada |
| CSP | Se hereda de base.html |

---

## 25. DEPENDENCY AUDIT

### Dependencias existentes (reutilizar)

| Dependencia | Versión | Ya cargada | Uso |
|-------------|---------|------------|-----|
| Bootstrap | 5.3.0 | SÍ | Grid, cards, botones |
| Leaflet | 1.9.4 | SÍ | Mapa interactivo |
| FontAwesome | 6.4.0 | SÍ | Iconos |
| Poppins | Google Fonts | SÍ | Tipografía |

### Nuevas dependencias

**Ninguna.** No se añaden dependencias nuevas. Todo se resuelve con las herramientas ya disponibles.

---

## 26. TESTING STRATEGY

### Unit Tests

- Validación de datos en `ruta_salsera_data.py` (todos los items tienen `evidence_status` válido)
- Todos los `source_ids` referenciados existen en `RUTA_SALSERA_SOURCES`

### Integration Tests

- GET `/ruta-salsera` retorna 200
- GET `/api/ruta-salsera` retorna JSON válido
- Template renderiza sin errores

### Functional Tests

- Timeline renderiza 14 eventos
- Mapa muestra 3 marcadores
- Venue cards muestran dirección y teléfono
- Badges de evidencia se muestran correctamente
- CTA "Abrir en Maps" genera enlace válido

### Accessibility Tests

- Lighthouse accessibility ≥90
- Keyboard navigation funcional
- Screen reader puede leer timeline y venues

### SEO Tests

- Title y meta description presentes
- Structured data válido
- Canonical URL definida

### Responsive Tests

- Mobile (<576px): timeline horizontal scroll, cards stack
- Tablet (576-991px): 2 columnas
- Desktop (≥992px): 3 columnas, timeline vertical

### Regression Tests

- `/medellin` sigue funcionando igual
- Home page sin cambios
- Navbar funciona correctamente
- Son Havana page sin cambios
- Otras rutas sin cambios

---

## 27. TEST MATRIX

| Test | Tipo | Archivo | Resultado esperado | Prioridad |
|------|------|---------|-------------------|-----------|
| Datos válidos | Unit | ruta_salsera_data.py | Todos items con evidence_status válido | Alta |
| Sources referenciados | Unit | ruta_salsera_data.py | Todos source_ids existen | Alta |
| Ruta 200 | Integration | main.py | GET /ruta-salsera → 200 | Alta |
| API JSON | Integration | content.py | GET /api/ruta-salsera → JSON válido | Alta |
| Timeline render | Functional | ruta_salsera.js | 14 eventos visibles | Alta |
| Map markers | Functional | ruta_salsera.js | 3 marcadores en mapa | Alta |
| Venue cards | Functional | ruta_salsera.js | 3 cards con datos | Alta |
| Evidence badges | Functional | ruta_salsera.js | Badges visibles en cada claim | Alta |
| Maps CTA | Functional | ruta_salsera.js | Enlace abre Google Maps | Media |
| Lighthouse a11y | Accessibility | Lighthouse | Score ≥90 | Media |
| Keyboard nav | Accessibility | Manual | Tab navigation funcional | Media |
| Mobile responsive | Responsive | Manual | Layout correcto <576px | Alta |
| /medellin intacta | Regression | Manual | Sin cambios | Alta |
| Home intacta | Regression | Manual | Sin cambios | Alta |
| Navbar funciona | Regression | Manual | Enlaces correctos | Alta |

---

## 28. IMPLEMENTATION ORDER

```
1.  Crear models/ruta_salsera_data.py (datos + evidence)
2.  Crear endpoint /api/ruta-salsera en content.py
3.  Crear ruta /ruta-salsera en main.py
4.  Crear templates/ruta_salsera.html (estructura base)
5.  Crear static/css/ruta_salsera.css (estilos específicos)
6.  Crear static/js/ruta_salsera.js (fetch + render intro)
7.  Implementar timeline en JS
8.  Implementar venue cards en JS
9.  Implementar mapa Leaflet en JS
10. Implementar artistas/orquestas en JS
11. Implementar radio en JS
12. Implementar industria discográfica en JS
13. Implementar Son Havana en JS
14. Implementar eventos actuales en JS
15. Implementar badges de evidencia en JS
16. Implementar SEO (metadata + structured data)
17. Implementar accessibility
18. Agregar enlace en navbar (base.html)
19. Tests de regresión
20. Audit final
```

---

## 29. ROLLBACK / SAFETY

### Reglas

1. **Cambios pequeños:** Cada archivo se crea/modifica de forma independiente
2. **Checkpoints:** Después de cada grupo de cambios, verificar que la app arranca
3. **No DB reset:** No se modifica la base de datos
4. **No Git destructivo:** No se hace reset, clean, o force push
5. **Revertir cambios propios:** Si algo falla, eliminar los archivos creados

### Puntos de verificación

| Checkpoint | Verificación |
|------------|-------------|
| Después del archivo de datos | Python importa sin errores |
| Después de la ruta | GET /ruta-salsera retorna 200 |
| Después del template | Página renderiza (puede estar vacía) |
| Después del JS | Contenido carga desde API |
| Después del CSS | Estilos se aplican |
| Después del navbar | Enlace aparece y funciona |
| Después de tests | Todos los tests pasan |

---

## 30. SCOPE GUARD

### IN SCOPE

- Template `ruta_salsera.html`
- Datos `ruta_salsera_data.py`
- API `/api/ruta-salsera`
- Ruta `/ruta-salsera`
- JS `ruta_salsera.js`
- CSS `ruta_salsera.css`
- Navbar link
- SEO metadata
- Structured data
- Responsive design
- Accessibility
- Badges de evidencia
- Timeline, venues, map, artists, radio, labels, events

### OUT OF SCOPE

- Modificación de `/medellin`
- Modificación de Son Havana page
- Modificación de `content_data.py`
- Nueva base de datos
- CMS o panel administrativo
- Sistema de autenticación
- i18n (EN/FR)
- Gamificación
- Audio/guía sonora
- Realidad aumentada
- App nativa
- Eventos futuros (solo los 2 documentados)
- Calle Palacé (excluida del MVP)
- "Renacimiento de la salsa brava" (excluido)

---

## 31. ADRs

### ADR-001: `/ruta-salsera` como nueva ruta

**Decisión:** Crear ruta nueva, no modificar `/medellin`.

**Razón:** `/medellin` es funcional, tiene datos propios, y sirve un propósito diferente (vista general). La Ruta tiene arquitectura de datos propia (evidence_status, sources) incompatible con la estructura actual.

**Consecuencia:** Dos páginas sobre Medellín en SalsaQuest. Se distinguen por su propósito: `/medellin` es overview, `/ruta-salsera` es experiencia documentada.

### ADR-002: Python dicts (no BD) para datos de la Ruta

**Decisión:** Datos en `ruta_salsera_data.py` como Python dicts, no en SQLAlchemy/SQLite.

**Razón:** El contenido editorial estático no necesita DB. El patrón de `content_data.py` ya funciona. Las migraciones innecesarias agregan complejidad sin beneficio.

**Consecuencia:** Los datos se actualizan editando el archivo Python, no vía un panel admin.

### ADR-003: API + client-side rendering

**Decisión:** Misma arquitectura que el resto de SalsaQuest (fetch → JSON → DOM).

**Razón:** Patrón probado, Leaflet se inicializa en client-side, badges de evidencia se renderizan en client-side. SEO se resuelve con metadata server-side.

**Consecuencia:** JavaScript renderiza todo el contenido. Sin JavaScript, la página muestra solo el título.

### ADR-004: Módulo de datos separado

**Decisión:** `ruta_salsera_data.py` separado de `content_data.py`.

**Razón:** `content_data.py` tiene 1463L. Los datos de la Ruta tienen campos nuevos (`evidence_status`, `sources`). Separar evita contaminar el archivo existente.

**Consecuencia:** Un archivo más que mantener, pero con responsabilidad clara.

### ADR-005: Sin nuevas dependencias

**Decisión:** No agregar ninguna dependencia nueva.

**Razón:** Leaflet, Bootstrap, FontAwesome ya están cargados. No se necesita nada adicional para el MVP.

**Consecuencia:** Funcionalidades limitadas a lo que las dependencias actuales permiten. Acceptable para MVP.

---

## 32. TRACEABILITY MATRIX

| Product Requirement | Evidence Source | Technical Component | Test |
|---------------------|-----------------|---------------------|------|
| Timeline con 14 eventos | RS-001 a RS-054 | `ruta_salsera_data.py` → `RUTA_SALSERA_TIMELINE` | Timeline render test |
| 3 lugares actuales | RS-033 a RS-048 | `ruta_salsera_data.py` → `RUTA_SALSERA_VENUES` | Venue cards test |
| Mapa con marcadores | Coordenadas verificadas | `ruta_salsera.js` → `renderMap()` | Map markers test |
| Badges de evidencia | Evidence Audit completo | `ruta_salsera.js` → `badgeEvidencia()` | Evidence badges test |
| 11 artistas/orquestas | RS-005 a RS-019 | `ruta_salsera_data.py` → `RUTA_SALSERA_ARTISTS` | Artists render test |
| 1 emisora de radio | RS-020 a RS-022 | `ruta_salsera_data.py` → `RUTA_SALSERA_RADIO` | Radio render test |
| 2 discográficas | RS-001 a RS-004 | `ruta_salsera_data.py` → `RUTA_SALSERA_LABELS` | Labels render test |
| Son Havana como venue | RS-025 a RS-032 | `ruta_salsera_data.py` → venue entry | Venue card test |
| SEO metadata | Product Spec §25 | Template blocks | Lighthouse SEO test |
| WCAG 2.2 AA | Product Spec §26 | Semantic HTML + ARIA | Lighthouse a11y test |
| Responsive | Product Spec §28 | CSS media queries | Manual responsive test |
| No datos DO_NOT_USE | Evidence Audit §H | Data validation | Unit test |

---

## 33. IMPLEMENTATION CHECKLIST

```
[ ] Crear models/ruta_salsera_data.py con todos los datos y evidence_status
[ ] Crear endpoint /api/ruta-salsera en content.py
[ ] Crear ruta /ruta-salsera en main.py
[ ] Crear templates/ruta_salsera.html con estructura base
[ ] Crear static/css/ruta_salsera.css con estilos específicos
[ ] Crear static/js/ruta_salsera.js con fetch y render
[ ] Implementar intro section
[ ] Implementar timeline con filtros por década
[ ] Implementar industria discográfica (Discos Fuentes + Codiscos)
[ ] Implementar radio (Latina Stereo)
[ ] Implementar artistas y orquestas (11 entradas)
[ ] Implementar venue cards (3 lugares)
[ ] Implementar mapa Leaflet con 3 marcadores
[ ] Implementar Son Havana como venue
[ ] Implementar eventos actuales (2 eventos)
[ ] Implementar badges de evidencia
[ ] Implementar fuentes section (MVP: inline badges)
[ ] Implementar CTA section
[ ] Agregar SEO metadata y structured data
[ ] Implementar accessibility (keyboard, ARIA, alt text)
[ ] Implementar responsive design
[ ] Agregar enlace "Ruta Salsera" en navbar (base.html)
[ ] Test: Python importa datos sin errores
[ ] Test: GET /ruta-salsera retorna 200
[ ] Test: GET /api/ruta-salsera retorna JSON válido
[ ] Test: Timeline renderiza 14 eventos
[ ] Test: Mapa muestra 3 marcadores
[ ] Test: Venue cards muestran datos correctos
[ ] Test: Badges de evidencia visibles
[ ] Test: /medellin sigue funcionando
[ ] Test: Home page sin cambios
[ ] Test: Navbar funciona correctamente
[ ] Lighthouse accessibility ≥90
[ ] Responsive mobile OK
[ ] Audit final
```

---

## 34. OPEN QUESTIONS

| # | Pregunta | Bloquea | Resolución propuesta |
|---|----------|---------|---------------------|
| OQ1 | ¿Coordenadas exactas geocodificadas? | Implementación del mapa | Usar coordenadas aproximadas de content_data.py (ya verificadas para El Tíbiri y Son Havana) |
| OQ2 | ¿Enlace en navbar dropdown "Lugares" o item independiente? | Navegación | Agregar en dropdown "Lugares" como 4to item |
| OQ3 | ¿Separar fuentes en sección aparte o solo inline? | MVP scope | MVP: solo inline badges. V1: sección de fuentes |

---

## 35. RISKS

| # | Riesgo | Impacto | Probabilidad | Mitigación |
|---|--------|---------|--------------|------------|
| 1 | Coordenadas imprecisas en mapa | Bajo | Media | Usar coordenadas de content_data.py ya verificadas |
| 2 | Confusión entre /medellin y /ruta-salsera | Bajo | Baja | Navbar labels claros, propósitos distintos |
| 3 | Contenido más extenso que otras páginas | Bajo | Alta | Paginación por secciones, scroll vertical |
| 4 | JS carga lenta en mobile | Medio | Baja | Lazy loading, mapa bajo demanda |
| 5 | Datos contradictorios visibles | Medio | Baja | evidence_status controla visibilidad |
| 6 | Navbar congestionado | Bajo | Media | Solo 1 item nuevo en dropdown existente |
| 7 | Fuentes CDN caídas | Bajo | Baja | Bootstrap/Leaflet/FontAwesome son CDNs robustos |

---

## 36. DEFINITION OF DONE — FASE 4

- [x] Se inspeccionó el proyecto real
- [x] Se confirmó el repositorio objetivo (`D:\Proyectos\sonhavanagame`)
- [x] Se leyó Evidence Audit
- [x] Se leyó Product Spec
- [x] Se resolvió la arquitectura de `/ruta-salsera`
- [x] Se analizó `/medellin`
- [x] Se definieron archivos exactos (4 crear, 3 modificar)
- [x] Se definió arquitectura de datos (Python dicts en módulo separado)
- [x] Se definió route architecture (SSR template + API endpoint)
- [x] Se definió frontend architecture (fetch → render)
- [x] Se definió mapa (Leaflet ya cargado, 3 marcadores)
- [x] Se definió evidence system (badges inline + panel futuro)
- [x] Se definió SEO (metadata + structured data)
- [x] Se definió accessibility (WCAG 2.2 AA)
- [x] Se definió performance (lazy loading, mapa bajo demanda)
- [x] Se definió security (Jinja2 escaping, noopener)
- [x] Se definió testing (15 tests definidos)
- [x] Se definió implementation order (20 pasos)
- [x] Se creó traceability matrix (12 requisitos trazados)
- [x] Se crearon 5 ADRs
- [x] Se creó implementation checklist (35 tareas)
- [x] Se documentaron scope guards (IN/OUT)
- [x] No se modificó código
- [x] No se modificó DB
- [x] No se realizaron operaciones Git
- [x] No se ejecutaron operaciones destructivas

---

## 37. INFORME FINAL

### A. Documento

`D:\Proyectos\sonhavanagame\ROUTE-SALSERA-IMPLEMENTATION-PLAN.md`

### B. Arquitectura actual

SalsaQuest es una app Flask multipágina con 19 templates, 4 blueprints, datos en Python dicts, y frontend Bootstrap 5 + Leaflet + FontAwesome. Patrón: Python dicts → API JSON → client-side rendering.

### C. Arquitectura propuesta

4 archivos nuevos (template, data, JS, CSS) + 3 modificaciones mínimas (route, API, navbar). Sin nuevas dependencias. Sin cambios a `/medellin`. Sin cambios a la DB.

### D. Archivos

| Acción | Archivo |
|--------|---------|
| CREATE | `app/models/ruta_salsera_data.py` |
| CREATE | `app/templates/ruta_salsera.html` |
| CREATE | `app/static/js/ruta_salsera.js` |
| CREATE | `app/static/css/ruta_salsera.css` |
| MODIFY | `app/routes/main.py` (+1 ruta) |
| MODIFY | `app/routes/content.py` (+1 endpoint) |
| MODIFY | `app/templates/base.html` (+1 enlace navbar) |
| NO TOUCH | Todo lo demás |

### E. Decisiones arquitectónicas

1. Ruta nueva, no modificar `/medellin`
2. Python dicts, no DB
3. API + client-side (mismo patrón existente)
4. Módulo de datos separado
5. Sin nuevas dependencias
6. Leaflet ya cargado (reutilizar)
7. Solo español en MVP
8. Badges inline para evidencia (MVP)
9. SEO server-side (template blocks)
10. Accesibilidad WCAG 2.2 AA

### F. Dependencias

Existentes: Bootstrap 5.3.0, Leaflet 1.9.4, FontAwesome 6.4.0, Poppins (Google Fonts).
Nuevas: Ninguna.

### G. Riesgos

7 riesgos documentados. Ninguno es bloqueante. El de mayor impacto es "contenido más extenso que otras páginas", mitigado con scroll por secciones.

### H. Preguntas abiertas

3 preguntas, todas con resolución propuesta. Ninguna bloqueante.

### I. Orden de implementación

20 pasos definidos, desde crear datos hasta audit final.

### J. Estado

**FASE 4 COMPLETA — PLANIFICACIÓN SOLAMENTE — NO IMPLEMENTADO**

# Fase 1 — Instrucciones de integración

## 1. Copia los archivos
- `css/fase1-diseno.css` → `app/static/css/fase1-diseno.css`
- `js/cursor-interactivo.js` → `app/static/js/cursor-interactivo.js`

## 2. Agrega el link y el script en `index.html`
Justo debajo de tu `<link ... style.css ...>` existente:
```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/fase1-diseno.css') }}">
```
Y junto a tus otros `<script>` antes de `</body>`:
```html
<script src="{{ url_for('static', filename='js/cursor-interactivo.js') }}"></script>
```

## 3. Aplica las clases nuevas donde correspondan

**Encabezados de sección** — reemplaza esto:
```html
<h3 class="text-warning fw-bold mb-3"><i class="fa-solid fa-star me-2"></i>Grandes Eventos</h3>
```
por esto (repite en TODOS los `<h3>` de sección: Récords, Historias, Timba,
Carátulas, Ranking, Orquestas, Instrumentos, Museos, Entrevistas, Grammy, etc.):
```html
<h3 class="glass-header"><i class="fa-solid fa-star me-2"></i>Grandes Eventos</h3>
```

**Tarjetas con hover-zoom** — donde tengas `class="card card-glass ..."`,
agrega `hover-zoom`:
```html
<div class="card card-glass hover-zoom ...">
```

**Título con efecto neón** (para cuando construyamos la sección Son Havana
en Fase 2, o si quieres aplicarlo ya al `<h1>` del hero):
```html
<h1 class="neon-title">Son Havana</h1>
```

## 4. Separar el bloque Trivia + Top Salseros + Timeline
Ahora mismo estas tres viven dentro de un `<div class="row">` compartido
(columnas `col-lg-4` / `col-lg-8`). Para darle su propio espacio a cada una:

1. Busca el `<div class="row g-4">` que envuelve `#desafio-section`,
   `#ranking-section` y `#timeline-section`.
2. Elimina las clases `col-lg-4` y `col-lg-8` de sus contenedores internos.
3. Envuelve cada una en su propio `<section class="mb-5">...</section>`,
   uno debajo del otro, en vez de lado a lado.
4. Aplica `glass-header` al título de cada una.

Con esto cada sección pasa a ocupar el ancho completo y tener su propio
"respiro" visual, en vez de competir por espacio en la misma fila.

## 5. Fase 4 (accesibilidad básica, ya incluida)
- El CSS respeta `prefers-reduced-motion` (usuarios que desactivan
  animaciones en su sistema no verán el parpadeo neón ni el cursor glow)
- El cursor interactivo se desactiva automáticamente en móvil/tablet
  (no tiene sentido ahí, y evita gastar batería/rendimiento)
- Pendiente para una próxima pasada: meta tags Open Graph/SEO y
  atributos `alt` reales en imágenes — mejor hacerlo cuando el
  contenido de Fase 2 esté listo, para no describir imágenes que
  van a cambiar.

---

# Fase 3 (parcial) — Fotos reales confirmadas con licencia abierta

Reemplaza estas 3 `imagen_url` en `ARTISTAS` (`content_data.py`) por las
reales — mismo slug, no rompe nada más:

```python
# la-lupe
"imagen_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/...",
# (usa el link de Special:FilePath de abajo, más estable)
```

Para no depender de rutas de miniatura que cambian, usa el patrón
`Special:FilePath` de Wikimedia (siempre resuelve a la imagen actual):

| Artista | URL para `imagen_url` |
|---|---|
| La Lupe | `https://commons.wikimedia.org/wiki/Special:FilePath/Cuban%20singer%20La%20Lupe%20performing%20in%20New%20York%20City%20LCCN2009632630%20(cropped).jpg` |
| Rubén Blades | `https://commons.wikimedia.org/wiki/Special:FilePath/Ruben%20Blades%20by%20Gage%20Skidmore.jpg` |
| Gilberto Santa Rosa | `https://commons.wikimedia.org/wiki/Special:FilePath/Concierto%20de%20Gilberto%20Santa%20Rosa%20en%20Pi%C3%B1as.jpg` |

**Atribución requerida** (son licencia CC BY-SA, no dominio público total
excepto La Lupe): agrega un pequeño crédito visible, por ejemplo un
`<small>` bajo la imagen o en el modal de detalle: "Foto: Wikimedia
Commons, CC BY-SA".

**Pendientes de Fase 3** (no encontré fuente confiable con licencia clara
aún): Willie Colón, Oscar D'León, Fruko, Afrosound. Puedo seguir
buscando en otra sesión — los artistas de Discos Fuentes (Fruko,
Afrosound) tienen poca cobertura en Wikimedia Commons, probablemente
haya que buscar en archivos de prensa colombiana con permiso de uso.

⚠️ **Dato para Fase 2:** Willie Colón falleció el 21 de febrero de 2026.
Tu biografía actual no lo menciona — revísala cuando trabajemos esa
sección para no dejarla desactualizada.

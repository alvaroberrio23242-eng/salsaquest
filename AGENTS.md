# AGENTS.md — SalsaQuest

Contexto persistente del repositorio para agentes de IA (OpenCode, y cualquier otro asistente que trabaje aquí). Léelo antes de proponer o ejecutar cambios.

## Qué es este proyecto

SalsaQuest es una app web interactiva (pensada como museo interactivo de la cultura salsera, no solo trivia) dirigida a turistas en lugares como Son Havana. Incluye storytelling, línea del tiempo histórica, museo de carátulas, biografías de artistas, mapa de lugares emblemáticos, sección Medellín salsera, trivia/desafío como elemento de gamificación, login y cartelera de eventos.

## Stack

- **Backend:** Python / Flask
- **Base de datos:** SQLite / SQLAlchemy
- **Frontend:** HTML5 / CSS3 / JavaScript (sin framework)
- **Hosting:** Render (deploy en vivo); requiere backend real, no puede vivir en GitHub Pages
- **Entorno local:** Windows, ruta `D:\Proyectos\sonhavanagame`, terminal Git Bash (MINGW64) — no usar PowerShell salvo excepciones puntuales (ej. `Compress-Archive`)

## Estructura

```
app/
├── routes/       (auth.py, main.py, timeline.py)
├── models/       (user.py, timeline_data.py, timeline_events_data.py)
├── services/     (ia_service.py — integración Anthropic, protegida con try/except)
├── templates/    (index.html, desafio.html, trivia.html, base.html, ...)
└── static/
    ├── css/
    ├── js/       (timeline.js, content.js, video-bg.js, ...)
    └── videos/   (fondos, comprimidos — ver sección Videos)
```

Rutas multipágina reales en `main.py`: `/historia/linea-de-tiempo`, `/historia/eventos-y-records`, `/artistas`, `/musica/caratulas-y-albumes`, `/musica/orquestas-e-instrumentos`, `/lugares`, `/medellin`, `/premios-y-entrevistas`, `/son-havana`, `/grammy`, `/timba`, `/trivia`, `/recursos`, además de `/` y `/desafio`.

## Decisiones de arquitectura fijadas (no revertir sin discutirlo)

- **Timeline:** fuente única de datos en `app/models/timeline_events_data.py` (`EVENTOS_TIMELINE`), usada por `init_db.py` y `timeline.py`. No duplicar esa lista en otro lado. Orden cronológico vía regex numérico (`_anio_numerico` en `timeline.py`), **no** alfabético ni por SQL `.asc()`. `/api/timeline` solo siembra la tabla si está vacía (antes se reseteaba en cada visita, causaba "database is locked").
- **Leaderboard:** `/api/leaderboard` vive únicamente en `auth.py` (se eliminó un duplicado que existía en `main.py`).
- **Trivia:** `/trivia` está separada de `/` en `main.py`. El endpoint `/api/trivia` en `main.py` (líneas ~86-108) es **código huérfano confirmado** — `timeline.js` usa su propio array local `preguntasQuiz`, ningún archivo hace fetch a `/api/trivia`. Candidato a eliminar.
- **API keys:** solo en variables de entorno (`.env`). `ANTHROPIC_API_KEY` ya configurada así. Nunca hardcodear claves.
- **Imágenes:** fotos reales vía Wikimedia Commons (licencias CC-BY/CC0), revisadas a mano. No inventar URLs de imágenes ni usar stock genérico.
- **Video de fondo:** usa dos elementos `<video>` (`#video-bg-a` / `#video-bg-b`, clase `.video-bg-layer`) para crossfade, controlados por `video-bg.js` (no usar `autoplay` en el HTML). Nunca debe caer a una imagen estática como fallback — siempre video en loop.
- **Videos comprimidos:** carpeta `app/static/videos` se mantiene comprimida (~20MB total). Los originales sin comprimir van en `originales_sin_comprimir/`, excluida en `.gitignore`. No commitear videos pesados sin comprimir.

## Convenciones de código y estilo

- **Comentarios:** estilo commit profesional, breves. Evitar comentarios narrativos/explicados-para-lector-externo — el dueño del repo necesita poder explicar cualquier cambio con sus propias palabras.
- **No asumir que un script subido/pegado es el que está en producción** sin confirmarlo (ya pasó con `trivia.js`, que resultó ser el script de `/desafio`, no el de `/trivia`).
- **Antes de eliminar código sospechoso de estar huérfano**, verificar con grep/búsqueda en todo el repo (routes, templates, JS) que ningún otro archivo lo consume — no asumir por el nombre.

## Estándar de trabajo obligatorio (loop construir-probar-auditar)

Todo cambio de desarrollo sigue el loop: PLANIFICAR → CONSTRUIR → EJECUTAR → PROBAR → AUDITAR → CORREGIR → VOLVER A PROBAR → ENTREGAR. Reglas clave:

- **"Compila/arranca" no es terminado:** comprobar funcionamiento real (páginas abiertas vía HTTP, respuesta real de APIs, imágenes que cargan con content-type correcto, datos que llegan al usuario).
- **Nunca mostrar:** `None`, `null`, `undefined`, `NaN`, 404, URLs rotas ni texto de debug. Dato faltante → estado explícito profesional ("Imagen no disponible", "Información pendiente de verificación").
- **Imágenes:** verificar identidad del sujeto por API/fuente (no fiarse del nombre del archivo), que la URL responde y es imagen, y registrar fuente+autor+licencia+URL. Coincidencia dudosa → marcar `NEEDS_REVIEW`, nunca confirmar por similitud.
- **Sin licencia compatible → placeholder honesto local** (`app/static/img/ficha-placeholder.svg`); nunca usar imagen protegida para llenar el diseño.
- **Acordes/progresiones:** material didáctico propio declarado como tal en pantalla; no transcribir tabs protegidas.
- **Regresión:** tras modificar algo, revisar funciones relacionadas (navegación, APIs compartidas, estilos, páginas vecinas).
- **Evidencia:** reporte final con tabla de casos de prueba (prueba/acción/resultado PASS-FAIL) distinguiendo VERIFICADO EJECUTANDO vs REVISADO POR INSPECCIÓN. No inventar evidencia jamás.
- **READY solo si:** pruebas críticas pasan, cada requisito del pedido auditado uno a uno, errores corregidos y re-testeados, sin placeholders rotos, sin None visibles, sin errores críticos conocidos.

## Empaquetado

Para generar un `.tar` del proyecto en Git Bash, hacerlo **fuera** de la carpeta del proyecto (si se genera adentro, se auto-incluye). Excluir: `.git`, `.venv`, `__pycache__`, `*.pyc`, `app/static/videos`, `instance`, `node_modules`, `*.tar.gz`.

## Qué NO hacer

- No reintroducir el logo neón del navbar (`fa-compact-disc` + `.neon-sign`) — fue eliminado deliberadamente de `base.html`.
- No usar PowerShell por defecto en este entorno.
- No modificar nada en modo `build` sin que el usuario lo haya pedido explícitamente para esa tarea — para exploración/auditoría, preferir modo `plan` o el subagente `explore` (solo lectura).

## Seguridad — Secretos

**Nunca incluyas valores reales de API keys, tokens o contraseñas en archivos de documentación (.md), reportes, logs commiteados, ni en ningún archivo que no esté en .gitignore.** Usa siempre placeholders como `YOUR_API_KEY_HERE` o referencias a variables de entorno. Esto aplica para humanos y agentes de IA por igual.

El repo tiene un pre-commit hook (`detect-secrets`) que bloquea automáticamente commits que contengan patrones de secretos. Si necesitas agregar un falso positivo al baseline: `detect-secrets scan --update .secrets.baseline`.

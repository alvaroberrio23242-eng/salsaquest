# SalsaQuest - Reglas del proyecto

## Reglas obligatorias

### Git
- Nunca ejecutes git add, commit, push, reset, rebase ni stash sin mi
  autorización explícita en el mismo mensaje.
- Antes de pedir autorización para un commit, muéstrame el git diff.
- El commit y el push son autorizaciones separadas: que yo autorice el
  commit NO implica autorización para el push. Espera confirmación
  explícita para cada uno.

### Sistema de evidencia (no negociable)
- Todo contenido histórico o factual debe clasificarse con uno de estos
  niveles: VERIFIED_PRIMARY, VERIFIED_SECONDARY, ATTRIBUTED, PROBABLE,
  PENDING, CONTRADICTED, DO_NOT_USE.
- Nunca presentes información PENDING, PROBABLE o CONTRADICTED como hecho
  confirmado.
- Términos subjetivos ("capital salsera", "epicentro", "himno", "el más
  importante") requieren atribución explícita a una fuente o deben
  eliminarse — nunca como hecho objetivo.
- "Content Contract": ningún contenido nuevo (fotos, historias, datos)
  entra a producción sin verificación equivalente a la auditoría ya
  hecha. No inventes datos; lo no verificado se marca como PENDING o se
  omite.

### Opiniones de visitantes y enlaces externos
- Nunca copies ni parafrasees reseñas de Google, Tripadvisor, Wanderlog
  ni ninguna otra plataforma. Solo enlaces salientes (target="_blank"
  rel="noopener noreferrer").
- Nunca almacenes ni muestres calificaciones numéricas de terceros
  (rating, score) dentro de SalsaQuest.
- Antes de etiquetar una cuenta de redes sociales como "oficial",
  verifica coherencia con el sitio web del lugar y/o prensa — no asumas
  por el nombre de usuario.

### Fotos
- Solo fuentes reutilizables legalmente: Wikimedia Commons con licencia
  CC-BY/CC0, material propio, o material con autorización explícita.
  Nunca descargues masivamente de Google.
- Categoriza siempre: actual / historica / archivo / prensa /
  oficial_cedida / ilustrativa / propia.
- Cada foto necesita datos de crédito (autor, fuente, licencia). No
  inventes créditos si no los tienes — déjalos vacíos y márcalo como
  pendiente.
- Si una foto es people_identifiable=True, no la publiques sin
  confirmación explícita mía de que hay consentimiento.

### Secretos
- No leas ni imprimas valores de .env, SECRET_KEY, DATABASE_URL ni
  ninguna clave/token, y no los escribas en archivos nuevos.
- Si encuentras un secreto expuesto, repórtalo solo así:
  SECRET DETECTED / FILE / LINE / TYPE / SEVERITY — nunca el valor.
- Verifica si .env está en .gitignore y si hay evidencia de que algún
  secreto haya estado alguna vez en el historial de git (sin mostrar su
  contenido). Un secreto que estuvo en el historial se considera
  comprometido y requiere rotación humana, no borrado del archivo.

### Alcance y arquitectura
- Solo D:\Proyectos\salsaquest. No toques otros proyectos ni hagas
  cambios no relacionados con la tarea.
- No modifiques la ruta /medellin bajo ningún motivo, aunque parezca
  relacionada.
- Los datos editoriales de la Ruta Salsera viven en
  app/models/ruta_salsera_data.py (diccionarios Python) como fuente
  única de verdad. No migres esto a SQLite ni cambies esa arquitectura
  sin que yo lo pida expresamente.
- Cambios pequeños, modulares y por fases. Antes de tocar código,
  explica el plan en pocas líneas.

### Rendimiento y accesibilidad
- Cuida el peso de cualquier multimedia nueva (fotos, animaciones): el
  hosting es Render plan gratuito, sensible al ancho de banda. Los
  videos de fondo ya se comprimieron de ~85-105MB a ~20MB; no repitas
  ese problema con fotos sin optimizar.
- Respeta siempre prefers-reduced-motion y mantén contraste/legibilidad.
- El vehículo cultural del mapa (cuando se implemente) debe ser diseño
  100% original — nunca inspirado en un personaje o marca con derechos
  de autor.

### Tests y verificación
- Después de cambios relevantes, corre la suite de tests tú mismo sin
  pedir permiso y muéstrame el resultado (total/passed/failed).
- No inventes resultados ni afirmes que algo funciona si no lo
  comprobaste ejecutándolo.
- Si pido "solo lectura" o "solo diagnostica", no modifiques nada.

## Estilo de respuesta
- Español, directo y conciso. Resultados en tablas cuando aplique.
  Indica rutas como archivo:línea.

## Contexto técnico
- Stack: Flask + SQLAlchemy + SQLite + Jinja2 + Bootstrap + Leaflet +
  JavaScript + Gunicorn, desplegado en Render (plan gratuito).
- Producción: https://salsaquest-1.onrender.com
- Repositorio: github.com/alvaroberrio23242-eng/salsaquest
- Arquitectura: multipágina (Flask blueprints). / redirige
  automáticamente a /ruta-salsera, que es la puerta de entrada principal
  del sitio.
- Secciones existentes: historia, línea de tiempo, artistas, orquestas,
  música, lugares, Son Havana, trivia/desafío, recursos y fuentes.
- Ruta Salsera (/ruta-salsera): hero con CTA, mapa Leaflet 420px con
  marcadores dorados con glow, 7 filtros por categoría, timeline
  vertical, tarjetas con hover, badges de evidencia en español
  ("Verificado", "Atribuido", "Probable"), SEO básico, accesibilidad
  (prefers-reduced-motion, sin zoom con rueda del mouse en mobile).
- Contenido MVP: 14 eventos de línea de tiempo, 3 lugares (El Tíbiri
  Tábara, Son Havana, El Suave), 11 artistas/orquestas, 1 emisora de
  radio. Todo en español (inglés/francés quedan para el futuro).
- Trabajo en curso: galería de fotos y enlaces externos de Son Havana
  (app/models/son_havana_extra.py, endpoint /api/son-havana-extra),
  aislado de content_data.py y ruta_salsera_data.py.
# ROUTE-SALSERA-PRODUCT-SPEC.md
## Especificación de Producto — La Ruta Salsera de Medellín
### SalsaQuest — Fase 3

**Fecha de especificación:** 18 septiembre 2026
**Arquitecto de producto:** OpenCode (mimo-v2.5-free)
**Documento de autoridad:** `ROUTE-SALSERA-EVIDENCE-AUDIT.md`

---

## 1. EXECUTIVE SUMMARY

**La Ruta Salsera de Medellín** es una experiencia digital dentro de SalsaQuest que documenta la historia, los lugares, la industria discográfica, la radio y los artistas que conforman la identidad salsera de Medellín. No es una landing page informativa: es una experiencia cultural y turística con evidencia verificable.

**Números clave:**
- 52 afirmaciones auditadas forensamente
- 22 VERIFIED_PRIMARY (42%)
- 12 VERIFIED_SECONDARY (23%)
- 7 ATTRIBUTED (13%)
- 14 ítems prohibidos de publicación
- 7 ítems pendientes de investigación
- 35 fuentes verificadas con URLs activas
- 2 contradicciones detectadas

**Decisión arquitectónica fundamental:** La Ruta Salsera NO reemplaza la sección `/medellin` existente. Es un producto nuevo con su propia ruta (`/ruta-salsera`), su propio template, y su propio contrato de contenido. La sección `/medellin` existente permanece como está.

---

## 2. PRODUCT VISION

### Qué es
Una experiencia digital de una sola página que combina línea de tiempo histórica, mapa interactivo, tarjetas de lugares con evidencia documentada, perfiles de artistas y orquestas, y una ruta turística recomendada — todo respaldado por una cadena de evidencia verificable.

### Para quién
Turistas internacionales, visitantes colombianos, salseros/investigadores, y usuarios existentes de SalsaQuest.

### Qué problema resuelve
Medellín no tiene una guía digital consolidada, verificable y navegabl de su identidad salsera. La información está dispersa en blogs, directorios, redes sociales y fuentes contradictorias. La Ruta resuelve esto con evidencia documentada.

### Propuesta de valor
Primera guía digital de la salsa en Medellín con evidencia trazable y clasificada. No es un blog de viajes: es una experiencia cultural con estándares de verificación.

### Diferenciador
Cada afirmación lleva un indicador de evidencia (Documentado, Fuente secundaria, Atribuido, En verificación). Ningún otro producto de turismo musical en Medellín ofrece transparencia de fuentes.

### Contexto cultural
Medellín fue sede de Discos Fuentes (la primera discográfica de música tropical en Colombia), Codiscos, y múltiples orquestas que definieron la salsa colombiana. Esta identidad es documentable con fuentes primarias.

### Contexto turístico
SalsaQuest opera en Son Havana, un bar de salsa en Laureles. La Ruta conecta la experiencia de Son Havana con el contexto histórico más amplio de la ciudad.

### Relación con SalsaQuest
La Ruta es un módulo dentro del ecosistema SalsaQuest. No es un producto independiente. Comparte navbar, footer, sistema de estilos, y infraestructura técnica.

### Relación con Son Havana
Son Havana aparece como parada documentada en la Ruta, con la misma evidencia verificada que cualquier otro lugar. No tiene tratamiento preferencial editorial.

### Objetivo de negocio
Posicionar SalsaQuest como referencia cultural para turismo salsero en Medellín. Atraer visitantes que buscan "salsa Medellín" o "ruta salsera Medellín" en buscadores.

### Objetivo de experiencia
Que el usuario comprenda la historia de la salsa en Medellín, identifique lugares que puede visitar, y tenga una ruta recomendada — todo con confianza en la información.

### Objetivo de aprendizaje cultural
Que el usuario entienda que Medellín no es solo sede de Discos Fuentes, sino un ecosistema completo de industria, radio, artistas y lugares que conforman una tradición salsera viva.

---

## 3. PRODUCT GOALS

| # | Goal | Métrica | Prioridad |
|---|------|---------|-----------|
| G1 | Que el usuario pueda navegar la historia de la salsa en Medellín por década | % de décadas con al menos 1 evento VERIFIED | Alta |
| G2 | Que el usuario pueda identificar lugares actuales de salsa en Medellín | Número de lugares con dirección verificada | Alta |
| G3 | Que cada afirmación lleve indicador de evidencia | 100% de claims con evidence_status | Alta |
| G4 | Que el usuario pueda abrir ubicación en Google Maps desde cualquier lugar | Todos los lugares con lat/lng | Alta |
| G5 | Que la experiencia funcione en mobile | Core Web Vitals GOOD en mobile | Alta |
| G6 | Que el SEO capture búsquedas de "salsa Medellín" | Impressions en Search Console | Media |
| G7 | Que el usuario pueda compartir la ruta | CTA de compartir funcional | Media |
| G8 | Que la experiencia sea accesible (WCAG 2.2 AA) | Lighthouse accessibility ≥90 | Media |

---

## 4. NON-GOALS

| # | Non-Goal | Razón |
|---|----------|-------|
| NG1 | No es un reseñador de bares | No damos opiniones sobre calidad de servicio |
| NG2 | No es una enciclopedia completa | No cubrimos toda la historia de la salsa, solo Medellín |
| NG3 | No es una tienda de entradas | No vendemos tickets |
| NG4 | No es un sustituto de Google Maps | Usamos Leaflet para el mapa interactivo, no replicamos funcionalidad completa |
| NG5 | No es una red social | No hay comentarios, reviews o perfiles de usuario |
| NG6 | No es una app nativa | Es web, responsive, no requiere instalación |
| NG7 | No inventamos datos faltantes | Preferimos mostrar "En verificación" a rellenar vacíos |
| NG8 | No convertimos el contenido en publicidad | Los CTAs respetan el propósito cultural |

---

## 5. TARGET USERS

### Persona A — Visitante internacional

**Necesidad:** Comprender la escena salsera de Medellín antes de llegar o durante su visita.

**Intención:** Encontrar lugares de salsa, entender la historia, tener una ruta.

**Preguntas:**
- ¿Dónde puedo bailar salsa en Medellín?
- ¿Cuál es la historia de la salsa en Medellín?
- ¿Qué lugares debo visitar?
- ¿Son Havana es un buen lugar?
- ¿Hay eventos de salsa próximamente?

**Contenido que busca:** Lugares actuales, mapa, ruta recomendada, eventos.

**Acción deseada:** Visitar 2-3 lugares de salsa durante su estadía.

**Fricciones:** Idioma (necesita EN/FR), no conoce la ciudad, no sabe distinguir lugares turísticos de lugares auténticos.

### Persona B — Visitante colombiano

**Necesidad:** Descubrir o redescubrir la historia musical de Medellín.

**Intención:** Conectar con la identidad cultural de la ciudad.

**Preguntas:**
- ¿Cuál fue el rol de Discos Fuentes?
- ¿Qué orquestas nacieron en Medellín?
- ¿Dónde quedaba la Calle Palacé?
- ¿Qué emisoras promueven la salsa?

**Contenido que busca:** Timeline histórica, industria discográfica, orquestas, radio.

**Acción deseada:** Compartir la historia con amigos/familia, visitar places históricos.

**Fricciones:** Puede asumir que ya sabe la historia y saltarse secciones.

### Persona C — Salsero / investigador

**Necesidad:** Verificar datos, encontrar fuentes, profundizar en la historia.

**Intención:** Encontrar información documentada y confiable.

**Preguntas:**
- ¿Cuándo se fundó exactamente Discos Fuentes?
- ¿Cuál es la fuente de la fecha de fundación de El Tíbiri?
- ¿Qué libros existen sobre la salsa en Medellín?
- ¿Cuáles son las fuentes primarias?

**Contenido que busca:** Fuentes, fechas exactas, datos verificados, bibliografía.

**Acción deseada:** Citar la información en su propio trabajo.

**Fricciones:** Necesita ver la evidencia, no solo el dato.

### Persona D — Usuario de SalsaQuest

**Necesidad:** Explorar la sección de Medellín dentro del ecosistema SalsaQuest.

**Intención:** Descubrir contenido nuevo relacionado con lo que ya conoce.

**Preguntas:**
- ¿Qué hay de nuevo en SalsaQuest sobre Medellín?
- ¿Cómo se conecta la historia de la salsa con Son Havana?
- ¿Puedo encontrar eventos próximos?

**Contenido que busca:** Contenido integrado con el resto de SalsaQuest, eventos, enlaces a otras secciones.

**Acción deseada:** Navegar entre la Ruta y otras secciones de SalsaQuest.

**Fricciones:** Puede no entender por qué la información tiene indicadores de evidencia.

---

## 6. USER JOURNEYS

### Journey principal: Descubrimiento completo

```
Entrada (/ruta-salsera)
  → Hero con título y contexto
  → Intro: "¿Por qué Medellín y la salsa?"
  → Timeline histórica (scroll horizontal por décadas)
  → Industria discográfica (Discos Fuentes, Codiscos)
  → Radio (Latina Stereo)
  → Artistas y orquestas
  → Lugares actuales (tarjetas)
  → Mapa (Leaflet con marcadores)
  → Ruta recomendada ("Recorre la Ruta")
  → Son Havana (sección integrada)
  → Fuentes y evidencia
  → CTA: "Explorar SalsaQuest"
```

### Journey alternativo: Solo lugares

```
Entrada (/ruta-salsera)
  → Scroll directo a Lugares actuales
  → Tarjetas con dirección y horarios
  → Mapa con marcadores
  → Abrir en Google Maps
  → Visitar lugar
```

### Journey alternativo: Solo historia

```
Entrada (/ruta-salsera)
  → Scroll directo a Timeline
  → Explorar décadas
  → Ver industria discográfica
  → Ver orquestas
  → Ver fuentes
```

### Journey alternativo: Desde Google (SEO)

```
Búsqueda: "salsa bars medellín" / "historia salsa medellín"
  → Landing page (/ruta-salsera)
  → Scroll a sección más relevante
  → Mapa / lugares / historia según intención
  → CTA: "Conocer Son Havana" o "Ver eventos"
```

### Journey alternativo: Desde Son Havana

```
Usuario en Son Havana → QR / enlace → /ruta-salsera
  → Sección de Son Havana (contexto histórico)
  → Lugares cercanos (El Tíbiri, ~600m)
  → Ruta recomendada
  → CTA: "Compartir la ruta"
```

### Journey alternativo: Navegación en inglés/francés

```
Búsqueda en inglés: "salsa medellín"
  → /ruta-salsera?lang=en
  → Contenido traducido
  → Nombres propios sin traducir
  → Fuentes sin traducir
```

---

## 7. INFORMATION ARCHITECTURE

### Estructura de módulos

```
La Ruta Salsera de Medellín (/ruta-salsera)
│
├── 1. Hero
│   ├── Título: "La Ruta Salsera de Medellín"
│   ├── Subtítulo: "Historia, lugares y cultura salsera"
│   └── CTA: "Explorar la ruta"
│
├── 2. Introducción — ¿Por qué Medellín y la salsa?
│   ├── Contexto: Discos Fuentes, Codiscos, industriamúsica tropical
│   ├── Conexión con SalsaQuest
│   └── Indicador: "Contenido documentado"
│
├── 3. Línea del tiempo
│   ├── Filtros por década
│   ├── Timeline horizontal/vertical
│   ├── Eventos VERIFIED con indicador de evidencia
│   └── Expansión por evento ( detalle + fuente)
│
├── 4. Industria discográfica
│   ├── Discos Fuentes (1934, Cartagena → Medellín)
│   ├── Codiscos (1950, Medellín)
│   ├── Relación con la salsa
│   └── Fuentes
│
├── 5. Radio
│   ├── Latina Stereo 100.9 FM
│   ├── "Salsa desde 1985"
│   └── Fuentes
│
├── 6. Músicos y orquestas
│   ├── Fruko y sus Tesos
│   ├── Grupo Galé
│   ├── Otras orquestas documentadas
│   └── Distinción persona/orquesta/registro
│
├── 7. Lugares actuales
│   ├── El Tíbiri Tábara
│   ├── Son Havana
│   ├── El Suave
│   ├── Tarjetas con dirección, horario, evidencia
│   └── CTA: "Abrir en Maps"
│
├── 8. Mapa
│   ├── Leaflet con marcadores
│   ├── Categorías: lugares actuales, históricos (si aplica)
│   ├── Popup con ficha resumen
│   └── CTA: "Abrir en Google Maps"
│
├── 9. Ruta recomendada
│   ├── Recorrido sugerido a pie
│   ├── Paradas con orden
│   ├── Tiempo estimado (si disponible, si no: PENDING)
│   └── CTA: "Compartir ruta"
│
├── 10. Son Havana
│   ├── Información del local (verificada)
│   ├── Enlace a página de Son Havana en SalsaQuest
│   └── Separación clara de entidades
│
├── 11. Fuentes y evidencia
│   ├── Tabla de fuentes clasificadas
│   ├── Niveles A, B, C, D
│   ├── Enlaces a fuentes primarias
│   └── Última verificación
│
├── 12. CTA
│   ├── "Explorar SalsaQuest"
│   ├── "Compartir la ruta"
│   └── "Descubrir eventos"
│
└── 13. Footer (compartido con SalsaQuest)
```

### Clasificación de módulos

| Módulo | MVP | V1 | Future | Justificación |
|--------|-----|----|--------|---------------|
| Hero | SÍ | — | — | Entrada esencial |
| Introducción | SÍ | — | — | Contexto mínimo necesario |
| Timeline | SÍ | — | — | Core del producto |
| Industria discográfica | SÍ | — | — | Solo 2 entidades documentadas |
| Radio | SÍ | — | — | Solo 1 emisora documentada |
| Artistas y orquestas | SÍ | — | — | 11 orquestas + 2 personas documentadas |
| Lugares actuales | SÍ | — | — | 3 lugares con datos operativos verificados |
| Mapa | SÍ | — | — | Los 3 lugares tienen coordenadas |
| Ruta recomendada | NO | SÍ | — | Requiere cálculo de distancias/tiempos |
| Son Havana | SÍ | — | — | Conexión con ecosistema SalsaQuest |
| Fuentes y evidencia | NO | SÍ | — | MVP no necesita tabla completa |
| CTA | SÍ | — | — | Conversión mínima |
| Footer | SÍ | — | — | Compartido con SalsaQuest |
| Calle Palacé | NO | NO | SÍ | Sin evidencia de bares específicos |
| "Renacimiento salsa brava" | NO | NO | SÍ | Expresión no documentada |
| i18n (EN/FR) | NO | SÍ | — | Requiere estrategia de traducción |
| Eventos próximos | NO | SÍ | — | Requiere fuente de datos actualizada |

---

## 8. CONTENT CONTRACT

### AUTHORIZED

Contenido autorizado para publicación directa como hecho documentado.

| ID | Contenido | Fuente | Estado |
|----|-----------|--------|--------|
| A01 | Discos Fuentes fundada en 1934 en Cartagena | Sitio oficial DF + Wikipedia | VERIFIED_PRIMARY |
| A02 | Codiscos fundada el 1 de julio de 1950 en Medellín | Sitio oficial Codiscos + El Colombiano | VERIFIED_PRIMARY |
| A03 | Julio Ernesto Estrada "Fruko" nació el 7 de julio de 1951 en Medellín | Sitio oficial DF + AllMusic | VERIFIED_PRIMARY |
| A04 | Fruko ingresa a Discos Fuentes en 1963, a los 12 años | AllMusic + Wikipedia | VERIFIED_PRIMARY |
| A05 | Fruko y sus Tesos fundada en 1970 en Medellín | Sitio oficial DF | VERIFIED_PRIMARY |
| A06 | Primer éxito: "A la memoria del muerto" — Píper Pimienta Díaz | Sitio oficial DF | VERIFIED_PRIMARY |
| A07 | "El Preso" grabada en 1975 — Wilson Manyoma "Saoko" | Sitio oficial DF + El Tiempo | VERIFIED_PRIMARY |
| A08 | Grupo Galé fundado en 1989 en Medellín | Wikipedia + sitio oficial | VERIFIED_PRIMARY |
| A09 | Diego Galé fue percusionista de Grupo Niche | Apple Music + Wikipedia | VERIFIED_SECONDARY |
| A10 | *Auténtico* (2007) nominado a Latin Grammy | Wikipedia EN | VERIFIED_SECONDARY |
| A11 | Latina Stereo 100.9 FM, "Salsa desde 1985" | Sitio oficial + TuneIn | VERIFIED_PRIMARY |
| A12 | Son Havana: Carrera 73 #44-56, Florida Nueva, Laureles | Dancefree + Evendo + Instagram | VERIFIED_PRIMARY |
| A13 | Son Havana All Stars (grupo propio) | Dancefree + Instagram | VERIFIED_PRIMARY |
| A14 | Son Havana: Rueda de Casino los miércoles | Dancefree | VERIFIED_PRIMARY |
| A15 | El Tíbiri: Cra 70 #70-03, sótano, Laureles | ColombiaBZ + 2POS + Real City Tours | VERIFIED_PRIMARY |
| A16 | El Tíbiri: teléfono +57 310 8495461 | ColombiaBZ + 2POS | VERIFIED_PRIMARY |
| A17 | El Tíbiri: Facebook facebook.com/tibiri.bar | ColombiaBZ | VERIFIED_PRIMARY |
| A18 | El Tíbiri: salsa clásica, son cubano, guaguancó | ColombiaBZ (reseñas) + Real City Tours | VERIFIED_PRIMARY |
| A19 | El Suave: Av. 33 #80a-30, Medellín | 2POS | VERIFIED_PRIMARY |
| A20 | El Suave: teléfono +57 310 4593267 | 2POS | VERIFIED_PRIMARY |
| A21 | El Suave: "salsa & sabor" | 2POS | VERIFIED_PRIMARY |
| A22 | Viva la Salsa 2026 — 25 julio, Estadio Atanasio Girardot | Canal Trece | VERIFIED_PRIMARY |
| A23 | Las Leyendas Vivas de la Salsa — 10a edición | Comfenalco | VERIFIED_PRIMARY |
| A24 | Santana — *¿Qué es la Salsa?* Medellín 1992 | U. del Valle bibliography | VERIFIED_PRIMARY |
| A25 | Jaramillo — *Música tropical y salsa en Colombia* 1992 | Resonancias UC | VERIFIED_PRIMARY |
| A26 | El Tíbiri: horarios Mié-Sáb 21:00-03:00 (sujeto a cambios) | 2POS | VERIFIED_PRIMARY |
| A27 | El Suave: horarios Lun-Sáb 16:00-03:00, Dom 16:00-00:00 | 2POS | VERIFIED_PRIMARY |
| A28 | Son Havana: horarios Mié-Jue hasta medianoche, Vie-Sáb hasta 4am | Dancefree + Evendo | VERIFIED_PRIMARY |

### ATTRIBUTED

Contenido publicable SOLO indicando claramente quién lo afirma o cuál es la fuente.

| ID | Contenido | Atribución | Fuente |
|----|-----------|------------|--------|
| AT01 | "El Preso" es considerada un himno de la salsa | Discos Fuentes + El Tiempo | Sitio oficial DF |
| AT02 | Para 1976 Fruko era "la mejor orquesta del país" | Discos Fuentes | Sitio oficial DF |
| AT03 | Fruko fue "el pionero de la salsa colombiana" | Discos Fuentes | Sitio oficial DF |
| AT04 | Discos Fuentes es descrita como "la Motown colombiana" | Wikipedia EN | Wikipedia |
| AT05 | Calle Palacé fue epicentro de la vida salsera | Latina Stereo | latinastereo.com |
| AT06 | Latina Stereo difundió salsa clásica y dura desde 1985 | Latina Stereo | latinastereo.com |
| AT07 | Latina Stereo presentó Los Hermanos Lebrón, El Gran Combo, Fania All Stars | Latina Stereo | latinastereo.com |
| AT08 | Héctor Lavoe en fiesta de Año Nuevo 1981 en hacienda de Pablo Escobar | Eddie Montalvo (conguero) | Revista Mundo Diners |
| AT09 | Fruko viaja a Nueva York en 1968 | Wikipedia EN (referencia no localizada) | Wikipedia |
| AT10 | Apodo "Fruko" proviene de muñeco publicitario FRUCO | Wikipedia EN | Wikipedia |
| AT11 | Distancia El Tíbiri — Son Havana: ~600-800m | Cálculo basado en direcciones | Cálculo propio |
| AT12 | 75% del catálogo de Discos Fuentes era música tropical | Resonancias UC (2024) | Artículo académico |

### PENDING

No publicar como hecho. Solo mostrar como "En verificación" o "Pendiente de confirmación".

| ID | Contenido | Estado actual | Acción necesaria |
|----|-----------|---------------|------------------|
| P01 | El Tíbiri: fecha de fundación | Sin fuente confiable | Investigación adicional |
| P02 | Son Havana: fundador Julio Restrepo Molina | Solo Instagram | Verificar en fuente institucional |
| P03 | Son Havana: segundo local en El Poblado | 2 fuentes no cruzadas | Verificar direcciones |
| P04 | El Tíbiri: Instagram / propietarios actuales | No encontrado | Investigación adicional |
| P05 | El Suave: historia completa | Sin evidencia | Investigación en archivo de prensa |
| P06 | El Suave: Instagram @discotecaelsuave | No verificado | Verificar existencia |
| P07 | Investigadores musicales de Medellín | Sin resultados | Buscar en catálogos universitarios |

### CONTRADICTED

No publicar hasta resolver la contradicción. Si se publica, debe incluir ambas versiones con fuentes.

| ID | Contenido | Versión A | Versión B | Resolución propuesta |
|----|-----------|-----------|-----------|---------------------|
| C01 | Traslado de Discos Fuentes a Medellín | 1954 (Wikipedia ES) | 1960 (sitio oficial DF) | "Entre 1954 y 1960" |
| C02 | Fundación de Fruko y sus Tesos | 1969 (Wikipedia EN) | 1970 (sitio oficial DF) | Priorizar fuente primaria: 1970 |

### DO_NOT_USE

Prohibido utilizar en el producto bajo cualquier circunstancia.

| ID | Contenido | Razón |
|----|-----------|-------|
| D01 | El Tíbiri fue fundado en 1992 | Sin evidencia |
| D02 | El Suave existe desde 1962 | Sin evidencia |
| D03 | El Suave fue fundado por Bernardo Arango | Sin evidencia |
| D04 | Bernardo "Malagente" Arango, segunda generación | Sin evidencia |
| D05 | Nancy Díaz, Catalina Arango, tercera generación | Sin evidencia |
| D06 | "Renacimiento de la salsa brava" como categoría factual | Expresión no encontrada en fuentes |
| D07 | Bares específicos de Calle Palacé (Aristi, Brisas de Costa Rica, Carruseles, El Conde, El Semáforo, El Diferente, El Ceilán, La Titular) | Sin evidencia documental |
| D08 | "El Preso" ha sido bailada en más de 70 países | Distorsión de dato |
| D09 | Instagram @discotecaelsuave | No verificado |
| D10 | El Tíbiri tiene Instagram | No encontrado |
| D11 | Hernán Darío Usquiano como investigador | No encontrado |
| D12 | Fecha exacta de fundación de El Tíbiri | Sin fuente confiable |
| D13 | "Capital salsera" como hecho factual | Es valoración |
| D14 | "Epicentro" como hecho factual | Es valoración |

---

## 9. EVIDENCE RULES

### Reglas de publicación por estado

| Estado | Regla | Ejemplo |
|--------|-------|---------|
| VERIFIED_PRIMARY | Publicar como hecho documentado. Fuente primaria verificada. | "Discos Fuentes fue fundada en 1934" |
| VERIFIED_SECONDARY | Publicar como hecho respaldado por fuente secundaria reconocida. | "Fruko viaja a Nueva York en 1968" |
| ATTRIBUTED | DEBE indicar atribución explícita. Nunca como hecho propio. | "Discos Fuentes es descrita como 'la Motown colombiana'" |
| PROBABLE | NO presentarlo como hecho. Usar lenguaje de probabilidad. | "Según una fuente, El Tíbiri pudo haber abierto en ~1996" |
| PENDING | NO publicarlo como hecho. Mostrar como "En verificación". | "Fecha de fundación: en proceso de verificación" |
| CONTRADICTED | NO publicarlo hasta resolver conflicto. Si se publica, incluir ambas versiones. | "Según Discos Fuentes, 1960. Según Wikipedia, 1954." |
| DO_NOT_USE | Excluir completamente del producto. | — |

### Cadena de evidencia obligatoria

```
Fuente → Evidence Audit → Content Contract → Product Spec → Implementation → QA
```

Ningún dato puede saltarse un paso.

### Indicador de evidencia en UI

Cada claim visible llevará un badge discreto:

| Badge | Color | Significado |
|-------|-------|-------------|
| 📄 Documentado | Verde | VERIFIED_PRIMARY |
| 📰 Fuente secundaria | Azul | VERIFIED_SECONDARY |
| 🏷️ Atribuido | Amarillo | ATTRIBUTED |
| ⏳ En verificación | Gris | PENDING |
| ⚠️ En disputa | Naranja | CONTRADICTED |

---

## 10. CONTENT INVENTORY

| Elemento | Estado | Publicable | Atribución | Fuente | Acción |
|----------|--------|------------|------------|--------|--------|
| Discos Fuentes 1934 | VERIFIED_PRIMARY | SÍ | — | Sitio oficial DF | Implementar |
| Discos Fuentes traslado Medellín | CONTRADICTED | CUIDADO | — | DF/Wikipedia | Usar rango "1954-1960" |
| 75% catálogo tropical | VERIFIED_SECONDARY | SÍ | Resonancias UC | Artículo académico | Implementar con atribución |
| Codiscos 1950 | VERIFIED_PRIMARY | SÍ | — | Sitio oficial Codiscos | Implementar |
| Fruko nació 1951 | VERIFIED_PRIMARY | SÍ | — | Sitio oficial DF | Implementar |
| Fruko ingresa DF 1963 | VERIFIED_PRIMARY | SÍ | — | AllMusic | Implementar |
| Fruko viaja NY 1968 | VERIFIED_SECONDARY | SÍ | — | Wikipedia | Implementar |
| Fruko y sus Tesos 1970 | VERIFIED_PRIMARY | SÍ | — | Sitio oficial DF | Implementar |
| "A la memoria del muerto" | VERIFIED_PRIMARY | SÍ | — | Sitio oficial DF | Implementar |
| "El Preso" 1975 | VERIFIED_PRIMARY | SÍ | — | DF + El Tiempo | Implementar |
| "El Preso" himno | ATTRIBUTED | SÍ | DF + El Tiempo | Sitio oficial DF | Implementar con atribución |
| Fruko mejor orquesta 1976 | ATTRIBUTED | SÍ | Discos Fuentes | Sitio oficial DF | Implementar con atribución |
| Fruko pionero | ATTRIBUTED | SÍ | Discos Fuentes | Sitio oficial DF | Implementar con atribución |
| Apodo de FRUCO | VERIFIED_SECONDARY | SÍ | Wikipedia | Wikipedia | Implementar |
| Discos Fuentes "Motown" | ATTRIBUTED | SÍ | Wikipedia EN | Wikipedia | Implementar con atribución |
| Grupo Galé 1989 | VERIFIED_PRIMARY | SÍ | — | Wikipedia + oficial | Implementar |
| Diego Galé en Niche/Lavoe | VERIFIED_SECONDARY | SÍ | — | Apple Music | Implementar |
| *Auténtico* Latin Grammy | VERIFIED_SECONDARY | SÍ | — | Wikipedia | Implementar |
| Latina Stereo 100.9 FM | VERIFIED_PRIMARY | SÍ | — | Sitio oficial | Implementar |
| Latina Stereo desde 1985 | ATTRIBUTED | SÍ | Latina Stereo | Sitio oficial | Implementar con atribución |
| Latina Stereo artistas | ATTRIBUTED | SÍ | Latina Stereo | Sitio oficial | Implementar con atribución |
| Son Havana 2010 | VERIFIED_SECONDARY | SÍ | — | Dancefree + Evendo | Implementar |
| Son Havana dirección | VERIFIED_PRIMARY | SÍ | — | Múltiples fuentes | Implementar |
| Son Havana All Stars | VERIFIED_PRIMARY | SÍ | — | Dancefree | Implementar |
| Son Havana Rueda miércoles | VERIFIED_PRIMARY | SÍ | — | Dancefree | Implementar |
| Son Havana fundador | PROBABLE | NO como hecho | — | Instagram | Omitir o atribuir |
| Son Havana 2do local | PROBABLE | NO | — | Real City Tours | Omitir |
| El Tíbiri dirección | VERIFIED_PRIMARY | SÍ | — | Múltiples fuentes | Implementar |
| El Tíbiri teléfono | VERIFIED_PRIMARY | SÍ | — | ColombiaBZ + 2POS | Implementar |
| El Tíbiri Facebook | VERIFIED_PRIMARY | SÍ | — | ColombiaBZ | Implementar |
| El Tíbiri sótano | VERIFIED_PRIMARY | SÍ | — | Múltiples reseñas | Implementar |
| El Tíbiri estilo | VERIFIED_PRIMARY | SÍ | — | Reseñas | Implementar |
| El Tíbiri horarios | VERIFIED_PRIMARY | SÍ | — | 2POS | Implementar |
| El Tíbiri fundación ~1996 | PROBABLE | NO como fecha | — | mbailomedellin | Omitir fecha |
| El Tíbiri fundación 1992 | DO_NOT_USE | NO | — | — | Eliminar |
| El Tíbiri Instagram | PENDING | NO | — | — | Omitir |
| El Suave dirección | VERIFIED_PRIMARY | SÍ | — | 2POS | Implementar |
| El Suave teléfono | VERIFIED_PRIMARY | SÍ | — | 2POS | Implementar |
| El Suave estilo | VERIFIED_PRIMARY | SÍ | — | 2POS | Implementar |
| El Suave horarios | VERIFIED_PRIMARY | SÍ | — | 2POS | Implementar |
| El Suave desde 1962 | DO_NOT_USE | NO | — | — | Eliminar |
| El Suave Bernardo Arango | DO_NOT_USE | NO | — | — | Eliminar |
| El Suave Instagram | PENDING | NO | — | — | Omitir |
| Calle Palacé epicentro | ATTRIBUTED | SÍ | Latina Stereo | latinastereo.com | Implementar con atribución |
| Bares de Palacé | DO_NOT_USE | NO | — | — | Eliminar |
| Héctor Lavoe 1981 | PROBABLE | SÍ con atribución | Eddie Montalvo | Mundo Diners | Implementar con atribución |
| "Renacimiento salsa brava" | DO_NOT_USE | NO | — | — | Eliminar |
| Viva la Salsa 2026 | VERIFIED_PRIMARY | SÍ | — | Canal Trece | Implementar |
| Leyendas Vivas X | VERIFIED_PRIMARY | SÍ | — | Comfenalco | Implementar |
| Santana *¿Qué es la Salsa?* | VERIFIED_PRIMARY | SÍ | — | U. del Valle | Implementar como referencia |
| Jaramillo *Música tropical* | VERIFIED_PRIMARY | SÍ | — | Resonancias UC | Implementar como referencia |
| Distancia Tíbiri-Son Havana | ATTRIBUTED | SÍ como cálculo | — | Cálculo propio | Implementar con nota |

---

## 11. CONTENT OBJECTS

### HistoricalEvent

```python
{
    "id": str,                    # "discos-fuentes-1934"
    "title": str,                 # "Discos Fuentes fundada en Cartagena"
    "year_start": str,            # "1934"
    "year_end": str | None,       # None
    "category": str,              # "industria" | "orquesta" | "radio" | "lugar" | "evento" | "persona"
    "description": str,           # Texto descriptivo
    "location": str | None,       # "Cartagena, Colombia"
    "people": list[str],          # ["Antonio Fuentes"]
    "organizations": list[str],   # ["Discos Fuentes"]
    "evidence_status": str,       # "VERIFIED_PRIMARY" | "VERIFIED_SECONDARY" | "ATTRIBUTED"
    "confidence": str,            # "high" | "medium" | "low"
    "sources": list[SourceRef],   # Referencias a fuentes
    "attribution": str | None,    # "Según Discos Fuentes..." (si aplica)
    "last_verified": str,         # "2026-09-18"
    "display_order": int          # Para ordenar en UI
}
```

### Venue

```python
{
    "id": str,                    # "el-tibiri"
    "name": str,                  # "El Tíbiri Tábara"
    "type": str,                  # "bar" | "discoteca" | "salón"
    "historical_period": str | None,  # None (no documentado como histórico)
    "address": str,               # "Cra 70 #70-03, Laureles"
    "neighborhood": str,          # "Laureles"
    "city": str,                  # "Medellín"
    "coordinates": {
        "lat": float,
        "lng": float
    },
    "phone": str | None,          # "+57 310 8495461"
    "whatsapp_url": str | None,
    "instagram": str | None,
    "facebook": str | None,
    "website": str | None,
    "description": str,
    "music_style": str,           # "Salsa clásica, son cubano, guaguancó"
    "status": str,                # "active" | "closed" | "unknown"
    "operating_hours": str | None, # "Mié-Sáb 21:00-03:00"
    "is_underground": bool,       # True (sótano)
    "evidence_status": str,
    "confidence": str,
    "sources": list[SourceRef],
    "attribution": str | None,
    "last_verified": str,
    "external_links": {
        "google_maps": str | None,
        "tripadvisor": str | None
    }
}
```

### ArtistOrchestra

```python
{
    "id": str,                    # "fruko-y-sus-tesos"
    "name": str,                  # "Fruko y sus Tesos"
    "entity_type": str,           # "orchestra" | "person" | "group"
    "founding_year": str | None,  # "1970"
    "founding_location": str | None,  # "Medellín"
    "label": str | None,          # "Discos Fuentes"
    "related_people": list[str],  # ["Julio Ernesto Estrada"]
    "related_groups": list[str],  # ["Grupo Niche"]
    "contribution": str,          # "Pionero de la salsa colombiana"
    "notable_works": list[str],   # ["El Preso", "A la memoria del muerto"]
    "image_url": str | None,
    "image_credit": CreditInfo | None,
    "evidence_status": str,
    "sources": list[SourceRef],
    "attribution": str | None,
    "last_verified": str
}
```

### RadioStation

```python
{
    "id": str,                    # "latina-stereo"
    "name": str,                  # "Latina Stereo"
    "frequency": str,             # "100.9 FM"
    "call_sign": str | None,      # "HJQO"
    "founding_period": str,       # "~1985"
    "slogan": str,                # "Salsa desde 1985"
    "role": str,                  # "Difusión de salsa clásica y dura"
    "location": str,              # "Medellín"
    "evidence_status": str,
    "sources": list[SourceRef],
    "attribution": str | None,
    "last_verified": str
}
```

### SourceRef

```python
{
    "source_id": str,             # "RS-001"
    "title": str,                 # "Discos Fuentes — Acerca"
    "publisher": str,             # "Discos Fuentes"
    "author": str | None,         # None
    "url": str,                   # "https://discosfuentes.com.co/acerca"
    "publication_date": str | None,
    "source_level": str,          # "A" | "B" | "C" | "D"
    "access_date": str,           # "2026-09-18"
    "claim_ids": list[str]        # ["RS-001", "RS-002"]
}
```

### RouteStop

```python
{
    "stop_id": str,               # "stop-1-el-tibiri"
    "sequence": int,              # 1
    "venue_id": str,              # "el-tibiri"
    "coordinates": {
        "lat": float,
        "lng": float
    },
    "estimated_visit_time_min": int | None,  # 60 o None si no disponible
    "category": str,              # "current_venue" | "historical_site" | "landmark"
    "description": str,
    "evidence_status": str,
    "cta": {
        "label": str,             # "Abrir en Maps"
        "url": str,
        "type": str               # "external" | "internal"
    }
}
```

---

## 12. PAGE BLUEPRINT

```text
/ruta-salsera
│
├── HEADER (heredado de base.html — navbar SalsaQuest)
│
├── HERO
│   ├── bg: imagen/video estático de Medellín
│   ├── h1: "La Ruta Salsera de Medellín"
│   ├── p: "Historia, lugares y cultura salsera documentados"
│   ├── badge: "Contenido documentado" (evidence indicator)
│   └── CTA: "Explorar la ruta" (scroll a timeline)
│
├── SECCIÓN: ¿Por qué Medellín y la salsa?
│   ├── card: Contexto (2-3 párrafos)
│   ├── mentions: Discos Fuentes, Codiscos, industria musical
│   └── badge: "Documentado" (evidence indicator)
│
├── SECCIÓN: Línea del Tiempo
│   ├── h2: "La historia de la salsa en Medellín"
│   ├── filtros por década (botones)
│   ├── timeline-container (scroll horizontal en mobile, vertical en desktop)
│   │   ├── 1934 — Discos Fuentes fundada
│   │   ├── 1950 — Codiscos fundada
│   │   ├── ~1954-1960 — Discos Fuentes a Medellín (rango, contradictado)
│   │   ├── 1963 — Fruko ingresa a DF
│   │   ├── 1968 — Fruko viaja a NY
│   │   ├── 1970 — Fruko y sus Tesos
│   │   ├── 1975 — "El Preso"
│   │   ├── 1985 — Latina Stereo
│   │   ├── 1989 — Grupo Galé
│   │   ├── ~1996 — El Tíbiri (aproximado)
│   │   ├── 2010 — Son Havana
│   │   └── 2026 — Viva la Salsa / Leyendas Vivas
│   └── cada evento: título, año, descripción, badge evidencia, fuente
│
├── SECCIÓN: Industria Discográfica
│   ├── h2: "Los sellos que hicieron la salsa"
│   ├── card: Discos Fuentes (1934, Cartagena → Medellín)
│   │   ├── descripción
│   │   ├── 75% catálogo tropical (con atribución)
│   │   ├── "Motown colombiana" (con atribución)
│   │   └── enlace: discosfuentes.com.co
│   └── card: Codiscos (1950, Medellín)
│       ├── descripción
│       └── enlace: codiscos.com
│
├── SECCIÓN: Radio
│   ├── h2: "La voz de la salsa"
│   └── card: Latina Stereo 100.9 FM
│       ├── "Salsa desde 1985" (con atribución)
│       ├── artistas presentados (con atribución)
│       └── enlace: latinastereo.com
│
├── SECCIÓN: Artistas y Orquestas
│   ├── h2: "Músicos y orquestas de Medellín"
│   ├── grid de cards:
│   │   ├── Fruko y sus Tesos (persona + orquesta separadas)
│   │   ├── Grupo Galé
│   │   ├── The Latin Brothers
│   │   ├── Afrosound
│   │   ├── Wganda Kenya
│   │   ├── Pachanga Orquesta
│   │   ├── Sonora 8
│   │   ├── Siguarajazz
│   │   ├── La Pregonera
│   │   ├── La Contundente
│   │   └── La Malandanza
│   └── cada card: nombre, tipo, año, sello, contribución, evidencia
│
├── SECCIÓN: Lugares Actuales
│   ├── h2: "Donde vive la salsa hoy"
│   ├── grid de venue cards:
│   │   ├── El Tíbiri Tábara
│   │   ├── Son Havana
│   │   └── El Suave
│   └── cada card: nombre, dirección, teléfono, horarios, estilo, evidencia, CTA Maps
│
├── SECCIÓN: Mapa
│   ├── h2: "Mapa de la Ruta"
│   ├── div#mapa-ruta-salsera (Leaflet)
│   ├── marcadores con popup
│   └── CTA: "Abrir mapa completo"
│
├── SECCIÓN: Ruta Recomendada (V1)
│   ├── h2: "Recorre la Ruta"
│   ├── paradas ordenadas
│   ├── tiempo estimado (si disponible)
│   └── CTA: "Compartir ruta"
│
├── SECCIÓN: Son Havana
│   ├── h2: "Son Havana"
│   ├── info del local (verificada)
│   ├── enlace a /son-havana
│   └── nota: "Son Havana es parte del ecosistema SalsaQuest"
│
├── SECCIÓN: Fuentes (V1)
│   ├── h2: "Fuentes y evidencia"
│   ├── tabla de fuentes clasificadas
│   └── enlaces a fuentes primarias
│
├── CTA
│   ├── "Explorar SalsaQuest"
│   ├── "Compartir la ruta"
│   └── "Descubrir eventos"
│
└── FOOTER (heredado de base.html)
```

---

## 13. TIMELINE SPECIFICATION

### Datos autorizados para la timeline

| Orden | Año | Evento | Categoría | Estado | Fuente |
|-------|-----|--------|-----------|--------|--------|
| 1 | 1934 | Discos Fuentes fundada en Cartagena | industria | VERIFIED_PRIMARY | Sitio oficial DF + Wikipedia |
| 2 | 1950 | Codiscos fundada en Medellín | industria | VERIFIED_PRIMARY | Sitio oficial Codiscos |
| 3 | ~1954-1960 | Discos Fuentes se traslada a Medellín | industria | CONTRADICTED | DF dice 1960, Wikipedia 1954 |
| 4 | 1963 | Fruko ingresa a Discos Fuentes | persona | VERIFIED_PRIMARY | AllMusic + Wikipedia |
| 5 | 1968 | Fruko viaja a Nueva York | persona | VERIFIED_SECONDARY | Wikipedia EN |
| 6 | 1970 | Fruko y sus Tesos fundada | orquesta | VERIFIED_PRIMARY | Sitio oficial DF |
| 7 | 1975 | "El Preso" — Wilson Manyoma | grabación | VERIFIED_PRIMARY | Sitio oficial DF + El Tiempo |
| 8 | 1985 | Latina Stereo inicia transmisiones | radio | VERIFIED_PRIMARY | Sitio oficial Latina Stereo |
| 9 | 1989 | Grupo Galé fundado | orquesta | VERIFIED_PRIMARY | Wikipedia + sitio oficial |
| 10 | ~1996 | El Tíbiri abre (fecha aproximada) | lugar | PROBABLE | mbailomedellin (fuente débil) |
| 11 | 2003 | Sonora 8 formada | orquesta | VERIFIED_SECONDARY | Latina Stereo |
| 12 | 2010 | Son Havana abre | lugar | VERIFIED_SECONDARY | Dancefree + Evendo |
| 13 | 2026 | Viva la Salsa — 25 julio | evento | VERIFIED_PRIMARY | Canal Trece |
| 14 | 2026 | Las Leyendas Vivas X edición | evento | VERIFIED_PRIMARY | Comfenalco |

### Reglas de visualización

- **Contradicted (RS-002):** Mostrar como rango "~1954-1960" con nota: "Fecha en disputa: Discos Fuentes indica 1960; otras fuentes indican 1954."
- **Probable (RS-038):** Mostrar como "~1996" con nota: "Fecha aproximada, pendiente de verificación."
- **No inventar eventos** para completar décadas vacías. La década de 1940 no tiene eventos autorizados.
- **Cada evento** lleva badge de evidencia y enlace a fuente.

### UI Timeline

```
Horizontal scroll en mobile (snap points por evento)
Vertical en desktop (tarjetas apiladas)
Filtros por década: [Todas] [1930s] [1950s] [1960s] [1970s] [1980s] [1990s] [2000s] [2010s] [2020s]
Click en evento → expansión inline con descripción + fuente
```

### Décadas sin contenido autorizado

| Década | Estado | Acción |
|--------|--------|--------|
| 1930s | Solo 1934 | Mostrar solo ese evento |
| 1940s | Sin eventos | No mostrar la década en filtros |
| 1950s | 1950 + ~1954-1960 | Mostrar ambos |
| 1960s | 1963 + 1968 | Mostrar ambos |
| 1970s | 1970 + 1975 | Mostrar ambos |
| 1980s | 1985 | Mostrar |
| 1990s | ~1996 | Mostrar con nota |
| 2000s | 2003 | Mostrar |
| 2010s | 2010 | Mostrar |
| 2020s | 2026 | Mostrar |

---

## 14. VENUE SPECIFICATION

### Tarjeta de lugar (Venue Card)

**Estructura:**

```
┌──────────────────────────────────────┐
│ [Badge evidencia]                    │
│                                      │
│ NOMBRE DEL LUGAR                     │
│ Tipo · Barrio                        │
│                                      │
│ Dirección completa                   │
│ Teléfono                             │
│ Horarios                             │
│                                      │
│ [Estilo musical]                     │
│                                      │
│ [CTA: Abrir en Maps]                 │
│ [CTA: WhatsApp / Instagram / Web]    │
│                                      │
│ 📄 Documentado | Última verificación │
│  : 18/09/2026                        │
└──────────────────────────────────────┘
```

### Regla especial: Solo datos operativos

Si un lugar solo tiene evidencia operacional actual (como El Suave), la tarjeta NO presentará:
- "Establecimiento histórico"
- "Fundado en [año]"
- "Fundado por [persona]"
- "Generación [número]"

En su lugar:
- Nombre
- Dirección verificada
- Teléfono verificada
- Horarios verificados
- Estilo musical verificado
- CTA para abrir en Maps

### Separación: históricos vs actuales

| Lugar | Tipo | Justificación |
|-------|------|---------------|
| El Tíbiri | Actual | Sin evidencia de fecha de fundación verificada |
| Son Havana | Actual | Fundado 2010, no es "histórico" en sentido de décadas |
| El Suave | Actual | Sin evidencia histórica verificada |
| Discos Fuentes (sede) | Histórico/actual | Fundada 1934, sede física verificada |
| Calle Palacé | Histórico (atribuido) | Solo como afirmación de Latina Stereo |

---

## 15. MAP SPECIFICATION

### Tipo de mapa

Leaflet con OpenStreetMap tiles (ya integrado en SalsaQuest).

### Marcadores

| Categoría | Color | Icono | Lugares |
|-----------|-------|-------|---------|
| Lugar actual de salsa | Rojo | fa-solid fa-martini-glass Citrus | El Tíbiri, Son Havana, El Suave |
| Lugar histórico (atribuido) | Amarillo | fa-solid fa-landmark | Calle Palacé (si se implementa) |
| Sello discográfico | Azul | fa-solid fa-compact-disc | Discos Fuentes (sede) |
| Evento actual | Verde | fa-solid fa-calendar | Estadio Atanasio Girardot |

### Popup al seleccionar marcador

```
┌──────────────────────────────┐
│ NOMBRE DEL LUGAR             │
│ Dirección                    │
│ [Estilo musical]             │
│                              │
│ [Abrir en Google Maps]       │
│ [Ver ficha completa]         │
│                              │
│ 📄 Documentado               │
└──────────────────────────────┘
```

### Coordenadas verificadas

| Lugar | Lat | Lng | Fuente |
|-------|-----|-----|--------|
| El Tíbiri | ~6.2520 | ~-75.5910 | Dirección verificada (Cra 70 #70-03) |
| Son Havana | ~6.2490 | ~-75.5940 | Dirección verificada (Cra 73 #44-56) |
| El Suave | ~6.2600 | ~-75.5650 | Dirección verificada (Av. 33 #80a-30) |
| Discos Fuentes | ~6.2070 | ~-75.5720 | Dirección conocida (Cra 11A #31A-89) |

**Nota:** Las coordenadas son aproximaciones basadas en direcciones verificadas. Deben geocodificarse exactamente durante implementación usando la API de Nominatim (OpenStreetMap) o Google Geocoding.

### Filtros del mapa

```
[✓] Lugares actuales
[✓] Sellos discográficos
[ ] Lugares históricos (solo si se implementa Calle Palacé)
[✓] Eventos actuales
```

### Comportamiento mobile

- Mapa en tamaño completo con marcadores
- Click en marcador → popup con info
- Botón "Abrir en Google Maps" enlace externo
- Mapa NO bloquea el contenido principal (carga bajo demanda)

---

## 16. ARTISTS & ORCHESTRAS

### Distinción de entidades

| Entidad | Tipo | Ejemplo |
|---------|------|---------|
| Persona | individual | Julio Ernesto Estrada "Fruko" |
| Orquesta | grupo | Fruko y sus Tesos |
| Grabación | obra | "El Preso" |
| Discográfica | empresa | Discos Fuentes |
| Evento | temporal | Viva la Salsa 2026 |
| Lugar | físico | El Tíbiri Tábara |

**Regla:** No mezclar entidades. Fruko (persona) ≠ Fruko y sus Tesos (orquesta). Diego Galé (persona) ≠ Grupo Galé (orquesta).

### Entradas autorizadas

#### Fruko y sus Tesos (orquesta)
- Fundada: 1970 (sitio oficial DF)
- Sello: Discos Fuentes
- Ubicación: Medellín
- Contribución: Pionera de la salsa colombiana (ATTRIBUTED — Discos Fuentes)
- Hitos: "A la memoria del muerto" (1970), "El Preso" (1975)
- Evidencia: VERIFIED_PRIMARY

#### Julio Ernesto Estrada "Fruko" (persona)
- Nacimiento: 7 julio 1951, Medellín
- Ingreso a DF: 1963 (12 años)
- Viaje a NY: 1968
- Apodo: Viene de FRUCO (VERIFIED_SECONDARY)
- Evidencia: VERIFIED_PRIMARY

#### Grupo Galé (orquesta)
- Fundada: 1989, Medellín
- Sello: Codiscos
- Fundador: Diego Galé (percusionista de Grupo Niche, trabajó con Héctor Lavoe)
- Destacado: *Auténtico* (2007) nominado a Latin Grammy
- Evidencia: VERIFIED_PRIMARY

#### Otras orquestas documentadas

| Orquesta | Fundación | Sello | Estado |
|----------|-----------|-------|--------|
| The Latin Brothers | 1970s | Discos Fuentes | VERIFIED_PRIMARY |
| Afrosound | 1973 | Discos Fuentes | VERIFIED_PRIMARY |
| Wganda Kenya | 1976 | Discos Fuentes | VERIFIED_PRIMARY |
| Pachanga Orquesta | ~1990s | — | VERIFIED_SECONDARY |
| Sonora 8 | 2003 | — | VERIFIED_SECONDARY |
| Siguarajazz | 2000 | — | VERIFIED_SECONDARY |
| La Pregonera | 2012 | — | VERIFIED_SECONDARY |
| La Contundente | 2005 | — | VERIFIED_SECONDARY |
| La Malandanza | 2014 | — | VERIFIED_SECONDARY |

---

## 17. RADIO

### Latina Stereo

| Campo | Valor | Estado |
|-------|-------|--------|
| Nombre | Latina Stereo | VERIFIED_PRIMARY |
| Frecuencia | 100.9 FM | VERIFIED_PRIMARY |
| Indicativo | HJQO | VERIFIED_SECONDARY |
| Inicio | ~1985 | ATTRIBUTED (la emisora lo afirma) |
| Lema | "Salsa desde 1985" | VERIFIED_PRIMARY |
| Función | Difusión de salsa clásica y dura | ATTRIBUTED |
| Artistas presentados | Los Hermanos Lebrón, El Gran Combo, Fania All Stars | ATTRIBUTED |
| URL | https://latinastereo.com | VERIFIED_PRIMARY |

### Regla de publicación

- La afirmación "Salsa desde 1985" DEBE llevar atribución: "Latina Stereo afirma..."
- La lista de artistas DEBE llevar atribución: "Según Latina Stereo, la emisora presentó..."
- No extrapolar programación actual basándose en programación histórica

---

## 18. DISCOGRAPHIC INDUSTRY

### Discos Fuentes

| Campo | Valor | Estado |
|-------|-------|--------|
| Fundación | 1934, Cartagena | VERIFIED_PRIMARY |
| Fundador | Antonio Fuentes Estrada | VERIFIED_PRIMARY |
| Traslado a Medellín | Entre 1954 y 1960 | CONTRADICTED |
| Catálogo tropical | 75% | VERIFIED_SECONDARY (Resonancias UC) |
| Descripción | "La Motown colombiana" | ATTRIBUTED (Wikipedia EN) |
| URL | https://discosfuentes.com.co | VERIFIED_PRIMARY |

### Contradicción: Traslado a Medellín

**No seleccionar arbitrariamente una fecha.** Publicar como:
> "Discos Fuentes se estableció en Medellín entre 1954 y 1960. El sitio oficial de la empresa indica 1960, mientras que otras fuentes apuntan a 1954."

### Codiscos

| Campo | Valor | Estado |
|-------|-------|--------|
| Fundación | 1 de julio de 1950, Medellín | VERIFIED_PRIMARY |
| Fundador | Alfredo Díez | VERIFIED_PRIMARY |
| Nombre original | "Zeida" (A. Diez al revés) | VERIFIED_PRIMARY |
| URL | https://www.codiscos.com | VERIFIED_PRIMARY |

---

## 19. CALLE PALACÉ

### Estado de evidencia

La afirmación de que la Calle Palacé fue "epicentro de la vida salsera" proviene ÚNICAMENTE de Latina Stereo (fuente primaria de la emisora sobre su contexto local). No hay evidencia documental de bares específicos.

### Lo que SÍ puede publicarse

- Afirmación atribuida: "Según Latina Stereo, la Calle Palacé fue epicentro de la vida salsera en Medellín"
- Contexto histórico general de la calle (si se documenta con fuente adicional)

### Lo que NO puede publicarse

- Nombres de bares específicos (Aristi, Brisas de Costa Rica, Carruseles, El Conde, El Semáforo, El Diferente, El Ceilán, La Titular)
- Descripciones de la vida nocturna en esos bares
- Fechas de operación de esos bares
- Cualquier dato que no esté respaldado por fuente verificable

### Recomendación para MVP

**Excluir Calle Palacé del MVP.** La sección puede implementarse en V1 o Future cuando se obtenga evidencia adicional (archivo de prensa, entrevistas, registros municipales).

Si se incluye en V1:
- Solo como mención atribuida a Latina Stereo
- Sin nombres de bares
- Con nota: "La información sobre establecimientos específicos de la Calle Palacé está pendiente de verificación documental."

---

## 20. EL TÍBIRI

### Datos que SÍ pueden mostrarse

| Dato | Valor | Fuente | Estado |
|------|-------|--------|--------|
| Nombre | El Tíbiri Tábara | ColombiaBZ + 2POS | VERIFIED_PRIMARY |
| Dirección | Cra 70 #70-03 (Calle 44B), Laureles | Múltiples fuentes | VERIFIED_PRIMARY |
| Teléfono | +57 310 8495461 | ColombiaBZ + 2POS | VERIFIED_PRIMARY |
| Facebook | facebook.com/tibiri.bar | ColombiaBZ | VERIFIED_PRIMARY |
| Tipo | Sótano (underground) | Reseñas múltiples | VERIFIED_PRIMARY |
| Estilo musical | Salsa clásica, son cubano, guaguancó | Reseñas + Real City Tours | VERIFIED_PRIMARY |
| Horarios | Mié-Sáb 21:00-03:00 (sujeto a cambios) | 2POS | VERIFIED_PRIMARY |

### Datos que NO pueden mostrarse como hechos

| Dato | Estado | Acción |
|------|--------|--------|
| Fecha de fundación | PROBABLE (~1996, Wix) | NO mostrar fecha. Mostrar: "Información histórica en proceso de verificación." |
| Fecha de fundación 1992 | DO_NOT_USE | NO mostrar bajo ninguna circunstancia |
| Instagram | PENDING | NO mostrar |
| Propietarios actuales | PENDING | NO mostrar |

### Cómo comunicar incertidumbre sin destruir la UX

En la tarjeta de El Tíbiri:

```
┌──────────────────────────────────────┐
│ 📄 Documentado                       │
│                                      │
│ EL TÍBIRI TÁBARA                     │
│ Sótano · Laureles, Medellín         │
│                                      │
│ Cra 70 #70-03 (Calle 44B)           │
│ +57 310 8495461                      │
│ Mié-Sáb 21:00-03:00                 │
│                                      │
│ Salsa clásica, son cubano,           │
│ guaguancó                            │
│                                      │
│ facebook.com/tibiri.bar              │
│                                      │
│ [CTA: Abrir en Google Maps]          │
│                                      │
│ 📄 Documentado · Verificado: 18/09/26│
└──────────────────────────────────────┘
```

NO incluir:
- "Fundado en 1992" (DO_NOT_USE)
- "Fundado en 1996" (sin corroborar)
- "Uno de los bares más antiguos de Medellín" (sin evidencia)
- Instagram (no encontrado)

---

## 21. EL SUAVE

### Datos que SÍ pueden mostrarse

| Dato | Valor | Fuente | Estado |
|------|-------|--------|--------|
| Nombre | Discoteca El Suave | 2POS | VERIFIED_PRIMARY |
| Dirección | Av. 33 #80a-30, Medellín | 2POS | VERIFIED_PRIMARY |
| Teléfono | +57 310 4593267 | 2POS | VERIFIED_PRIMARY |
| Horarios | Lun-Sáb 16:00-03:00, Dom 16:00-00:00 | 2POS | VERIFIED_PRIMARY |
| Estilo | Salsa & sabor | 2POS | VERIFIED_PRIMARY |
| Valoración | 4.5/5 (597 opiniones) | 2POS | VERIFIED_PRIMARY |

### Datos que NO pueden mostrarse

| Dato | Estado | Acción |
|------|--------|--------|
| Desde 1962 | DO_NOT_USE | NO mostrar |
| Fundado por Bernardo Arango | DO_NOT_USE | NO mostrar |
| Segunda generación | DO_NOT_USE | NO mostrar |
| Tercera generación | DO_NOT_USE | NO mostrar |
| Instagram @discotecaelsuave | PENDING | NO mostrar |

### Cómo presentar El Suave

Como **lugar actual documentado**, NO como "establecimiento histórico":

```
┌──────────────────────────────────────┐
│ 📄 Documentado                       │
│                                      │
│ DISCOTECA EL SUAVE                   │
│ Discoteca · Medellín                 │
│                                      │
│ Av. 33 #80a-30                       │
│ +57 310 4593267                      │
│ Lun-Sáb 16:00-03:00, Dom 16:00-00:00│
│                                      │
│ Salsa & sabor                        │
│                                      │
│ [CTA: Abrir en Google Maps]          │
│                                      │
│ 📄 Documentado · Verificado: 18/09/26│
└──────────────────────────────────────┘
```

---

## 22. SON HAVANA

### Regla de identidad

Mantener completamente separadas estas entidades:

| Entidad | Tipo | Relación |
|---------|------|----------|
| Son Havana | Bar/Restaurante | Local de salsa en Laureles |
| Julio Restrepo Molina | Persona | Identificado con Son Havana en Instagram (PROBABLE) |
| Inversiones Son Havana S.A.S. | Empresa | Razón social (si existe documentación) |
| Son Havana All Stars | Orquesta/Banda | Grupo propio del bar (VERIFIED_PRIMARY) |
| Latina Stereo | Emisora | Entidad completamente separada |

**No fusionar. No atribuir automáticamente hechos de una entidad a otra.**

### Datos de Son Havana (bar) que SÍ pueden mostrarse

| Dato | Valor | Fuente | Estado |
|------|-------|--------|--------|
| Nombre | Son Havana | Múltiples | VERISHED_PRIMARY |
| Fundación | 2010 | Dancefree + Evendo | VERIFIED_SECONDARY |
| Dirección | Cra 73 #44-56, Florida Nueva, Laureles | Múltiples | VERIFIED_PRIMARY |
| Teléfono | +57 311 339-7175 | Casacol | VERIFIED_SECONDARY |
| WhatsApp | 3105156550 | Dancefree | VERIFIED_PRIMARY |
| Instagram | @sonhavana (52K+) | Instagram | VERIFIED_PRIMARY |
| Grupo propio | Son Havana All Stars | Dancefree + Instagram | VERIFIED_PRIMARY |
| Rueda de Casino | Los miércoles | Dancefree | VERIFIED_PRIMARY |
| Horarios | Mié-Jue hasta medianoche, Vie-Sáb hasta 4am | Dancefree + Evendo | VERIFIED_PRIMARY |

### Datos que NO pueden mostrarse como hechos

| Dato | Estado | Acción |
|------|--------|--------|
| Fundador: Julio Restrepo Molina | PROBABLE | Mostrar solo si se atribuye: "Julio Restrepo, identificado con Son Havana" |
| Segundo local en El Poblado | PROBABLE | NO mostrar sin verificación cruzada |
| "El bar de salsa más popular de Medellín" | Sin evidencia | NO mostrar valoraciones no documentadas |

### Cómo integrar Son Havana en la Ruta

Son Havana aparece como **parada documentada** en la Ruta, con la misma tarjeta que cualquier otro lugar. No tiene tratamiento preferencial.

En la sección de Son Havana dentro de la Ruta:
- Información del local (verificada)
- Enlace a `/son-havana` (página completa de SalsaQuest)
- Nota: "Son Havana es parte del ecosistema SalsaQuest"

**NO:**
-Convertir la sección de Son Havana en publicidad
- Dar Treatment editorial preferente
- Mezclar la historia de la Ruta con promociones de Son Havana

---

## 23. ROUTE EXPERIENCE

### "Recorre la Ruta"

**Punto de entrada:** Botón "Explorar la Ruta" en el Hero o al final de la sección de Lugares.

**Paradas recomendadas (orden):**

| # | Parada | Categoría | Tiempo est. | CTA |
|---|--------|-----------|-------------|-----|
| 1 | El Tíbiri Tábara | Lugar actual | ~60 min | Abrir en Maps |
| 2 | Son Havana | Lugar actual | ~90 min | Abrir en Maps |
| 3 | El Suave | Lugar actual | ~60 min | Abrir en Maps |

**Criterios de orden:**
1. Proximidad geográfica (El Tíbiri y Son Havana están a ~600m)
2. Horarios de apertura
3. Experiencia del usuario (empezar por sótano, terminar por local más grande)

**Tiempo total estimado:** NO calculado (pendiente de validación terreno). Marcar como "Pendiente de cálculo".

**Transporte:** A pie (distancias cortas en Laureles/Florida Nueva).

**Enlace externo:** Google Maps con directions mode.

**CTA final:** "Compartir la Ruta" (deep link o WhatsApp).

### Estado de cada parada

Todas las paradas son **lugares actuales documentados**. Ninguno es "histórico" en el sentido de haber sido documentado por décadas de existencia.

---

## 24. INTERNATIONALIZATION

### Estrategia

| Campo | Español (ES) | Inglés (EN) | Francés (FR) |
|-------|-------------|-------------|--------------|
| Contenido fuente | SÍ | Traducido | Traducido |
| Nombres propios | Sin cambio | Sin cambio | Sin cambio |
| Nombres históricos | Sin cambio | Sin cambio | Sin cambio |
| Atribuciones | Sin cambio | Sin cambio | Sin cambio |
| Fuentes | Sin cambio | Sin cambio | Sin cambio |
| URLs | Sin cambio | Sin cambio | Sin cambio |
| Fallback | — | ES | ES |

### Reglas

1. **No traducir nombres propios:** "Discos Fuentes" no es "Fuentes Records". "El Tíbiri Tábara" no es "The Tíbiri Tábara".
2. **No alterar nombres históricos:** "El Preso" no es "The Prisoner" en contenido histórico.
3. **No perder atribución al traducir:** La atribución viaja en el mismo idioma que la fuente original.
4. **SEO internacional:** hreflang tags para ES/EN/FR.
5. **Fallback:** Si FR no está disponible, mostrar EN. Si EN no está disponible, mostrar ES.

### URLs

```
/ruta-salsera          → ES (default)
/ruta-salsera?lang=en  → EN
/ruta-salsera?lang=fr  → FR
```

o alternativamente:

```
/ruta-salsera          → ES
/en/route-sera         → EN (futuro)
/fr/la-route-salsa     → FR (futuro)
```

Para MVP: query parameter `?lang=` es suficiente.

---

## 25. SEO

### SEO técnico

| Elemento | ES | EN | FR |
|----------|----|----|-----|
| title | "La Ruta Salsera de Medellín \| SalsaQuest" | "The Salsa Route of Medellín \| SalsaQuest" | "La Route Salsa de Medellín \| SalsaQuest" |
| meta description | "Descubre la historia de la salsa en Medellín: lugares, artistas, industria discográfica y ruta turística documentada." | "Discover the history of salsa in Medellín: venues, artists, record labels, and a documented tourist route." | "Découvrez l'histoire de la salsa à Medellín : lieux, artistes, labels et itinéraire touristique documenté." |
| canonical | /ruta-salsera | /ruta-salsera | /ruta-salsera |
| hreflang | hreflang="es" | hreflang="en" | hreflang="fr" |
| og:title | "La Ruta Salsera de Medellín" | "The Salsa Route of Medellín" | "La Route Salsa de Medellín" |
| og:description | (igual a meta description) | (igual a meta description) | (igual a meta description) |
| og:image | Imagen representativa de Medellín | Misma | Misma |
| twitter:card | summary_large_image | Misma | Misma |

### Structured data

```json
{
    "@context": "https://schema.org",
    "@type": "TouristTrip",
    "name": "La Ruta Salsera de Medellín",
    "description": "Historia, lugares y cultura salsera de Medellín documentados",
    "touristType": "Cultural tourism",
    "itinerary": {
        "@type": "ItemList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "item": {
                    "@type": "NightClub",
                    "name": "El Tíbiri Tábara",
                    "address": "Cra 70 #70-03, Laureles, Medellín"
                }
            },
            {
                "@type": "ListItem",
                "position": 2,
                "item": {
                    "@type": "NightClub",
                    "name": "Son Havana",
                    "address": "Cra 73 #44-56, Florida Nueva, Medellín"
                }
            },
            {
                "@type": "ListItem",
                "position": 3,
                "item": {
                    "@type": "NightClub",
                    "name": "Discoteca El Suave",
                    "address": "Av. 33 #80a-30, Medellín"
                }
            }
        ]
    }
}
```

### SEO semántico — Clusters

| Cluster | Páginas | Prioridad |
|---------|---------|-----------|
| salsa Medellín | /ruta-salsera | Alta |
| historia de la salsa en Medellín | /ruta-salsera (sección timeline) | Alta |
| ruta salsera Medellín | /ruta-salsera | Alta |
| lugares de salsa Medellín | /ruta-salsera (sección lugares + mapa) | Alta |
| salsa Colombia | /ruta-salsera (sección industria) | Media |
| turismo salsa Medellín | /ruta-salsera | Media |
| bares de salsa Medellín | /ruta-salsera (lugares actuales) | Media |
| Discos Fuentes Medellín | /ruta-salsera (sección industria) | Media |
| Fruko y sus Tesos | /ruta-salsera (sección artistas) | Baja |
| Latina Stereo Medellín | /ruta-salsera (sección radio) | Baja |

### Robots y sitemap

- /ruta-salsera: indexable, follow
- No bloquear en robots.txt
- Incluir en sitemap.xml

---

## 26. ACCESSIBILITY

### WCAG 2.2 AA como objetivo

| Requisito | Implementación |
|-----------|----------------|
| Contraste | Texto sobre video: mínimo 4.5:1 (overlay suficientemente oscuro) |
| Keyboard navigation | Todos los interactivos navegables con Tab |
| Focus states | Focus visible en todos los elementos interactivos |
| Semantic HTML | headings jerárquicos (h1 → h2 → h3), landmarks, lists |
| ARIA | Solo cuando corresponda (mapa, timeline, popups) |
| Reduced motion | Respetar prefers-reduced-motion: ocultar animaciones |
| Alt text | Todas las imágenes con alt descriptivo |
| Mapas | Alternativa textual del contenido del mapa |
| Video | Noautoplay, controls disponibles, poster como fallback |
| Textos sobre video | Garantizar legibilidad con overlay |
| No depender del color | Los badges de evidencia tienen texto + icono, no solo color |

### Timeline accesible

- Navegable con teclado (flechas izquierda/derecha)
- ARIA labels en cada evento
- Expansión de detalle con Enter/Space
- Skip link para saltar la timeline

### Mapa accesible

- Alternativa textual: lista de lugares con direcciones
- Marcadores con ARIA labels
- Popup accesible con teclado

---

## 27. PERFORMANCE

### Lazy loading

| Recurso | Strategy |
|---------|----------|
| Imágenes de lugares | loading="lazy" |
| Mapa Leaflet | Carga bajo demanda (solo cuando el usuario llega a la sección) |
| Video de fondo | Ya existente (hero de SalsaQuest) |
| Fuentes | preload solo para Poppins (fuente principal) |

### Core Web Vitals

| Métrica | Target | Strategy |
|---------|--------|----------|
| LCP | <2.5s | Lazy load de imágenes, preload del hero |
| FID | <100ms | JavaScript mínimo, event handlers ligeros |
| CLS | <0.1 | Dimensiones explícitas en imágenes, mapa con height fijo |

### Recursos

- **Imágenes:** WebP/AVIF si la arquitectura lo permite, fallback a JPEG
- **JS:** Sin frameworks pesados. Vanilla JS + Bootstrap 5 (ya cargado)
- **CSS:** Ya existente (style.css + fase1-diseno.css)
- **Fonts:** Google Fonts (ya cargado, solo Poppins necesario)
- **Mapa:** Leaflet (ya cargado en todas las páginas)

### Caching

- Assets estáticos: cache-control max-age=31536000 (1 año)
- HTML: no-cache (siempre fresco)
- API responses: cache-control max-age=3600 (1 hora)

---

## 28. RESPONSIVE DESIGN

### Breakpoints

| Device | Width | Comportamiento |
|--------|-------|----------------|
| Mobile | <576px | Stack vertical, timeline horizontal scroll |
| Tablet | 576-991px | 2 columnas, timeline mixto |
| Desktop | 992-1199px | 3 columnas, timeline vertical |
| Large | ≥1200px | Contenido centrado, max-width |

### Comportamiento por componente

| Componente | Mobile | Desktop |
|------------|--------|---------|
| Hero | Full width, texto centrado | Full width, texto centrado |
| Timeline | Scroll horizontal (snap) | Vertical (tarjetas) |
| Venue cards | 1 columna | 2-3 columnas |
| Mapa | Full width, height 300px | 2/3 width, height 420px |
| Artistas | 1-2 columnas | 3-4 columnas |
| Ruta | Lista vertical | Lista con mapa lateral |
| Footer | Stack vertical | Horizontal |

### Touch

- Swipe en timeline horizontal
- Tap en marcadores del mapa
- Botones grandes para CTAs (mínimo 44x44px)

---

## 29. CONVERSION ARCHITECTURE

### CTAs respetuosos (no invasivos)

| CTA | Ubicación | Tipo | Acción |
|-----|-----------|------|--------|
| "Explorar la ruta" | Hero | Primario | Scroll a timeline |
| "Abrir en Maps" | Venue cards | Secundario | Enlace externo a Google Maps |
| "Reserva por WhatsApp" | Venue cards (si aplica) | Secundario | Enlace externo |
| "Compartir la ruta" | Final de ruta | Primario | Share API o WhatsApp |
| "Explorar SalsaQuest" | Final de página | Primario | Navegación interna |
| "Descubrir eventos" | Sección de eventos | Secundario | Navegación interna |
| "Ver opiniones en TripAdvisor" | Venue cards | Terciario | Enlace externo |

### Regla

Los CTAs no convierten la página en una landing comercial. Cada CTA debe aportar valor al usuario:
- "Abrir en Maps" → el usuario puede ir al lugar
- "Compartir la ruta" → el usuario puede compartir con amigos
- "Explorar SalsaQuest" → el usuario descubre más contenido

---

## 30. ANALYTICS SPECIFICATION

### Eventos conceptuales (no implementar todavía)

| Evento | Trigger | Datos |
|--------|---------|-------|
| route_view | Página cargada | lang, referrer |
| timeline_interaction | Click en evento de timeline | event_id, decade |
| venue_open | Click en venue card | venue_id |
| source_open | Click en enlace de fuente | source_id, url |
| map_interaction | Click en marcador del mapa | venue_id, lat, lng |
| route_start | Click en "Recorre la Ruta" | — |
| external_link_click | Click en enlace externo | url, venue_id |
| son_havana_click | Click en enlace de Son Havana | target |
| language_change | Cambio de idioma | from_lang, to_lang |
| cta_click | Click en CTA | cta_id, target |

---

## 31. TRUST UX

### Sistema visual de confianza

| Badge | Icono | Color | Texto |
|-------|-------|-------|-------|
| Documentado | 📄 | Verde (#28a745) | "Documentado" |
| Fuente secundaria | 📰 | Azul (#007bff) | "Según fuente verificada" |
| Atribuido | 🏷️ | Amarillo (#ffc107) | "Atribuido a [fuente]" |
| En verificación | ⏳ | Gris (#6c757d) | "En proceso de verificación" |
| En disputa | ⏚ | Naranja (#fd7e14) | "Información en revisión" |

### Reglas de visualización

- Badge siempre acompañado de texto (nunca solo icono)
- Click en badge → tooltip con explicación + enlace a fuente
- No medir "verdad" con porcentajes o scores
- La evidencia se explica, no se gamifica

---

## 32. MISSING DATA UX

### Mensajes estándar para datos faltantes

| Situación | Mensaje |
|-----------|---------|
| Fecha no verificada | "La fecha exacta no está suficientemente documentada." |
| Información pendiente | "Información histórica en proceso de verificación." |
| Atribución no confirmada | "Esta afirmación se conserva como referencia atribuida y no como hecho confirmado." |
| Fuente no encontrada | "No se encontraron fuentes documentales para esta afirmación." |
| Dato contradictorio | "Existen versiones encontradas sobre este dato. Ver fuentes." |

### Reglas

- **Nunca:** "Según la IA..."
- **Nunca:** Texto inventado para rellenar vacíos
- **Nunca:** Placeholder que parezca dato real
- **Siempre:** Marcar explícitamente lo que no se sabe
- **Siempre:** Preferir ausencia de dato a invención

---

## 33. CONTENT INVENTORY COMPLETO

### Resumen ejecutivo

| Categoría | Total | Authorized | Attributed | Pending | Prohibited |
|-----------|-------|------------|------------|---------|------------|
| Hechos históricos | 14 | 10 | 2 | 1 | 1 |
| Lugares | 3 | 3 | 0 | 0 | 0 |
| Artistas/Orquestas | 11 | 11 | 0 | 0 | 0 |
| Radio | 1 | 1 | 0 | 0 | 0 |
| Eventos | 2 | 2 | 0 | 0 | 0 |
| Fuentes académicas | 2 | 2 | 0 | 0 | 0 |
| **Total** | **33** | **29** | **2** | **1** | **1** |

### Detalle por módulo

#### Timeline (14 eventos)
- 10 VERIFIED_PRIMARY
- 2 ATTRIBUTED
- 1 PROBABLE (~1996)
- 1 CONTRADICTED (traslado DF)

#### Lugares (3 lugares)
- 3 VERIFIED_PRIMARY (datos operativos)
- 0 con evidencia histórica documentada

#### Artistas/Orquestas (11 entradas)
- 11 con evidencia VERIFIED o VERIFIED_SECONDARY

#### Radio (1 emisora)
- 1 VERIFIED_PRIMARY + ATTRIBUTED

#### Eventos (2 eventos)
- 2 VERIFIED_PRIMARY

#### Fuentes académicas (2 obras)
- 2 VERIFIED_PRIMARY

---

## 34. MVP VS FUTURE

### MVP (Mínimo Viable Product)

| Funcionalidad | Justificación |
|---------------|---------------|
| Hero con título y CTA | Entrada esencial |
| Introducción (¿Por qué Medellín?) | Contexto mínimo necesario |
| Timeline con 14 eventos | Core del producto |
| Industria discográfica (DF + Codiscos) | Solo 2 entidades documentadas |
| Radio (Latina Stereo) | Solo 1 emisora documentada |
| Artistas y orquestas (11 entradas) | Datos verificados disponibles |
| Lugares actuales (3 lugares) | Datos operativos verificados |
| Mapa con marcadores | Coordenadas disponibles |
| Son Havana (sección integrada) | Conexión con ecosistema |
| CTA (Explorar SalsaQuest, Compartir) | Conversión mínima |
| Badge de evidencia | Diferenciador del producto |
| Responsive design | Requisito básico |
| SEO básico (title, meta, structured data) | Visibilidad en buscadores |

### V1 (Post-MVP)

| Funcionalidad | Justificación |
|---------------|---------------|
| Ruta recomendada con paradas | Requiere cálculo de distancias |
| Fuentes y evidencia (tabla completa) | Enrichment post-MVP |
| i18n (EN/FR) | Requiere estrategia de traducción |
| Eventos próximos (integración) | Requiere fuente de datos actualizada |
| Share / social | Funcionalidad de engagement |
| Calle Palacé (mención atribuida) | Requiere Decisión editorial |

### Future

| Funcionalidad | Justificación |
|---------------|---------------|
| Audio/guía sonora | Requiere producción de audio |
| Realidad aumentada | Requiere desarrollo especializado |
| Gamificación (badges de visitas) | Requiere backend de usuarios |
| Calle Palacé con bares específicos | Requiere investigación adicional |
| "Renacimiento de la salsa brava" | Requiere definición documental |
| App nativa | Requiere desarrollo mobile separado |
| Colaboración con restaurants/bares | Requiere acuerdos comerciales |

---

## 35. IMPLEMENTATION CONTRACT

### Arquitectura

- **Ruta Flask:** `/ruta-salsera` → `render_template('ruta_salsera.html')`
- **Blueprint:** Agregar a `main.py` o crear `routes/ruta_salsera.py`
- **Template:** `templates/ruta_salsera.html` (extiende `base.html`)
- **Datos:** JSON en `models/ruta_salsera_data.py` (mismaoda que `content_data.py`)
- **API:** `/api/ruta-salsera` → sirve el JSON de la ruta
- **JS:** Nuevo archivo `static/js/ruta-salsera.js` para interacciones específicas
- **CSS:** Agregar estilos específicos a `style.css` o nuevo `ruta-salsera.css`

### Datos

- Todos los datos en Python (no en BD) — misma convención que `content_data.py`
- Cada entrada incluye `evidence_status` y `sources`
- No hay migraciones ni seeds
- Los datos se cargan vía API JSON

### Evidencia

- Cada claim en el HTML lleva `data-evidence="VERIFIED_PRIMARY"` (o el estado correspondiente)
- Los badges de evidencia se renderizan con JS basándose en `data-evidence`
- Las fuentes se almacenan en `data-source-id` y se muestran en tooltip

### Seguridad

- No se exponen API keys
- No se modifica la base de datos
- No se insertan datos del usuario en la Ruta
- Los enlaces externos usan `rel="noopener noreferrer"`

### Performance

- Lazy load de imágenes
- Mapa carga bajo demanda
- JS específico de la Ruta carga solo en `/ruta-salsera`
- CSS específico carga solo en `/ruta-salsera`

### SEO

- Structured data en el template
- hreflang para ES/EN/FR
- Open Graph y Twitter Cards
- Canonical URL

### Accessibility

- WCAG 2.2 AA
- Keyboard navigation
- ARIA labels en timeline y mapa
- Alt text en imágenes
- Reduced motion

### Responsive

- Mobile-first
- Breakpoints: 576, 768, 992, 1200
- Timeline: horizontal scroll en mobile, vertical en desktop

### Analytics

- Eventos listados en sección 30
- No implementar todavía

### Entity separation

- Son Havana ≠ Julio Restrepo ≠ Inversiones Son Havana S.A.S. ≠ Son Havana All Stars ≠ Latina Stereo
- Cada entidad tiene sus propios datos y evidencia
- No se fusionan en ningún punto del código

---

## 36. ACCEPTANCE CRITERIA

### Evidence

- [ ] Ningún claim publicado carece de `evidence_status`
- [ ] Ningún claim DO_NOT_USE aparece en la experiencia
- [ ] Los claims pendientes NO se presentan como hechos
- [ ] Los claims contradictorios muestran ambas versiones con fuentes
- [ ] Los claims ATTRIBUTED llevan atribución explícita
- [ ] Cada claim tiene al menos una fuente asociada

### Entity integrity

- [ ] Son Havana NO se fusiona con Julio Restrepo Molina
- [ ] Son Havana All Stars permanece separado
- [ ] Latina Stereo permanece separada
- [ ] Fruko (persona) ≠ Fruko y sus Tesos (orquesta)
- [ ] Diego Galé (persona) ≠ Grupo Galé (orquesta)

### UX

- [ ] La experiencia funciona en mobile (<576px)
- [ ] La timeline es navegable con teclado
- [ ] El mapa no bloquea el contenido principal
- [ ] Las fuentes son accesibles (click en badge → tooltip con fuente)
- [ ] Los CTAs funcionan (enlaces externos abren en nueva pestaña)
- [ ] El video de fondo no bloquea el contenido

### SEO

- [ ] Metadata definida para ES/EN/FR
- [ ] Canonical definido
- [ ] Structured data válido
- [ ] hreflang definido
- [ ] Open Graph completo
- [ ] Robots.txt permite indexación
- [ ] Incluido en sitemap.xml

### Performance

- [ ] Video no bloquea el contenido principal
- [ ] Mapa puede cargarse de forma diferida
- [ ] Lazy loading en imágenes
- [ ] LCP <2.5s
- [ ] CLS <0.1

### Content

- [ ] 14 eventos en timeline (todos con evidencia)
- [ ] 3 lugares actuales (todos con datos operativos verificados)
- [ ] 11 artistas/orquestas (todos con evidencia)
- [ ] 1 emisora de radio (con evidencia)
- [ ] 2 eventos actuales (con evidencia)
- [ ] 2 fuentes académicas (con evidencia)
- [ ] Ningún dato DO_NOT_USE visible

---

## 37. DEFINITION OF DONE — FASE 3

- [x] `ROUTE-SALSERA-EVIDENCE-AUDIT.md` fue leído completamente
- [x] La especificación se basa exclusivamente en evidencia autorizada
- [x] Existe Content Contract (sección 8)
- [x] Existe Content Inventory (sección 33)
- [x] Existe Page Blueprint (sección 12)
- [x] Existe definición de objetos de contenido (sección 11)
- [x] Existe arquitectura de información (sección 7)
- [x] Existe estrategia ES/EN/FR (sección 24)
- [x] Existe estrategia SEO (sección 25)
- [x] Existan requisitos de accessibility (sección 26)
- [x] Existan requisitos de performance (sección 27)
- [x] Existe arquitectura de conversión (sección 29)
- [x] Existe separación explícita de entidades (secciones 20, 21, 22)
- [x] Existan reglas para datos desconocidos (sección 32)
- [x] Existe MVP/V1/Future (sección 34)
- [x] Existan acceptance criteria (sección 36)
- [x] Existe Definition of Done (esta sección)
- [x] No se modificó código
- [x] No se modificó la base de datos
- [x] No se ejecutó ninguna operación destructiva
- [x] No se realizó ninguna operación Git
- [x] No se inventaron datos

---

## 38. OPEN QUESTIONS

| # | Pregunta | Bloquea | Prioridad |
|---|----------|---------|-----------|
| OQ1 | ¿Coordenadas exactas de El Tíbiri, Son Havana, El Suave? | Implementación del mapa | Alta |
| OQ2 | ¿Usar query parameter (?lang=) o rutas separadas (/en/) para i18n? | Implementación i18n | Media |
| OQ3 | ¿Crear nuevo blueprint o agregar a main.py? | Arquitectura del código | Alta |
| OQ4 | ¿CSS separado (ruta-salsera.css) o agregar a style.css? | Organización del código | Media |
| OQ5 | ¿La Ruta sale del navbar principal o es accesible solo desde /medellin? | Navegación | Alta |
| OQ6 | ¿Incluir sección de fuentes en MVP o solo en V1? | Contenido del MVP | Media |
| OQ7 | ¿Cómo manejar la ruta /ruta-salsera vs la existente /medellin? | Arquitectura | Alta |

---

## 39. PENDING EVIDENCE

| # | Item | Estado actual | Acción necesaria |
|---|------|---------------|------------------|
| PE1 | El Tíbiri — fecha de fundación | PROBABLE (~1996, Wix) | Investigación adicional (registro mercantil, entrevista) |
| PE2 | El Suave — historia completa | Sin evidencia | Archivo de prensa, entrevista directa |
| PE3 | Calle Palacé — bares históricos | Sin evidencia | Archivo de prensa |
| PE4 | Son Havana — fundador confirmado | PROBABLE (Instagram) | Verificación institucional |
| PE5 | Son Havana — segundo local | PROBABLE (2 fuentes) | Verificación cruzada |
| PE6 | Héctor Lavoe — conciertos públicos en Medellín | Solo anécdota 1981 | Archivo de prensa |
| PE7 | Investigadores musicales de Medellín | Sin resultados | Catálogos universitarios |

---

## 40. PROHIBITED CONTENT

Los siguientes contenidos están **PROHIBIDOS** en La Ruta Salsera de Medellín:

1. ❌ "El Tíbiri fue fundado en 1992"
2. ❌ "El Suave existe desde 1962"
3. ❌ "El Suave fue fundado por Bernardo Arango"
4. ❌ "Bernardo 'Malagente' Arango, segunda generación"
5. ❌ "Nancy Díaz, Catalina Arango, tercera generación"
6. ❌ "Renacimiento de la salsa brava" como categoría factual
7. ❌ Bares específicos de Calle Palacé (Aristi, Brisas de Costa Rica, Carruseles, El Conde, El Semáforo, El Diferente, El Ceilán, La Titular)
8. ❌ "El Preso ha sido bailada en más de 70 países"
9. ❌ Instagram @discotecaelsuave
10. ❌ El Tíbiri tiene Instagram
11. ❌ Hernán Darío Usquiano como investigador verificado
12. ❌ Fecha exacta de fundación de El Tíbiri
13. ❌ "Capital salsera" como hecho factual
14. ❌ "Epicentro" como hecho factual (sin atribución)

---

## 41. FINAL PRODUCT DECISION MATRIX

| Decisión | Opción A | Opción B | Decisión | Razón |
|----------|----------|----------|----------|-------|
| Ruta nueva vs modificar /medellin | Nueva ruta /ruta-salsera | Modificar /medellin | **A** | Preservar sección existente, producto independiente |
| Datos en Python vs BD | Python dict (content_data) | SQLAlchemy | **Python dict** | Convención existente, sin migraciones |
| CSS separado vs integrado | Nuevo archivo | Agregar a style.css | **Decidir en implementación** | Depende del volumen de estilos |
| Blueprint nuevo vs main.py | Nuevo archivo | En main.py | **A** | Modularidad, separación de responsabilidades |
| i18n por query param vs rutas | ?lang=en | /en/route | **Query param** | MVP simpler, migrar a rutas en V1 |
| Fuentes en MVP vs V1 | Incluir | Excluir | **Excluir** | MVP se centra en contenido, fuentes en V1 |
| Calle Palacé en MVP | Incluir | Excluir | **Excluir** | Sin evidencia de bares específicos |
| "Renacimiento salsa brava" en MVP | Incluir | Excluir | **Excluir** | Expresión no documentada |
| Mapa Leaflet vs Google Maps | Leaflet (ya cargado) | Google Maps API | **Leaflet** | Sin costo adicional, ya integrado |
| Structured data en MVP | Incluir | Excluir | **Incluir** | SEO básico es esencial |

---

## 42. RESUMEN EJECUTIVO A ENTREGAR

### A. Documento creado/modificado

`ROUTE-SALSERA-PRODUCT-SPEC.md` — Ruta: `D:\Proyectos\sonhavanagame\ROUTE-SALSERA-PRODUCT-SPEC.md`

### B. Arquitectura propuesta

| Módulo | Ubicación | Descripción |
|--------|-----------|-------------|
| Template | `templates/ruta_salsera.html` | Página principal de la Ruta |
| Route | `routes/main.py` o `routes/ruta_salsera.py` | Ruta Flask `/ruta-salsera` |
| Data | `models/ruta_salsera_data.py` | Datos estáticos con evidencia |
| API | `/api/ruta-salsera` | Endpoint JSON |
| JS | `static/js/ruta_salsera.js` | Interacciones específicas |
| CSS | `static/css/ruta_salsera.css` o en `style.css` | Estilos específicos |

### C. MVP concreto

1. Hero con título y CTA
2. Introducción (¿Por qué Medellín?)
3. Timeline con 14 eventos documentados
4. Industria discográfica (Discos Fuentes + Codiscos)
5. Radio (Latina Stereo)
6. Artistas y orquestas (11 entradas)
7. Lugares actuales (3 lugares con datos operativos)
8. Mapa con marcadores
9. Son Havana (sección integrada)
10. CTA (Explorar SalsaQuest, Compartir)
11. Badge de evidencia en cada claim
12. Responsive design
13. SEO básico

### D. Future concreto

1. Ruta recomendada con paradas
2. Fuentes y evidencia (tabla completa)
3. i18n (EN/FR)
4. Eventos próximos
5. Share / social
6. Calle Palacé (mención atribuida)
7. Audio/guía sonora
8. Realidad aumentada
9. Gamificación

### E. Evidence

| Categoría | Autorizados | Pendientes | Prohibidos |
|-----------|-------------|------------|------------|
| Contenido publicable | 29 items | 7 items | 14 items |

### F. Riesgos

| Riesgo | Impacto | Probabilidad | Mitigación |
|--------|---------|--------------|------------|
| Fechas contradictorias (DF traslado) | Medio | Alta | Usar rango, no fecha exacta |
| El Tíbiri sin fecha verificable | Bajo | Alta | No mostrar fecha, solo datos operativos |
| El Suave sin historia documentada | Bajo | Alta | Mostrar solo datos actuales |
| i18n incompleto | Medio | Media | Lanzar solo ES en MVP |
| Coordenadas imprecisas | Medio | Media | Geocodificar durante implementación |
| Confusión entre /medellin y /ruta-salsera | Medio | Baja | Documentar claramente la diferencia |

### G. Decisiones importantes

1. La Ruta es un producto nuevo, no una modificación de /medellin
2. Los datos están en Python dicts, no en la BD
3. MVP solo en español
4. Calle Palacé excluida del MVP
5. "Renacimiento de la salsa brava" excluido del MVP
6. Son Havana con tratamiento editorial igualitario
7. Cada claim lleva badge de evidencia
8. Fuentes excluidas del MVP (solo en V1)
9. Structured data incluido en MVP
10. Leaflet para el mapa (ya cargado)

### H. Preguntas abiertas

7 preguntas listadas en sección 38. Las más bloqueantes:
- OQ3: Blueprint nuevo vs main.py
- OQ7: Relación /ruta-salsera vs /medellin
- OQ1: Coordenadas exactas

### I. Estado de implementación

**NO IMPLEMENTADO — FASE 3 SOLAMENTE**

Este documento es una especificación de producto. No contiene código, no modifica archivos existentes, no ejecuta comandos, no realiza operaciones Git. Está diseñado para ser consumido por la Fase 4 (Implementation Plan).

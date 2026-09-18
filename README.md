# 🎵 SalsaQuest

### Medellín se escucha. Medellín se baila.

**SalsaQuest** es una experiencia web interactiva dedicada a explorar la cultura salsera de Medellín a través de **lugares, historia, artistas, música, eventos, mapas, retos y experiencias digitales**.

El proyecto combina desarrollo web, cartografía interactiva, narrativa cultural, gamificación y diseño de experiencias para convertir información dispersa sobre la escena salsera en una experiencia digital navegable.

> **Producto principal:** Ruta Salsera
> **Tecnología:** Flask · SQLAlchemy · SQLite · Jinja · JavaScript · Leaflet
> **Estado:** En producción

---

## 🚀 Demo

### 🌎 Explorar SalsaQuest

**[Abrir SalsaQuest](https://salsaquest-1.onrender.com/)**

La entrada principal de la aplicación conduce directamente a:

**Ruta Salsera — Medellín**

Una experiencia interactiva para explorar la ciudad desde su historia y cultura salsera.

---

# 🗺️ Ruta Salsera

## Medellín se escucha. Medellín se baila.

**Ruta Salsera** es la experiencia central de SalsaQuest.

La aplicación utiliza una combinación de **mapa real, coordenadas geográficas, contenido cultural y navegación interactiva** para explorar distintos elementos de la escena salsera de Medellín.

Incluye:

* 🗺️ mapa interactivo
* 📍 lugares y venues
* 🎺 artistas y orquestas
* 📻 radio
* 💿 sellos discográficos
* 📜 línea histórica
* 📅 eventos
* 🎯 experiencias y retos
* 🔎 fuentes y trazabilidad de información

La ruta está diseñada para funcionar como una capa digital de exploración cultural, turística y musical.

---

# 🎯 Qué busca resolver

La cultura salsera de una ciudad no está únicamente en sus discotecas.

También existe en:

* sus barrios;
* sus emisoras;
* sus coleccionistas;
* sus artistas;
* sus academias;
* sus eventos;
* sus lugares históricos;
* sus sellos;
* sus historias;
* sus visitantes;
* y las comunidades que mantienen viva la música.

SalsaQuest busca convertir esos elementos en una **experiencia digital conectada y explorable**.

---

# 🧭 Experiencias

## Ruta Salsera

Exploración geográfica y cultural de Medellín.

## Medellín

Contenido relacionado con lugares y experiencias salseras de la ciudad.

## Son Havana

Experiencia dedicada al universo de Son Havana, manteniendo separadas las entidades y contextos relacionados con el establecimiento.

## Desafío

Componente de gamificación para convertir la exploración cultural en una experiencia participativa.

---

# 🧩 Funcionalidades

### 🗺️ Cartografía interactiva

Mapa basado en geografía real y coordenadas verificables.

### 📜 Timeline

Línea temporal para explorar acontecimientos y referencias relacionadas con la historia salsera.

### 📍 Venues

Lugares relevantes para la experiencia salsera.

### 🎺 Artistas y orquestas

Contenido organizado alrededor de artistas y agrupaciones.

### 📻 Radio

Integración de referencias y recursos relacionados con radio y difusión musical.

### 💿 Sellos

Información sobre sellos y ecosistemas musicales.

### 📅 Eventos

Agenda y referencias de eventos cuando existe información disponible.

### 🔎 Evidence Tracking

Los contenidos se estructuran procurando diferenciar entre información verificada, atribuida, pendiente de verificación y otros estados de evidencia.

Esto permite evitar presentar como hechos datos que no cuentan con respaldo suficiente.

---

# 🏗️ Arquitectura

SalsaQuest está construido como una aplicación web modular basada en Flask.

```text
Browser
   │
   ▼
Flask Application
   │
   ├── Routes
   │
   ├── Templates / Jinja
   │
   ├── Content Models
   │
   ├── APIs
   │
   └── Static Assets
          │
          ├── CSS
          ├── JavaScript
          ├── Images
          └── Video
```

La aplicación mantiene una separación entre:

* presentación;
* rutas;
* modelos;
* contenido;
* datos;
* recursos estáticos;
* lógica interactiva.

---

# 🛠️ Stack tecnológico

| Tecnología        | Uso                             |
| ----------------- | ------------------------------- |
| **Python**        | Lenguaje principal              |
| **Flask**         | Framework web                   |
| **SQLAlchemy**    | ORM / persistencia              |
| **SQLite**        | Base de datos local             |
| **Jinja2**        | Renderizado de templates        |
| **JavaScript**    | Interactividad                  |
| **Leaflet**       | Mapas interactivos              |
| **OpenStreetMap** | Datos cartográficos             |
| **HTML5 / CSS3**  | Interfaz                        |
| **MP4**           | Experiencias visuales dinámicas |

---

# 🎨 Diseño de experiencia

SalsaQuest utiliza una identidad visual inspirada en:

* cultura salsera;
* La Habana;
* Medellín;
* neón;
* música;
* nightlife;
* mapas;
* exploración;
* interfaces de videojuegos.

La interfaz utiliza elementos como:

* glassmorphism;
* efectos de iluminación;
* overlays;
* animaciones;
* mapas interactivos;
* video;
* microinteracciones;
* navegación orientada a exploración.

### Principio visual

Cuando técnicamente es apropiado, el proyecto prioriza **experiencias visuales dinámicas** sobre fondos estáticos.

Los recursos audiovisuales se optimizan para equilibrar:

**impacto visual + velocidad + consumo de datos + experiencia móvil.**

---

# ⚡ Performance

Los videos utilizados como fondos visuales cuentan con versiones optimizadas para reducir el peso de descarga.

Se priorizan:

* resolución adecuada al contexto;
* compresión;
* ausencia de audio cuando no es necesario;
* `muted`;
* `playsinline`;
* `preload="metadata"`;
* reproducción en loop;
* fallback mediante poster.

El objetivo es mantener una experiencia visual inmersiva sin convertir los recursos multimedia en un cuello de botella.

---

# 🔐 Integridad de información

SalsaQuest no pretende convertir información no comprobada en hechos.

El proyecto utiliza estados de evidencia para diferenciar distintos niveles de confianza, incluyendo:

```text
VERIFIED_PRIMARY
VERIFIED_SECONDARY
ATTRIBUTED
PROBABLE
PENDING
CONTRADICTED
DO_NOT_USE
```

Esto es especialmente importante para información histórica, biográfica y cultural.

La regla de producto es simple:

> **Cuando un dato no puede respaldarse adecuadamente, no debe presentarse como un hecho confirmado.**

---

# 🧪 Testing

El proyecto incluye pruebas automatizadas para validar componentes críticos.

Entre las verificaciones actuales se encuentran:

* disponibilidad de `/ruta-salsera`;
* funcionamiento de la API;
* disponibilidad de `/medellin`;
* comportamiento del endpoint raíz;
* validación de campos requeridos;
* comprobaciones de contenido;
* regresiones de funcionalidades existentes.

El endpoint principal actualmente utiliza:

```text
/
 ↓
302 Redirect
 ↓
/ruta-salsera
 ↓
200 OK
```

La experiencia de Ruta Salsera es, por tanto, la puerta de entrada principal de SalsaQuest.

---

# 🔒 Seguridad y control de cambios

El desarrollo sigue principios de cambios controlados:

* no eliminar datos sin autorización;
* no recrear bases de datos innecesariamente;
* no introducir información inventada;
* evitar modificaciones fuera del alcance de una tarea;
* validar cambios mediante pruebas;
* mantener separadas entidades que representan personas, negocios, marcas u organizaciones diferentes;
* proteger secretos mediante variables de entorno.

Los archivos sensibles no deben incorporarse al repositorio.

---

# 📁 Estructura del proyecto

```text
sonhavanagame/
│
├── app/
│   ├── routes/
│   ├── models/
│   ├── templates/
│   └── static/
│       ├── css/
│       ├── js/
│       ├── images/
│       └── videos/
│
├── tests/
│
├── instance/
│
├── .env.example
├── AGENTS.md
├── PROJECT_REPORT.md
├── README.md
└── run.py
```

---

# 💻 Instalación local

## 1. Clonar

```bash
git clone https://github.com/alvaroberrio23242-eng/salsaquest.git
cd salsaquest
```

## 2. Crear entorno virtual

### Windows

```powershell
python -m venv .venv
```

Activar:

```powershell
.venv\Scripts\activate
```

## 3. Instalar dependencias

```powershell
pip install -r requirements.txt
```

## 4. Configurar variables de entorno

Crear `.env` a partir de `.env.example`.

No incluir secretos reales en Git.

## 5. Ejecutar

```powershell
python run.py
```

Abrir:

```text
http://127.0.0.1:5000
```

La aplicación debería conducir al flujo principal:

```text
http://127.0.0.1:5000/
        ↓
/ruta-salsera
```

---

# 🧪 Ejecutar tests

```powershell
pytest
```

Para obtener información detallada:

```powershell
pytest -v
```

---

# 🗺️ Roadmap

El proyecto continúa evolucionando hacia una experiencia cultural y turística más completa.

### Actual

* [x] Aplicación web Flask
* [x] Ruta Salsera
* [x] Mapa interactivo
* [x] Timeline
* [x] Venues
* [x] Artistas y orquestas
* [x] Radio
* [x] Sellos
* [x] Eventos
* [x] Sistema de evidencia
* [x] Experiencias dinámicas
* [x] Testing
* [x] Deployment

### Evolución

* [ ] Mayor profundidad de datos culturales
* [ ] Rutas temáticas
* [ ] Experiencias personalizadas
* [ ] Mayor integración turística
* [ ] Gamificación avanzada
* [ ] Internacionalización ampliada
* [ ] Integraciones externas
* [ ] Capas inteligentes de recomendación

Las futuras funcionalidades deberán mantener como principios:

**evidencia + seguridad + rendimiento + utilidad + experiencia de usuario.**

---

# 🌎 Visión

SalsaQuest parte de la salsa, pero el concepto puede evolucionar hacia una plataforma de **exploración cultural interactiva**.

La idea es conectar:

```text
Cultura
   +
Geografía
   +
Historia
   +
Música
   +
Turismo
   +
Tecnología
   +
Gamificación
```

para crear experiencias digitales que permitan descubrir una ciudad de una manera diferente.

---

# 👨‍💻 Proyecto

**SalsaQuest** forma parte del ecosistema de proyectos de desarrollo de software de:

**Álvaro Berrío**

Estudiante de Ingeniería de Sistemas enfocado en:

* desarrollo de software;
* aplicaciones web;
* Python;
* Flask;
* arquitectura de sistemas;
* experiencias digitales;
* automatización;
* inteligencia artificial.

---

## 🔗 Enlaces

* **Demo:** https://salsaquest-1.onrender.com/
* **Repositorio:** https://github.com/alvaroberrio23242-eng/salsaquest

---

> **Aquí la salsa importa.**
>
> **SalsaQuest — Medellín se escucha. Medellín se baila.**

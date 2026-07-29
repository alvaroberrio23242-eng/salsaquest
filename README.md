# 🕺 SalsaQuest

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-black?logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-DB-07405E?logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/status-en%20desarrollo-yellow)

**SalsaQuest** es una aplicación web interactiva pensada para turistas que visitan lugares emblemáticos de la cultura salsera (como *Son Havana*). Combina storytelling, trivia gamificada y módulos interactivos para enseñar sobre la historia, la música y los personajes de la salsa de forma accesible y entretenida — todo con un fondo de video de La Habana en loop y una estética "neón salsero".

---

## 🌟 Características

- 🎬 **Fondo de video rotativo** de La Habana con tarjetas de "vidrio esmerilado" (glassmorphism) que dejan ver el video detrás del texto.
- 📜 **Menú e Interacción**: consulta interactiva de productos, bebidas y gastronomía del establecimiento.
- 📅 **Eventos & Cartelera**: sección informativa con las actividades y presentaciones del lugar.
- 🕰️ **Línea de tiempo interactiva** de la historia de la salsa, con filtros por década, trivia, imágenes y video/audio embebido.
- ⭐ **Grandes Eventos de la Salsa**: los conciertos y hitos que marcaron el género (Fania All-Stars, Feria de Cali, etc).
- 🏆 **Récords de la Salsa**: hitos y marcas históricas del género.
- 🕺 **Historias de Artistas y Ritmos**: biografías de La Lupe, Fruko, Afrosound, Gilberto Santa Rosa, Willie Colón, Rubén Blades, Oscar D'León, y del guaguancó como ritmo raíz — con modal de detalle al hacer clic.
- 🥁 **Sección de Timba**: origen del género, récords y playlists curadas.
- 🎯 **Trivia Salsera gamificada** con reto diario y sistema de puntos.
- 🏅 **Leaderboard / Ranking** de los mejores puntajes.
- 🔐 **Registro de usuarios** con captura de datos (lead) y recompensa.
- 🎵 **Reproductor de Spotify** embebido con playlist oficial.
- 👁️ **Contador de visitas** del sitio.
- 🌐 Base para contenido multilingüe (pensado para turistas internacionales).

---

## 🛠️ Tecnologías

| Capa | Tecnología |
|---|---|
| Backend | Python / Flask (Blueprints) |
| Base de datos | SQLite / SQLAlchemy |
| Frontend | HTML5, CSS3 (glassmorphism + neón), JavaScript (vanilla, fetch API) |
| UI | Bootstrap 5, Font Awesome |
| Control de versiones | Git & GitHub |

---

## 📁 Estructura del proyecto

```
salsaquest/
├── run.py                     # Punto de entrada de la app
├── init_db.py                 # Script de inicialización de la base de datos
├── requirements.txt
└── app/
    ├── __init__.py             # Factory de la app Flask, registro de blueprints
    ├── models/
    │   ├── user.py              # Modelo de usuario (auth + leaderboard)
    │   ├── timeline_data.py     # Modelo de la línea de tiempo
    │   ├── content_data.py      # Datos de eventos, récords, artistas y timba
    │   └── visit_counter.py     # Contador de visitas
    ├── routes/
    │   ├── main.py               # Home, trivia, leaderboard
    │   ├── auth.py               # Registro / login
    │   ├── timeline.py           # API de la línea de tiempo
    │   └── content.py            # API de eventos, récords, artistas, timba, visitas
    ├── services/
    │   └── ia_service.py         # Servicio de IA (en desarrollo)
    ├── static/
    │   ├── css/style.css         # Estilos (tema neón + glassmorphism)
    │   ├── js/                   # timeline.js, trivia.js, video-bg.js, content.js
    │   ├── videos/                # Clips de fondo (La Habana)
    │   └── img/                  # Imágenes estáticas
    └── templates/
        ├── index.html            # Página principal
        └── desafio.html          # Pantalla de desafío
```

---

## 🚀 Cómo ejecutar la aplicación localmente

### Requisitos previos

Tener instalado **Python 3.8+** en tu equipo.

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/alvaroberrio23242-eng/salsaquest.git
cd salsaquest

# 2. Crear y activar un entorno virtual
python -m venv .venv
source .venv/bin/activate        # En Windows: .venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar la aplicación
python run.py
```

La app quedará disponible en `http://127.0.0.1:5000`.

### Notas sobre los videos de fondo

Los clips de video (`app/static/videos/habana-1.mp4`, `habana-2.mp4`, `habana-3.mp4`, `habana-carro.mp4`) y la imagen de poster (`app/static/img/cuba-flag.jpg`) no se versionan pesados en el repo por defecto — si vas a agregar los tuyos, comprímelos primero para que la app cargue rápido en celulares:

```bash
ffmpeg -i tu-video.mp4 -vf scale=1280:-1 -crf 28 app/static/videos/habana-1.mp4
```

---

## 🗺️ Roadmap

- [ ] Traducción completa multilingüe (ES/EN)
- [ ] Más artistas e hitos en la sección de Historias
- [ ] Integración de playlists de Spotify curadas por sección
- [ ] Panel de administración para editar contenido sin tocar código

---

## 📄 Licencia

Proyecto en desarrollo activo — licencia por definir.
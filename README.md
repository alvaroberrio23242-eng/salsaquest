# 🎺 SalsaQuest — Plataforma Interactiva de Historia de la Salsa

SalsaQuest es una aplicación web interactiva diseñada para explorar la evolución histórica de la salsa, desafiar conocimientos musicales mediante trivias interactivas y mantener un ranking global de puntuaciones.

---

## 🏗️ Arquitectura del Sistema

El siguiente diagrama ilustra la separación de capas del proyecto utilizando la arquitectura de **Blueprints de Flask** y comunicación asíncrona mediante **API REST**:

```mermaid
graph TD
    subgraph Cliente [Navegador Web / Frontend]
        UI[Bootstrap 5 + CSS3]
        JS[timeline.js / trivia.js]
    end

    subgraph Servidor [Backend - Flask Framework]
        Router[App Factory / __init__.py]
        MainBP[Main Blueprint /routes/main.py]
        TimelineBP[Timeline Blueprint /routes/timeline.py]
        AuthBP[Auth Blueprint /routes/auth.py]
    end

    subgraph Persistencia [Base de Datos]
        ORM[SQLAlchemy ORM]
        DB[(SQLite / sonhavana.db)]
    end

    UI -->|Peticiones HTTP/Fetch| Router
    Router --> MainBP
    Router --> TimelineBP
    Router --> AuthBP

    MainBP -->|Consultas| ORM
    TimelineBP -->|Consultas| ORM
    ORM <---> DB

    TimelineBP -->|JSON Data| JS
    JS -->|Renderizado Dinámico| UI
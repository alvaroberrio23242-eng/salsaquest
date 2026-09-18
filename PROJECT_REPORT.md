## sonhavanagame (SalsaQuest)

**Ruta:** D:\Proyectos\sonhavanagame
**Estado:** 🟠 Incompleto (aplicación Flask funcional con problema de seguridad crítico)
**Evidencia:** Aplicación Flask completa SalsaQuest ( Museo interactivo de la cultura salsera). Ejecutable localmente con `python run.py` (http://127.0.0.1:5000). Tiene patrón factory crear_app(), SQLAlchemy, Flask-Login, contador de visitas, panel admin, leaderboard. Requisito crítico: SECRET_KEY debe estar en variable de entorno (fail-fast si no está). Tiene Procfile (web: gunicorn run:app).
**Stack:**
- Backend: Python/Flask, SQLAlchemy 2.0, Flask-Login
- Frontend: HTML/CSS/JS (Bootstrap 5, glassmorphism, neón), JavaScript vanilla (fetch API)
- Base de datos: SQLite (archivo sonhavana.db, init_db.py crea tablas)
- Infraestructura: Gunicorn (Procfile: web: gunicorn run:app), Render/Railway posible
**Git:** ✅ On branch main, up to date with 'origin/main', clean working tree
**GitHub:** ✅ origin https://github.com/alvaroberrio23242-eng/salsaquest.git (nota: repo nombrado salsaquest, no sonhavanagame)
**Último commit:** 5899155 fix: seguridad de admin/SECRET_KEY, validación robusta de leaderboard (P1+P2), eliminación de endpoint huérfano /api/trivia y limpieza de grammy.js
**¿Pusheado?** ✅ Sí — commit 5899155 está en origin/main
**Deploy:** Requiere configurar variables de entorno (ver `.env.example`). Procfile y estructura listos.
**Production readiness:** REQUIERE TRABAJO
- Puntos fuertes: Aplicación Flask completa y funcional, autenticación/autorización (Flask-Login), leaderboard, panel admin, contador de visitas, modelos SQLAlchemy completos, rutas API completas
- Problemas: commit local modifications en otros proyectos pueden afectar

### Próximo paso único
**Rotar la API key de Anthropic** (la anterior fue expuesta en el historial de git en commit eb14cde a través de este archivo). La nueva key debe configurarse en `.env`.
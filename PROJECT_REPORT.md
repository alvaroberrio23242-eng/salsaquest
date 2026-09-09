## sonhavanagame (SalsaQuest)

**Ruta:** D:\Proyectos\sonhavanagame
**Estado:** 🟠 Incompleto (aplicación Flask funcional con problema de seguridad crítico)
**Evidencia:** Aplicación Flask completa SalsaQuest ( Museo interactivo de la cultura salsera). Ejecutable localmente con `python run.py` (http://127.0.0.1:5000). Tiene patrón factory crear_app(), SQLAlchemy, Flask-Login, contador de visitas, panel admin, leaderboard. El último commit 5899155 pusheado al remote. Requisito crítico: SECRET_KEY debe estar en variable de entorno (fail-fast si no está). .env tiene ANTHROPIC_API_KEY hardcodeada (`REDACTED_API_KEY`) - problema de seguridad grave. .env.example no encontrado en el proyecto. Tiene Procfile (web: gunicorn run:app).
**Stack:**
- Backend: Python/Flask, SQLAlchemy 2.0, Flask-Login
- Frontend: HTML/CSS/JS (Bootstrap 5, glassmorphism, neón), JavaScript vanilla (fetch API)
- Base de datos: SQLite (archivo sonhavana.db, init_db.py crea tablas)
- Infraestructura: Gunicorn (Procfile: web: gunicorn run:app), Render/Railway posible
**Git:** ✅ On branch main, up to date with 'origin/main', clean working tree
**GitHub:** ✅ origin https://github.com/alvaroberrio23242-eng/salsaquest.git (nota: repo nombrado salsaquest, no sonhavanagame)
**Último commit:** 5899155 fix: seguridad de admin/SECRET_KEY, validación robusta de leaderboard (P1+P2), eliminación de endpoint huérfano /api/trivia y limpieza de grammy.js
**¿Pusheado?** ✅ Sí — commit 5899155 está en origin/main
**Deploy:** Parcial — tiene Procfile y estructura, pero ANTHROPIC_API_KEY hardcodeado en .env impide deploy seguro
**Production readiness:** REQUIERE TRABAJO
- Puntos fuertes: Aplicación Flask completa y funcional, autenticación/autorización (Flask-Login), leaderboard, panel admin, contador de visitas, modelos SQLAlchemy completos, rutas API completas
- Problemas: ANTHROPIC_API_KEY hardcodeada en .env (crítico - expuesta en repositorio); falta .env.example; commit local modifications en otros proyectos pueden afectar; las keys de IA deben moverse a variables de entorno

### Próximo paso único
**Eliminar ANTHROPIC_API_KEY hardcodeado de .env y agregar a .env.example solo como placeholder** (nunca commitear keys reales)
# AGENTS.md — SalsaQuest Operating Guidelines

## Overview
SalsaQuest is a Flask-based web application providing a cultural and historical guide to Salsa music in Medellín ("La Ruta Salsera").

## Stack
- **Framework:** Flask 3.1+ / WSGI (Gunicorn)
- **Database:** SQLAlchemy 2.0+ (PostgreSQL in production, SQLite local fallback)
- **Testing:** Pytest (`python -m pytest`)
- **Deployment:** Render (via `render.yaml`)

## Core Rules for Agents
1. **Preserve Business Logic:** Never modify `app/content_data.py` or blueprint structures without explicit authorization.
2. **Database URLs:** Always ensure `DATABASE_URL` replaces `postgres://` with `postgresql://`.
3. **Evidence-Based Historical Content:** Do NOT fabricate historical events, locations, or dates. Maintain research entries in `docs/research/`.
4. **Testing Integrity:** All 26 test cases must pass (`python -m pytest`) before any commit/push.

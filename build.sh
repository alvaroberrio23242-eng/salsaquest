#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
# NOTA: init_db.py NO se corre aqui a proposito. init_db.py hace
# db.drop_all() y borraria usuarios/leaderboard en cada despliegue.
# Las tablas ya se crean solas (sin borrar datos) al arrancar la app,
# via db.create_all() en app/__init__.py y run.py.
# Corre init_db.py manualmente solo la primera vez, o cuando quieras
# resetear los eventos de la timeline a proposito.
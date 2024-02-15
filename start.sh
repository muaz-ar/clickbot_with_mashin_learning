#!/bin/bash
# Warten auf die MySQL-Datenbank
while ! nc -z db 3306; do
  sleep 1
done

# Starten der Python-Anwendung
exec python ./modules/main.py

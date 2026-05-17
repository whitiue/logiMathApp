[app]

# Nombre visible de la app
title = LogiMath

# Nombre interno
package.name = logimath

# Dominio (puede ser cualquiera)
package.domain = org.logimath

# Carpeta del código
source.dir = .

# Extensiones que incluirá
source.include_exts = py,png,jpg,kv,atlas,json

# Archivo principal
entrypoint = main.py

# Versión
version = 1.0

# Dependencias
requirements = python3,kivy,requests

# Orientación
orientation = portrait

# Pantalla completa
fullscreen = 0

# Permisos Android
android.permissions = INTERNET

# API Android
android.api = 33

# Android mínimo
android.minapi = 21

# Arquitecturas
android.archs = arm64-v8a, armeabi-v7a

# Logs
log_level = 2


[buildozer]

# Directorio de compilación
bin_dir = ./bin
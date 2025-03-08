#!/bin/bash

# Verifica si Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "Python3 no está instalado. Por favor instálalo antes de continuar."
    exit 1
fi

# Crea el entorno virtual si no existe
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Entorno virtual creado exitosamente."
fi

# Activa el entorno virtual
source venv/bin/activate

# Instala las dependencias
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "Dependencias instaladas correctamente."
else
    echo "El archivo requirements.txt no se encontró."
    exit 1
fi

echo "Configuración completada. Usa 'source venv/bin/activate' para activar el entorno."

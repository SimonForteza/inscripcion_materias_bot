#!/bin/bash

# Verifica si el archivo .config_done existe
if [ -f ".config_done" ]; then
    echo "La configuración ya ha sido completada previamente."
    echo "Presione cualquier tecla para salir..."
    read -n 1 -s
    exit 0
fi

echo "Iniciando la instalación..."

# Verifica si Python está instalado
if ! command -v python &> /dev/null; then
    echo "Python no está instalado. Por favor instálalo antes de continuar."
    exit 1
fi

# Crea el entorno virtual si no existe
if [ ! -d "venv" ]; then
    python -m venv venv
    venv/bin/python -m pip install --upgrade pip
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

# Solicita el email dos veces y verifica que coincidan
while true; do
    read -p "Ingrese su correo electrónico: " email1
    read -p "Confirme su correo electrónico: " email2

    # Verificación simple de email (contiene @ y .)
    if [[ "$email1" =~ @.*\..* ]]; then
        if [ "$email1" == "$email2" ]; then
            echo "Correo electrónico verificado correctamente."
            break
        else
            echo "Los correos electrónicos no coinciden. Inténtelo de nuevo."
        fi
    else
        echo "Correo electrónico no válido. Intentelo nuevamente."
    fi
done

# Solicita la contraseña dos veces y verifica que coincidan
while true; do
    read -sp "Ingrese su contraseña: " password1
    echo
    read -sp "Confirme su contraseña: " password2
    echo

    if [ "$password1" == "$password2" ]; then
        echo "Contraseña verificada correctamente."
        break
    else
        echo "Las contraseñas no coinciden. Inténtelo de nuevo."
    fi
done

# Guarda el email y la contraseña en el archivo .env
echo "MY_USERNAME=$email1" > .env
echo "PASSWORD=$password1" >> .env

# Ejecuta el script para obtener la URL
export PYTHONPATH=$(pwd)/src
python src/get_url.py

# Crear el archivo de control
touch .config_done
echo "Configuración completada. Usa 'source venv/bin/activate' para activar el entorno."

echo "Configuración completada. Usa 'source venv/bin/activate' para activar el entorno."

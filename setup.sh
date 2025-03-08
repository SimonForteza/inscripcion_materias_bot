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


# Solicita el email dos veces y verifica que coincidan
while true; do
    read -p "Ingrese su correo electrónico: " email1
    read -p "Confirme su correo electrónico: " email2

    # Verificación de formato básico de email
    if [[ ! "$email1" =~ ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$ ]]; then
        echo "Correo electrónico no válido. Inténtelo nuevamente."
        continue
    fi

    if [ "$email1" == "$email2" ]; then
        echo "Correo electrónico verificado correctamente."
        break
    else
        echo "Los correos electrónicos no coinciden. Inténtelo de nuevo."
    fi
done

# Solicita la contraseña dos veces y verifica que coincidan
while true; do
    read -s -p "Ingrese su contraseña: " password1
    echo
    read -s -p "Confirme su contraseña: " password2
    echo

    if [ "$password1" == "$password2" ]; then
        echo "Contraseña verificada correctamente."
        break
    else
        echo "Las contraseñas no coinciden. Inténtelo de nuevo."
    fi
done

# Guarda el email y la contraseña en el archivo .env
cat <<EOF > .env
EMAIL=$email1
PASSWORD=$password1
EOF


#Ejecuta el script para obtener la url
PYTHONPATH=$(pwd)/src python3 src/main.py

# Crear el archivo de control
touch .config_done
echo "Configuración completada. Usa 'source venv/bin/activate' para activar el entorno."

echo "Configuración completada. Usa 'source venv/bin/activate' para activar el entorno."

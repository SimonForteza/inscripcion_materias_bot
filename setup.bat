@echo off

:: Verifica si el archivo .config_done existe
if exist .config_done (
    echo La configuración ya ha sido completada previamente.
    echo Presione cualquier tecla para salir...
    pause >nul
    exit /b 0
)

echo Iniciando la instalacion...

:: Verifica si Python está instalado
where python >nul 2>nul
if errorlevel 1 (
    echo Python no está instalado. Por favor instalalo antes de continuar.
    exit /b 1
)

:: Crea el entorno virtual si no existe
if not exist "venv" (
    python -m venv venv
    python.exe -m pip install --upgrade pip
    echo Entorno virtual creado exitosamente.
)

:: Activa el entorno virtual
call venv\Scripts\activate.bat

:: Instala las dependencias
if exist "requirements.txt" (
    pip install -r requirements.txt
    echo Dependencias instaladas correctamente.
) else (
    echo El archivo requirements.txt no se encontró.
    exit /b 1
)

:: Solicita el email dos veces y verifica que coincidan
:email_loop
set /p email1=Ingrese su correo electronico: 
set /p email2=Confirme su correo electronico: 

:: Verificación simple de email (contiene @ y .)
echo %email1% | findstr "@." >nul
if errorlevel 1 (
    echo Correo electrónico no valido. Intentelo nuevamente.
    goto email_loop
)

if "%email1%"=="%email2%" (
    echo Correo electronico verificado correctamente.
) else (
    echo Los correos electrónicos no coinciden. Inténtelo de nuevo.
    goto email_loop
)

:: Solicita la contraseña dos veces y verifica que coincidan
:password_loop
set /p password1=Ingrese su contraseña: 
set /p password2=Confirme su contraseña: 

if "%password1%"=="%password2%" (
    echo Contraseña verificada correctamente.
) else (
    echo Las contraseñas no coinciden. Inténtelo de nuevo.
    goto password_loop
)

:: Guarda el email y la contraseña en el archivo .env
echo MY_USERNAME=%email1% > .env
echo PASSWORD=%password1% >> .env

:: Ejecuta el script para obtener la URL
set PYTHONPATH=%cd%\src 
python src\get_url.py

:: Crear el archivo de control
type nul > .config_done
echo Configuracion completada. Usa 'call venv\Scripts\activate.bat' para activar el entorno.

echo Configuracion completada. Usa 'call venv\Scripts\activate.bat' para activar el entorno.

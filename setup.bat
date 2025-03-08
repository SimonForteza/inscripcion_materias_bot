@echo off

:: Verifica si Python está instalado
where python >nul 2>nul
if errorlevel 1 (
    echo Python no está instalado. Por favor instálalo antes de continuar.
    exit /b 1
)

:: Crea el entorno virtual si no existe
if not exist "venv" (
    python -m venv venv
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
set /p email1=Ingrese su correo electrónico: 
set /p email2=Confirme su correo electrónico: 

:: Verificación de formato básico de email
echo %email1% | findstr /r "^[a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]*\.[a-zA-Z]{2,}$" >nul
if errorlevel 1 (
    echo Correo electrónico no válido. Inténtelo nuevamente.
    goto email_loop
)

if "%email1%"=="%email2%" (
    echo Correo electrónico verificado correctamente.
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
echo EMAIL=%email1% > .env
echo PASSWORD=%password1% >> .env

:: Ejecuta el script para obtener la URL
set PYTHONPATH=%cd%\src python src\main.py

:: Crear el archivo de control
type nul > .config_done
echo Configuración completada. Usa 'call venv\Scripts\activate.bat' para activar el entorno.

echo Configuración completada. Usa 'call venv\Scripts\activate.bat' para activar el entorno.

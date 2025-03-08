@echo off
REM Verifica si Python está instalado
where python >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo Python no está instalado. Por favor instálalo antes de continuar.
    exit /b
)

REM Crea el entorno virtual si no existe
IF NOT EXIST "venv" (
    python -m venv venv
    echo Entorno virtual creado exitosamente.
)

REM Activa el entorno virtual
call .\venv\Scripts\activate

REM Instala las dependencias
IF EXIST "requirements.txt" (
    pip install -r requirements.txt
    echo Dependencias instaladas correctamente.
) ELSE (
    echo El archivo requirements.txt no se encontró.
    exit /b
)

echo Configuración completada. Usa "venv\Scripts\activate" para activar el entorno.

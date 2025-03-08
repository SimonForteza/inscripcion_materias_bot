from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv
import os
import time

from src.complete_prompt import complete_prompt
from src.data_processing import filter_data, is_valid_subject, get_day_subject, print_tables
from src.subjects import choose_subjects, prueba, get_subjects_names
from src.config import SUBJECTS, turnos, day_index, column_names


def parse_username(email: str) -> str:
    return email.split('@')[0]


def main():
    load_dotenv()
    url = os.getenv("URL")
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get(url)

    except Exception as e:
        print(f"Error while selecting subjects and days: {e}")
    

    username = parse_username(os.getenv("MY_USERNAME"))
    password = os.getenv("PASSWORD")
    time.sleep(1)
    complete_prompt(username, password)
    time.sleep(5)
    button = driver.find_element(By.ID, 'ContentPlaceHolder1_btnSeleccionarMaterias')
    print(button.text)
    button.click()

    # Seleccionar tabla de materias
    tbody = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_ucMateriaInscripcionBuscador_rptMaterias_grdMaterias_1"]/tbody')
    
    # Iterar por cada materia
    for subj in SUBJECTS:
        choose_subjects(subj, tbody)  # Seleccionarla en la página

    # Cerrar ventana de materias
    close_btn = driver.find_element(By.XPATH, '//*[@id="form1"]/div[5]/div[3]/div/button/span')
    close_btn.click()
    
    # Marcar días
    dias_disponibles = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_pnlContenido"]/table/tbody/tr[3]/td/table/tbody/tr[6]/td[4]')
    dias = dias_disponibles.find_elements(By.TAG_NAME, 'input')

    for dia in dias:
        if not dia.is_selected():  # Si no está seleccionado
            dia.click()

    # Se selecciona el turno
    option = driver.find_element(By.XPATH, turnos["3"])
    option_text = option.text

    select = Select(driver.find_element(By.ID, 'ContentPlaceHolder1_cboTurno'))
    select.select_by_visible_text(option_text)

    # Buscar materias
    buscar_btn = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_btnBuscar"]')
    buscar_btn.click()

    time.sleep(2)

    # Crear una lista con los nombres de las materias
    subjects_names_list = get_subjects_names(driver)

    tables = []
    for i in range(len(SUBJECTS)):
        table = []
        tabla_materia = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//*[@id="ContentPlaceHolder1_rptMateriaClases_grdClases_{i}_grdResultados_{i}"]/tbody'))
        )

        filas = tabla_materia.find_elements(By.TAG_NAME, 'tr')

        for fila in filas:
            fila_list = fila.text.split()

            if is_valid_subject(fila_list):
                day_subject = get_day_subject(fila)
                fila_filtered = filter_data(fila_list, day_index[day_subject])
                
                table.append(fila_filtered)

        tables.append(table)

    # IMPRIMIR RESULTADOS
    resultado_imprimir = print_tables(tables, column_names, subjects_names_list)
    time.sleep(2)
    driver.quit()
    print(resultado_imprimir)


if __name__ == "__main__":
    main()
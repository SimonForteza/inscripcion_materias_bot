from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .config import SUBJECTS

def choose_subjects(subject, tbody):
    rows = tbody.find_elements(By.XPATH, 'tr')
    for i in range(1, len(rows)):
        indice = i - 1
        tr = rows[i]
        subject_name = tr.find_element(By.XPATH, './/td[4]')
        if subject_name.text == subject:
            btn = tr.find_element(By.XPATH, f'.//td[1]//span//input[@id="ContentPlaceHolder1_ucMateriaInscripcionBuscador_rptMaterias_grdMaterias_1_chkSeleccionar_{indice}"]')
            if not btn.is_selected():
                btn.click()

def prueba(subjects, tbody):
    rows = tbody.find_elements(By.XPATH, '//*[@id="ContentPlaceHolder1_ucMateriaInscripcionBuscador_rptMaterias_grdMaterias_1"]/tbody')
    for i in range(1, len(rows)):
        indice = i - 1
        tr = rows[i]
        subject_name = tr.find_element(By.XPATH, './/td[@class="colMateria"]')
        if subject_name.text in subjects:
            #btn = tr.find_element(By.XPATH, f'.//td[1]//span//input[@id="ContentPlaceHolder1_ucMateriaInscripcionBuscador_rptMaterias_grdMaterias_1_chkSeleccionar_{indice}"]')
            btn = tr.find_element(By.XPATH, f'//*[@id="ContentPlaceHolder1_ucMateriaInscripcionBuscador_rptMaterias_grdMaterias_1_chkSeleccionar_{indice}"]')
            if not btn.is_selected():
                btn.click()


def get_subjects_names(driver):
    subjects_names = []
    for i in range(1, len(SUBJECTS) + 1):
        span = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'/html/body/form/div[3]/div/div[1]/table/tbody/tr/td/div/table/tbody/tr[4]/td/table/tbody/tr/td/span[{i}]'))
        )
        subjects_names.append(span.text)
    return subjects_names

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import pyperclip

import time
import random

from get_user_information import get_user_info

def type_text(field, email: str):
     """This function types text simulating to being a human"""
     for letra in email:
        field.send_keys(letra)
        time.sleep(0.05)

def avoid_prompt():
    for i in range(3):
        pyautogui.keyDown('tab')
        pyautogui.keyUp('tab')
    
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')


def get_platform_url() -> str:
    url = 'https://inscripciones.uade.edu.ar'
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        #se accede a la pagina
        driver.get(url)

    except Exception as e:
        print(f"Error while getting the URL: {e}")

    time.sleep(2)
    boton_login = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/a'))
    )
    boton_login.click()

    #get the user info
    username, password = get_user_info()
    
    #complete the email adress
    signIn_field = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.XPATH, '//*[@id="i0116"]'))
    )
    type_text(signIn_field, username)
    signIn_field.send_keys(Keys.ENTER)

    time.sleep(2)
    #complete the password
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "i0118"))
    )
    type_text(password_field, password)
    time.sleep(2)
    password_field.send_keys(Keys.ENTER)

    time.sleep(2)
    boton_no = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="idBtn_Back"]'))
    )
    boton_no.click()

    time.sleep(2)
    boton_menu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/ul/li[2]/a'))
    )
    boton_menu.click()

    time.sleep(2)
    boton_inscribite = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="inscripcionesWrapper"]/div[3]/div[1]/div/a'))
    )
    driver.execute_script("arguments[0].click();", boton_inscribite)

    time.sleep(2)
    boton_continuar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/button'))
    )
    driver.execute_script("arguments[0].click();", boton_continuar)

    time.sleep(2)
    avoid_prompt()
    
    for i in range(2):
        pyautogui.keyDown('tab')
        pyautogui.keyUp('tab')
    pyautogui.hotkey('ctrl', 'c')

    # Obtiene la URL después de la redirección
    result_url = pyperclip.paste()
    print(result_url)

    driver.quit()
    return result_url

print(get_platform_url())
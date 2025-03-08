import pyautogui
import time

def complete_prompt(username, password):
    """this function complete the prompt to access the page"""
    
    # Escribir el primer texto
    pyautogui.write(username, interval=0.01)

    # Presionar la tecla Tab
    pyautogui.press('tab')
    time.sleep(1)

    # Escribir el segundo texto
    pyautogui.write(password, interval=0.01)

    # Presionar Enter
    pyautogui.press('enter')

    # Minimizar la ventana
    pyautogui.hotkey('win', 'down')

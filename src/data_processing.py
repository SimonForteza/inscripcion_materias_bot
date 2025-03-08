from selenium.webdriver.common.by import By
from tabulate import tabulate

def filter_data(information: list, day):
    """this function select the wanted data"""
    filtered_info = [information[0], information[1], information[3], information[5], information[6], information[7], information[8], information[9]]
    filtered_info.insert(3, day)
    return filtered_info

def is_valid_subject(subject_info: list):
    """this function check if the subject info is valid"""
    for i in range(len(subject_info)):
        if subject_info[1] != "MONSERRAT" or subject_info[9] == "0":
            return False
    return True

def get_day_subject(tr):
    index = 0
    td_elements = tr.find_elements(By.TAG_NAME, "td")
    for td in td_elements:
        class_name = td.get_attribute("class")
        if class_name == "tdDiaResaltado":
            return index
        index += 1

def print_tables(tables, column_names, subjects_names_list):
    result = []
    
    for i in range(len(subjects_names_list)):
        result.append("\n" + subjects_names_list[i].upper())
        if len(tables[i]) > 0:
            result.append(tabulate(tables[i], headers=column_names, tablefmt="fancy_grid"))
        else:
            result.append("NO HAY VACANTES DISPONIBLES ACTUALMENTE EN ESTE TURNO")
    
    return "\n\n".join(result)


    
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

"""1. import os
   2. pe win: os.system("pip install selenium")
   3. linux: os.system("sudo pip install selenium")"""

# Variabile constante
ADRESA: str = "https://sites.google.com/view/testare-cu-selnium/"
PAG_PRINCIPALA: str = "pag-principala"
PAG1: str = "pagina1"
PAG2: str = "pagina2"

# --------------------------ATENTIE!------------------------------------
# Problema: Gaseste in toate paginile html de mai sus cuvantul [TESTING]
# si afiseaza de cate ori apare
# ----------------------------------------------------------------------

LISTA_ADRESE: list = [PAG_PRINCIPALA, PAG1, PAG2]
CUV_TARGET: str = "[TESTING]"  # Cuv. pe care il cautam
rez_final: list = []  # Stocarea a tuturor elementelor  care contin CUV_TARGET


def navigare(target: str) -> None:
    """Aceasta functie va cauta in toate paginile in format text de mai sus
        prin variabile CUV_TARGET"""
    global rez_final
    # driver.switch_to.new_window("tab")
    elem_list: list = []  # Initializare pentru stocarea elementelor care contin var. CUV_TARGET vezi mai jos
    contor: int = 0  # var. pt a contoriza de cate ori afiseaza in text var. CUV_TARGET
    driver: webdriver = webdriver.Chrome()  # Instantierea obj driver din clasa Chrome
    """Obj "wait" cu scopul de a astepta -> vezi ultimul parametru
    pana cand incarca toate elementele de mai jos"""
    wait: webdriver = WebDriverWait(driver, 10)
    driver.get(f"{ADRESA}{target}")  # Adresa + pagina .html target
    lista_elem: list = wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME, "C9DxTc")))  # Toate elem
    for element in lista_elem:  # Iteratiile
        if CUV_TARGET in element.text:
            elem_list.append(element.text)
    for element1 in elem_list:
        element1 = element1.split(" ")  # Ne va returna o lista din str (metoda)
        for element2 in element1:
            if element2 == CUV_TARGET or CUV_TARGET in element2:
                contor += 1
    if contor > 0:
        rez_final.append(f"In {target}, cuvantul {CUV_TARGET} a fost gasit de {contor} ori ")
    driver.quit()


if __name__ == "__main__":  # Var. speciala de declansare a scriptului
    for adresa in LISTA_ADRESE:  # Iteratia prin toate paginile
        navigare(adresa)
    print(rez_final)

import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class ActionsSelenium:
    def __init__(self, driver):
        self.driver = driver

    def select_type_element(self, type):
        match type:
            case 'id':
                return By.ID
            case 'name':
                return By.NAME
            case 'class':
                return By.CLASS_NAME
            case _:
                raise Exception('Type not found')
            
    def find_element(self, selector, name, timeout=20):
        type = self.select_type_element(selector)

        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located((type, name)))


    def click_element(self, element):
        element.click()


    def exit_app(self):
        self.driver.close()
        os.system("taskkill /f /im winium.exe")

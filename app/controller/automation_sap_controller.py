import yaml
import time
from app.config.configuration import STEPS
from app.utils.log import log_wrapper
from app.libs.actions_selenium import ActionsSelenium
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class SAPAutomation:
    def __init__(self, driver):
        self.actions = ActionsSelenium(driver)

    @log_wrapper
    def load_steps(self):
        with open(r'{}'.format(STEPS), 'r', encoding='utf-8') as file:
            steps = yaml.safe_load(file)
        return steps
    
    @log_wrapper
    def automation_sap(self, steps):
        time.sleep(5)

        window = self.actions.find_element(selector='class', name=steps['WINDOW_MAIN'])
        button_alter_vision = self.actions.find_element(selector='id', name=steps['BUTTON_ALTER_VISION'])
        self.actions.click_element(button_alter_vision)

        select_vision = self.actions.find_element(selector='name', name=steps['SELECT_VISION'])
        self.actions.click_element(select_vision)

        button_new_cnx = self.actions.find_element(selector='id', name=steps['BUTTON_NEW_CNX'])
        self.actions.click_element(button_new_cnx)

        window = self.actions.find_element(selector='class', name=steps['WINDOW_SYSTEM_USER'])
        input_description = window.find_element_by_id(steps['INPUT_DESCRIPTION'])
        input_description.send_keys("SAPGUI")
        
        input_id = window.find_element_by_id(steps['INPUT_ID_SIS'])
        input_id.send_keys("LEO")

        self.actions.exit_app()


    @log_wrapper
    def run(self):
        try:
            steps = self.load_steps()
            self.automation_sap(steps=steps)

        except NoSuchElementException:
            raise 'Element not found'
        
        except TimeoutException:
            raise 'Timeout'
        
        except Exception as ex:
            raise ex
from selenium.webdriver import Remote
from app.config.configuration import WINIUM_DRIVER
import os


class WebDriverFactory:
    @staticmethod
    def create_driver():
        os.startfile(r"{}".format(WINIUM_DRIVER))
        
        capabilities = {
            "debugConnectToRunningApp": 'false',
            "app": r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"
        }

        driver = Remote(command_executor='http://localhost:9999', desired_capabilities=capabilities)

        return driver
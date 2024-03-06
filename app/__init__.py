from app.utils.webdriver_factory import WebDriverFactory
from app.controller.automation_sap_controller import SAPAutomation

driver = WebDriverFactory.create_driver()
automation_controller = SAPAutomation(driver)


def run():
    automation_controller.run()
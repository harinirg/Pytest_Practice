import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities import excelReader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Utilities import logCreator

@pytest.mark.parametrize("username,password", excelReader.get_data("ExcelFiles/LoginData.xlsx","login"))
class TestLogin1:
    def test_validlogin1(self, username, password):
        logger = logCreator.log_generatoor()
        self.driver = webdriver.Chrome()
        logger.info("Opening chrome browser")
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/")
        logger.info("Launching Demoblaze application")
        username = str(username).strip()
        password = str(password).strip()
        print(f"Username from Excel: '{username}'")
        print(f"Password from Excel: '{password}'")
        self.driver.find_element(By.ID, "login2").click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "loginusername")))
        self.driver.find_element(By.ID, "loginusername").send_keys(username)
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)
        logger.info("Enter the login credentials")
        self.driver.find_element(By.XPATH, "//button[text()='Log in']").click()
        try:
            alert = WebDriverWait(self.driver, 3).until(EC.alert_is_present())
            print("Login Failed :", alert.text)
            logger.info("Login failed")
            alert.accept()
        except:
            welcome_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "nameofuser"))).text
            logger.info("Login successful")
            print("Login Successful :", welcome_text)
        self.driver.quit()
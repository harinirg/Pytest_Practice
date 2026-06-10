from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    
    def __init__(self,driver):
        self.driver = driver
    email="//input[@placeholder='E-Mail Address']"
    password="//input[@placeholder='Password']"
    login_btn="//input[@class='btn btn-primary']"
    account="//h2[contains(text(),'My Account')]"
    def enter_login_details(self, email, password):
        self.driver.find_element(By.XPATH, self.email).send_keys(email)
        self.driver.find_element(By.XPATH, self.password).send_keys(password)
        self.driver.find_element(By.XPATH, self.login_btn).click()
    def login_title(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.account))).text
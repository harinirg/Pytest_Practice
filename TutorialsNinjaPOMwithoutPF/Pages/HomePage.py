from selenium.webdriver.common.by import By

class HomePage:
    
    def __init__(self,driver):
        self.driver = driver
    
    search_box_field = "search"
    search_button = "//button[contains(@class,'btn-default')]"
    myaccount="//a[@title='My Account']"
    login="//a[text()='Login']"

    def search_action(self,search):
        self.driver.find_element(By.NAME,self.search_box_field).send_keys(search)

    def click_login_button(self):
        self.driver.find_element(By.XPATH,self.myaccount).click()
        self.driver.find_element(By.XPATH,self.login).click()

    def click_search_button(self):
        self.driver.find_element(By.XPATH,self.search_button).click()
    
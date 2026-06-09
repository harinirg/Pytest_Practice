import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.mark.parametrize('browser',['chrome','firefox'])
@pytest.mark.parametrize('input_url',['https://www.flipkart.com/','https://www.amazon.in/'])
def test_url(browser,input_url):
    if browser == "chrome" :
        web_driver = webdriver.Chrome()
    if browser == "firefox" :
        web_driver = webdriver.Firefox()
    web_driver.maximize_window()
    web_driver.get(input_url)
    print(web_driver.title)
    time.sleep(5)
    web_driver.close()
import pytest
from selenium import webdriver
@pytest.mark.parametrize("input_browser", ["chrome", "edge"])
@pytest.mark.parametrize("input_url", ["https://www.flipkart.com/", "https://www.amazon.com/"])
def test_url(input_browser, input_url):
    if input_browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
    elif input_browser == "edge":
        options = webdriver.EdgeOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Edge(options=options)
    driver.get(input_url)
    print(f"Browser: {input_browser}")
    print(f"Title: {driver.title}")
    driver.quit()
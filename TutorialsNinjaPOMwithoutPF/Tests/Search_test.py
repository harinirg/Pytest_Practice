import pytest
from selenium.webdriver.common.by import By
from Pages.HomePage import HomePage
from Pages.SearchPage import SearchPage


@pytest.mark.usefixtures("setup_and_teardown")

class TestSearch:
    
    def test_validproduct(self):
        
        homepage = HomePage(self.driver)
        homepage.search_action("HP")
        homepage.click_search_button()
        
        searchpage = SearchPage(self.driver)
        print(searchpage.display_status)
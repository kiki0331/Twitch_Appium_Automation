import os
import json
import allure
from core_framework.base_page import BasePage

class HomePageScript(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(current_dir, "..", "pages", "home_page.json") 
        with open(json_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    @allure.step("Go to home page by URL")
    def go_to_home_page_by_url(self):
        self.driver.get("https://m.twitch.tv/")

    @allure.step("Close popup and click search")
    def close_popup_and_click_search(self):
        self.click_element(self.data["close_button"])
        self.click_element(self.data["search_button"])

import os
import json
import allure
from core_framework.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(current_dir, "..", "pages", "search_page.json") 
        with open(json_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    @allure.step("Perform search for keyword: {keyword}")
    def perform_search(self, keyword):
        self.click_element(self.data["input_button"])
        self.send_key(self.data['input_button'], keyword)
        self.click_element(self.data['title1_button'])

    @allure.step("Verify search results and video playback")
    def verify_results_and_playback(self, search_keyword):
        self.wait_element(self.data['streamer_button'])
        self.scroll_page(500)
        self.wait_element(self.data['last_video'])
        self.scroll_page(-500)
        self.click_element(self.data['streamer_button'])
        self.wait_video_playing()
        self.element_screenshot(f"screenshot_{search_keyword}.png")

import json
from ui_function import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        with open("home_page.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def close_popup_and_click_search(self):
        self.driver.get("https://m.twitch.tv/")
        self.click_element(self.data['close_button'], "close_button")
        self.click_element(self.data['search_button'], "search_button")

class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        with open("search_page.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def perform_search(self, keyword):
        self.click_element(self.data['input_button'], "input_button")
        self.send_key(self.data['input_button'], "search_input", keyword)
        self.click_element(self.data['title1_button'], "select_game")

    def verify_results_and_playback(self, search_keyword):
        self.wait_element(self.data['streamer_button'], "streamer_button")
        self.scroll_page(500)
        self.wait_element(self.data['last_video'], "last_video")
        self.scroll_page(-500)
        self.click_element(self.data['streamer_button'], "streamer_button")
        self.wait_video_playing()
        self.element_screenshot(f"screenshot_{search_keyword}.png")
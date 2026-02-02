import pytest
from test_ui_step import HomePage, SearchPage

@pytest.mark.parametrize("search_term, url_term", [("StarCraft II", "StarCraft%20II")])
def test_twitch_ui_workflow(shared_driver, search_term, url_term):
    home = HomePage(shared_driver)
    search = SearchPage(shared_driver)
    
    home.close_popup_and_click_search()
    
    search.perform_search(search_term)
    search.wait_url_contains(url_term) 
    search.verify_results_and_playback(search_term)